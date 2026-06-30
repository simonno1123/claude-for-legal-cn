#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");

const SERVER_VERSION = "0.1.0";
const ROOT = path.resolve(__dirname, "..", "..");
const SAMPLE_INDEX = path.join(__dirname, "local-index.sample.json");

const AUTHORITY_ORDER = {
  guiding_case: 1,
  reference_case: 2,
  gazette_case: 3,
  typical_case: 4,
  judicial_answer: 5,
  ordinary_judgment: 6,
  manual_upload: 7
};

const TOOL_DEFINITIONS = [
  {
    name: "law_search",
    description: "Search local China laws, administrative regulations, judicial interpretations, local rules, and regulatory materials.",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string" },
        authority_level: { type: "string" },
        status: { type: "string" },
        limit: { type: "integer", minimum: 1, maximum: 50 }
      },
      required: ["query"]
    }
  },
  {
    name: "article_lookup",
    description: "Look up a specific article by regulation title/alias and article number.",
    inputSchema: {
      type: "object",
      properties: {
        regulation: { type: "string" },
        article: { type: "string" }
      },
      required: ["regulation", "article"]
    }
  },
  {
    name: "regulation_detail",
    description: "Return metadata and article list for a regulation in the local index.",
    inputSchema: {
      type: "object",
      properties: {
        regulation: { type: "string" },
        include_articles: { type: "boolean" }
      },
      required: ["regulation"]
    }
  },
  {
    name: "case_search",
    description: "Search guiding cases, reference cases, gazette cases, typical cases, judicial answers, and ordinary judgments in the local index.",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string" },
        authority_rank: { type: "string" },
        limit: { type: "integer", minimum: 1, maximum: 50 }
      },
      required: ["query"]
    }
  },
  {
    name: "case_detail",
    description: "Return one case by id or case number.",
    inputSchema: {
      type: "object",
      properties: {
        id: { type: "string" },
        case_number: { type: "string" }
      }
    }
  },
  {
    name: "case_authority_rank",
    description: "Rank cases by China-law authority level; ordinary judgments are persuasive references only.",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string" },
        case_ids: { type: "array", items: { type: "string" } },
        limit: { type: "integer", minimum: 1, maximum: 50 }
      }
    }
  },
  {
    name: "judicial_answer_search",
    description: "Search Supreme People's Court judicial answer entries in the local index.",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string" },
        limit: { type: "integer", minimum: 1, maximum: 50 }
      },
      required: ["query"]
    }
  },
  {
    name: "judicial_answer_detail",
    description: "Return one judicial answer by id.",
    inputSchema: {
      type: "object",
      properties: {
        id: { type: "string" }
      },
      required: ["id"]
    }
  },
  {
    name: "citation_check",
    description: "Check legal citations and case numbers against the local index and return verification status.",
    inputSchema: {
      type: "object",
      properties: {
        text: { type: "string" },
        citations: { type: "array", items: { type: "string" } }
      }
    }
  }
];

function today() {
  return new Date().toISOString().slice(0, 10);
}

function normalize(value) {
  return String(value || "").trim().toLowerCase();
}

function compact(value) {
  return normalize(value).replace(/[《》中华人民共和国\s]/g, "");
}

function limitOf(args, fallback = 10) {
  const n = Number(args && args.limit);
  if (!Number.isFinite(n)) return fallback;
  return Math.max(1, Math.min(50, Math.trunc(n)));
}

function repoRelative(file) {
  return path.relative(ROOT, file);
}

function loadIndex() {
  const configured = process.env.LOCAL_LEGAL_INDEX;
  const candidates = [];
  if (configured) {
    const resolved = path.resolve(process.cwd(), configured);
    candidates.push(resolved);
    candidates.push(path.join(resolved, "index.json"));
    candidates.push(path.join(resolved, "local-index.json"));
  }
  candidates.push(SAMPLE_INDEX);

  for (const candidate of candidates) {
    try {
      if (!fs.existsSync(candidate) || !fs.statSync(candidate).isFile()) continue;
      const data = JSON.parse(fs.readFileSync(candidate, "utf8"));
      return {
        data: {
          version: data.version || "unknown",
          generated_at: data.generated_at || null,
          source_note: data.source_note || "",
          regulations: Array.isArray(data.regulations) ? data.regulations : [],
          cases: Array.isArray(data.cases) ? data.cases : [],
          judicial_answers: Array.isArray(data.judicial_answers) ? data.judicial_answers : []
        },
        index_path: candidate,
        using_sample: candidate === SAMPLE_INDEX
      };
    } catch (error) {
      return {
        data: { version: "error", generated_at: null, source_note: "", regulations: [], cases: [], judicial_answers: [] },
        index_path: candidate,
        using_sample: false,
        load_error: String(error && error.message ? error.message : error)
      };
    }
  }

  return {
    data: { version: "missing", generated_at: null, source_note: "", regulations: [], cases: [], judicial_answers: [] },
    index_path: null,
    using_sample: false,
    load_error: "No local legal index found."
  };
}

const INDEX = loadIndex();

function baseMeta() {
  return {
    connector: "legal-data",
    connector_version: SERVER_VERSION,
    provider: INDEX.using_sample ? "sample-local-index" : "local-index",
    index_path: INDEX.index_path ? repoRelative(INDEX.index_path) : null,
    index_generated_at: INDEX.data.generated_at,
    retrieved_at: today(),
    needs_manual_verification: true,
    verification_note: INDEX.using_sample
      ? "Using bundled sample index. Replace with official/commercial/enterprise-authorized index before relying on results."
      : "Local index result. Verify against official or enterprise-authorized source before relying on it.",
    load_error: INDEX.load_error || null
  };
}

function regulationNames(reg) {
  return [reg.title, ...(reg.aliases || [])].filter(Boolean);
}

function regulationMatches(reg, query) {
  const q = normalize(query);
  const cq = compact(query);
  return regulationNames(reg).some((name) => normalize(name).includes(q) || compact(name).includes(cq));
}

function findRegulation(query) {
  return INDEX.data.regulations.find((reg) => regulationMatches(reg, query));
}

function articleMatches(article, articleQuery) {
  const q = String(articleQuery || "").trim();
  const digits = q.replace(/[^\d]/g, "");
  return article.article_no === q || (digits && article.article_no && article.article_no.replace(/[^\d]/g, "") === digits);
}

function sourceEnvelope(item) {
  return {
    source_type: item.source_type || "local-index",
    source_name: item.source_name || null,
    source_url: item.source_url || null,
    retrieved_at: item.retrieved_at || null,
    status: item.status || null,
    freshness: item.freshness || null
  };
}

function lawSearch(args) {
  const query = args.query || "";
  const q = normalize(query);
  const cq = compact(query);
  const limit = limitOf(args);
  const results = [];

  for (const reg of INDEX.data.regulations) {
    if (args.authority_level && reg.authority_level !== args.authority_level) continue;
    if (args.status && reg.status !== args.status) continue;
    const nameHit = regulationNames(reg).some((name) => normalize(name).includes(q) || compact(name).includes(cq));
    const articleHits = (reg.articles || []).filter((article) => {
      return normalize(article.article_no).includes(q) ||
        normalize(article.heading).includes(q) ||
        normalize(article.text).includes(q) ||
        compact(article.text).includes(cq);
    });
    if (!nameHit && articleHits.length === 0) continue;
    results.push({
      id: reg.id,
      title: reg.title,
      aliases: reg.aliases || [],
      authority_level: reg.authority_level,
      issuing_authority: reg.issuing_authority,
      effective_date: reg.effective_date,
      status: reg.status,
      source: sourceEnvelope(reg),
      matched_articles: articleHits.slice(0, 5).map((article) => ({
        article_no: article.article_no,
        heading: article.heading,
        snippet: article.text
      }))
    });
  }

  return { meta: baseMeta(), query, count: results.length, results: results.slice(0, limit) };
}

function articleLookup(args) {
  const reg = findRegulation(args.regulation);
  if (!reg) {
    return { meta: baseMeta(), found: false, regulation: args.regulation, article: args.article, message: "Regulation not found in local index." };
  }
  const article = (reg.articles || []).find((item) => articleMatches(item, args.article));
  if (!article) {
    return { meta: baseMeta(), found: false, regulation: reg.title, article: args.article, message: "Article not found in local index." };
  }
  return {
    meta: baseMeta(),
    found: true,
    regulation: {
      id: reg.id,
      title: reg.title,
      authority_level: reg.authority_level,
      issuing_authority: reg.issuing_authority,
      effective_date: reg.effective_date,
      status: reg.status,
      source: sourceEnvelope(reg)
    },
    article
  };
}

function regulationDetail(args) {
  const reg = findRegulation(args.regulation);
  if (!reg) return { meta: baseMeta(), found: false, regulation: args.regulation, message: "Regulation not found in local index." };
  const detail = { ...reg, source: sourceEnvelope(reg) };
  if (!args.include_articles) delete detail.articles;
  return { meta: baseMeta(), found: true, regulation: detail };
}

function textMatches(record, query, fields) {
  const q = normalize(query);
  return fields.some((field) => {
    const value = record[field];
    if (Array.isArray(value)) return value.some((item) => normalize(item).includes(q));
    return normalize(value).includes(q);
  });
}

function caseSearch(args) {
  const query = args.query || "";
  const limit = limitOf(args);
  const results = INDEX.data.cases
    .filter((item) => !args.authority_rank || item.authority_rank === args.authority_rank)
    .filter((item) => textMatches(item, query, ["title", "case_number", "court", "summary", "holding", "focus"]))
    .sort((a, b) => (AUTHORITY_ORDER[a.authority_rank] || 99) - (AUTHORITY_ORDER[b.authority_rank] || 99))
    .slice(0, limit)
    .map((item) => ({
      id: item.id,
      title: item.title,
      case_number: item.case_number,
      case_type: item.case_type,
      authority_rank: item.authority_rank,
      court: item.court,
      decision_date: item.decision_date,
      focus: item.focus || [],
      summary: item.summary,
      source: sourceEnvelope(item),
      needs_manual_verification: item.needs_manual_verification !== false
    }));
  return { meta: baseMeta(), query, count: results.length, results };
}

function caseDetail(args) {
  const id = normalize(args.id);
  const caseNumber = normalize(args.case_number);
  const item = INDEX.data.cases.find((entry) => normalize(entry.id) === id || normalize(entry.case_number) === caseNumber);
  if (!item) return { meta: baseMeta(), found: false, message: "Case not found in local index." };
  return { meta: baseMeta(), found: true, case: { ...item, source: sourceEnvelope(item) } };
}

function caseAuthorityRank(args) {
  let pool = INDEX.data.cases.slice();
  if (Array.isArray(args.case_ids) && args.case_ids.length) {
    const ids = new Set(args.case_ids.map(normalize));
    pool = pool.filter((item) => ids.has(normalize(item.id)) || ids.has(normalize(item.case_number)));
  } else if (args.query) {
    pool = caseSearch({ query: args.query, limit: args.limit || 50 }).results;
  }
  const ranked = pool
    .map((item) => ({
      id: item.id,
      title: item.title,
      case_number: item.case_number,
      authority_rank: item.authority_rank,
      rank_order: AUTHORITY_ORDER[item.authority_rank] || 99,
      rank_note: authorityNote(item.authority_rank),
      source: sourceEnvelope(item),
      needs_manual_verification: item.needs_manual_verification !== false
    }))
    .sort((a, b) => a.rank_order - b.rank_order)
    .slice(0, limitOf(args));
  return { meta: baseMeta(), count: ranked.length, results: ranked };
}

function authorityNote(rank) {
  switch (rank) {
    case "guiding_case": return "指导性案例，参考强度最高，但仍不替代法律和司法解释。";
    case "reference_case": return "人民法院案例库参考案例，可校准裁判思路。";
    case "gazette_case": return "最高人民法院公报案例，具有较高参考价值。";
    case "typical_case": return "典型案例/监管案例，用于政策和裁判倾向参考。";
    case "judicial_answer": return "法答网精选问答，仅作司法问答参考。";
    case "ordinary_judgment": return "普通裁判文书，仅作类案趋势和说理参考。";
    default: return "未知权威等级，必须人工复核。";
  }
}

function judicialAnswerSearch(args) {
  const query = args.query || "";
  const results = INDEX.data.judicial_answers
    .filter((item) => textMatches(item, query, ["title", "topic", "question", "answer_summary"]))
    .slice(0, limitOf(args))
    .map((item) => ({
      id: item.id,
      title: item.title,
      topic: item.topic || [],
      published_at: item.published_at,
      answer_summary: item.answer_summary,
      authority_rank: item.authority_rank || "judicial_answer",
      source: sourceEnvelope(item),
      needs_manual_verification: item.needs_manual_verification !== false
    }));
  return { meta: baseMeta(), query, count: results.length, results };
}

function judicialAnswerDetail(args) {
  const item = INDEX.data.judicial_answers.find((entry) => normalize(entry.id) === normalize(args.id));
  if (!item) return { meta: baseMeta(), found: false, message: "Judicial answer not found in local index." };
  return { meta: baseMeta(), found: true, judicial_answer: { ...item, source: sourceEnvelope(item) } };
}

function extractCitations(args) {
  const citations = [];
  if (Array.isArray(args.citations)) citations.push(...args.citations.map(String));
  const text = String(args.text || "");
  const re = /《([^》]+)》\s*第\s*([一二三四五六七八九十百千万零〇\d]+)\s*条/g;
  let match;
  while ((match = re.exec(text))) citations.push(`《${match[1]}》第${match[2]}条`);
  return [...new Set(citations.map((item) => item.trim()).filter(Boolean))];
}

function parseCitation(citation) {
  const match = citation.match(/《([^》]+)》\s*第\s*([一二三四五六七八九十百千万零〇\d]+)\s*条/);
  if (!match) return null;
  return { regulation: match[1], article: `第${match[2]}条` };
}

function citationCheck(args) {
  const citations = extractCitations(args);
  const checked = citations.map((citation) => {
    const parsed = parseCitation(citation);
    if (!parsed) {
      const caseMatch = INDEX.data.cases.find((item) => normalize(item.case_number) === normalize(citation) || normalize(item.id) === normalize(citation));
      return caseMatch
        ? { citation, type: "case", exists: true, status: "found", match: { id: caseMatch.id, case_number: caseMatch.case_number, authority_rank: caseMatch.authority_rank }, source: sourceEnvelope(caseMatch), needs_manual_verification: true }
        : { citation, type: "unknown", exists: false, status: "unsupported-format", warning: "Only 《法规名》第N条 and indexed case ids/numbers are supported in this local checker." };
    }
    const result = articleLookup(parsed);
    if (!result.found) {
      return { citation, type: "law_article", exists: false, status: "not-found", parsed, warning: result.message };
    }
    return {
      citation,
      type: "law_article",
      exists: true,
      status: result.regulation.status || "unknown",
      parsed,
      match: {
        regulation_id: result.regulation.id,
        title: result.regulation.title,
        article_no: result.article.article_no,
        heading: result.article.heading,
        pinpoint_status: result.article.pinpoint_status || "unknown"
      },
      source: result.regulation.source,
      needs_manual_verification: true
    };
  });
  return { meta: baseMeta(), count: checked.length, results: checked };
}

const TOOL_HANDLERS = {
  law_search: lawSearch,
  article_lookup: articleLookup,
  regulation_detail: regulationDetail,
  case_search: caseSearch,
  case_detail: caseDetail,
  case_authority_rank: caseAuthorityRank,
  judicial_answer_search: judicialAnswerSearch,
  judicial_answer_detail: judicialAnswerDetail,
  citation_check: citationCheck
};

function jsonResponse(id, result) {
  return { jsonrpc: "2.0", id, result };
}

function jsonError(id, code, message, data) {
  return { jsonrpc: "2.0", id, error: { code, message, data } };
}

function handleMessage(message) {
  if (!message || typeof message !== "object") return null;
  const { id, method, params = {} } = message;
  if (!method || method.startsWith("notifications/")) return null;

  try {
    if (method === "initialize") {
      return jsonResponse(id, {
        protocolVersion: "2024-11-05",
        capabilities: { tools: {} },
        serverInfo: { name: "claude-for-legal-cn/legal-data", version: SERVER_VERSION }
      });
    }
    if (method === "tools/list") return jsonResponse(id, { tools: TOOL_DEFINITIONS });
    if (method === "tools/call") {
      const name = params.name;
      const handler = TOOL_HANDLERS[name];
      if (!handler) return jsonError(id, -32601, `Unknown tool: ${name}`);
      const result = handler(params.arguments || {});
      return jsonResponse(id, { content: [{ type: "text", text: JSON.stringify(result, null, 2) }] });
    }
    return jsonError(id, -32601, `Unknown method: ${method}`);
  } catch (error) {
    return jsonError(id, -32000, error && error.message ? error.message : String(error));
  }
}

function encodeMessage(payload) {
  const body = Buffer.from(JSON.stringify(payload), "utf8");
  return Buffer.concat([Buffer.from(`Content-Length: ${body.length}\r\n\r\n`, "utf8"), body]);
}

function startStdioServer() {
  let buffer = Buffer.alloc(0);
  process.stdin.on("data", (chunk) => {
    buffer = Buffer.concat([buffer, chunk]);
    while (true) {
      const headerEnd = buffer.indexOf("\r\n\r\n");
      if (headerEnd === -1) return;
      const header = buffer.slice(0, headerEnd).toString("utf8");
      const match = header.match(/Content-Length:\s*(\d+)/i);
      if (!match) {
        buffer = buffer.slice(headerEnd + 4);
        continue;
      }
      const length = Number(match[1]);
      const bodyStart = headerEnd + 4;
      const bodyEnd = bodyStart + length;
      if (buffer.length < bodyEnd) return;
      const raw = buffer.slice(bodyStart, bodyEnd).toString("utf8");
      buffer = buffer.slice(bodyEnd);
      let message;
      try {
        message = JSON.parse(raw);
      } catch (error) {
        process.stdout.write(encodeMessage(jsonError(null, -32700, "Parse error", String(error))));
        continue;
      }
      const response = handleMessage(message);
      if (response) process.stdout.write(encodeMessage(response));
    }
  });
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function selfTest() {
  const labor47 = articleLookup({ regulation: "劳动合同法", article: "47" });
  assert(labor47.found, "expected Labor Contract Law Article 47");
  const company88 = citationCheck({ text: "请核验《公司法》第88条和《不存在法》第1条。" });
  assert(company88.count === 2, "expected two citation checks");
  assert(company88.results.some((item) => item.exists), "expected one existing citation");
  assert(company88.results.some((item) => !item.exists), "expected one missing citation");
  const ranked = caseAuthorityRank({ query: "出资", limit: 5 });
  assert(Array.isArray(ranked.results), "expected ranked case results");
  const tools = handleMessage({ jsonrpc: "2.0", id: 1, method: "tools/list" });
  assert(tools.result.tools.length >= 9, "expected MCP tools list");
  process.stdout.write(JSON.stringify({
    ok: true,
    server_version: SERVER_VERSION,
    index_path: repoRelative(INDEX.index_path),
    using_sample: INDEX.using_sample,
    tools: TOOL_DEFINITIONS.map((tool) => tool.name)
  }, null, 2) + "\n");
}

if (require.main === module) {
  if (process.argv.includes("--self-test")) selfTest();
  else startStdioServer();
}

module.exports = {
  handleMessage,
  TOOL_HANDLERS,
  loadIndex
};
