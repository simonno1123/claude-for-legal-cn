#!/usr/bin/env bash
# Smoke-test the local legal-data MCP server without requiring network or API keys.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

node "$ROOT/connectors/legal-data/server.js" --self-test >/tmp/legal-data-self-test.json
python3 -m json.tool /tmp/legal-data-self-test.json >/dev/null
python3 - "$ROOT" <<'PY'
import json, subprocess, sys
root = sys.argv[1]
out = subprocess.check_output([
    "node",
    "-e",
    """
const srv = require('./connectors/legal-data/server.js');
const call = (name, args) => srv.handleMessage({jsonrpc:'2.0', id:1, method:'tools/call', params:{name, arguments:args}}).result.content[0].text;
const article = JSON.parse(call('article_lookup', {regulation:'劳动合同法', article:'第47条'}));
const cite = JSON.parse(call('citation_check', {text:'《公司法》第54条；《不存在法》第1条'}));
if (!article.found) throw new Error('article_lookup failed');
if (!cite.results.some(x => x.exists) || !cite.results.some(x => !x.exists)) throw new Error('citation_check did not return mixed results');
console.log(JSON.stringify({ok:true, article: article.article.article_no, citation_count: cite.count}));
"""
], cwd=root)
json.loads(out)
PY
rm -f /tmp/legal-data-self-test.json
echo "  ✓ legal-data local MCP smoke test"
