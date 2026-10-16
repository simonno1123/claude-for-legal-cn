$ErrorActionPreference = 'Stop'
$utf8 = [Text.UTF8Encoding]::new($false, $true)
[Console]::OutputEncoding = $utf8
$root = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/'
$executable = 'C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
$executableSha = 'B847BB9F4E48C19F585C8BF7D8B355F3F8C6D2125717ECE9C9D7E16FB9F09DE8'
$sources = '[{"Role":"scalar","Path":"validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_CANDIDATE_REV1.py","SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},{"Role":"tree","Path":"validation/route_b_c03/wp_008/RDM_CANON2_STRUCTURAL_LAYOUT_CANDIDATE_REV1.py","SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},{"Role":"binding","Path":"validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_CANDIDATE_REV1.py","SHA256":"32535D3E4800E39E8AAF510166AD2AF04E0436D39E7C0BAD528B329D24E66821","Bytes":5799},{"Role":"validation","Path":"validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_VALIDATION_REV1.py","SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}]' | ConvertFrom-Json
$definitions = '[{"Id":"MU-B01","TargetRole":"binding","Before":"_require(document_sha == data[\"document_sha256\"], \"DOCUMENT_SHA_MISMATCH\")","After":"_require(True, \"DOCUMENT_SHA_MISMATCH\")","ExpectedAssertion":"L-LABEL-STALE-FULL-SHA","Topic":"全文散列保护移除","Matches":1,"MutatedSHA256":"11EBD7A12AF07BEAA4EDD8245EE13100629BEACA8302B41E06C67B7CB8EFB973","MutatedBytes":5764},{"Id":"MU-B02","TargetRole":"binding","Before":"_require(aggregate[\"sha256\"] == stream_sha, \"BODY_AGGREGATE_SHA_MISMATCH\")","After":"_require(True, \"BODY_AGGREGATE_SHA_MISMATCH\")","ExpectedAssertion":"B-AGGREGATE-MISMATCH","Topic":"正文聚合散列保护移除","Matches":1,"MutatedSHA256":"03CD28E0F619ED747DEFBCCF2264461B1D668E10E5D2AEA38809CFD0E115358B","MutatedBytes":5770},{"Id":"MU-B03","TargetRole":"binding","Before":"_require(aggregate[\"entry_count\"] == count, \"BODY_COUNT_MISMATCH\")","After":"_require(True, \"BODY_COUNT_MISMATCH\")","ExpectedAssertion":"B-COUNT-MISMATCH","Topic":"正文条目数保护移除","Matches":1,"MutatedSHA256":"EC5113EE8477E692805F5BCB0E59750D322A4FD7D4719655E4165B72FEE86886","MutatedBytes":5770},{"Id":"MU-B04","TargetRole":"binding","Before":"_require(aggregate[\"byte_total\"] == total, \"BODY_TOTAL_MISMATCH\")","After":"_require(True, \"BODY_TOTAL_MISMATCH\")","ExpectedAssertion":"B-TOTAL-MISMATCH","Topic":"正文总字节数保护移除","Matches":1,"MutatedSHA256":"73D3A0FAD551855816817F11A42D5B0014172CB19E645F9AE2D473A58438CD59","MutatedBytes":5771},{"Id":"MU-B05","TargetRole":"binding","Before":"_require(data[\"aggregate_sha256\"] == stream_sha, \"DETACHED_AGGREGATE_SHA_MISMATCH\")","After":"_require(True, \"DETACHED_AGGREGATE_SHA_MISMATCH\")","ExpectedAssertion":"D-MISMATCH-AGGREGATE_SHA256","Topic":"detached 聚合散列保护移除","Matches":1,"MutatedSHA256":"9F1E2087EA471904969BF58ADF34C4F129ACC038D5D8F971F3326C9F2A941183","MutatedBytes":5765},{"Id":"MU-B06","TargetRole":"binding","Before":"_require(data[\"entry_count\"] == count, \"DETACHED_COUNT_MISMATCH\")","After":"_require(True, \"DETACHED_COUNT_MISMATCH\")","ExpectedAssertion":"D-MISMATCH-ENTRY_COUNT","Topic":"detached 条目数保护移除","Matches":1,"MutatedSHA256":"E38808C8846B503EC9E7EA2D9C806DDF6DB7DEEEAF8765AF4612A141C4874D0A","MutatedBytes":5775},{"Id":"MU-B07","TargetRole":"binding","Before":"_require(data[\"byte_total\"] == total, \"DETACHED_TOTAL_MISMATCH\")","After":"_require(True, \"DETACHED_TOTAL_MISMATCH\")","ExpectedAssertion":"D-MISMATCH-BYTE_TOTAL","Topic":"detached 总字节数保护移除","Matches":1,"MutatedSHA256":"D2547E6CBA6574643CAB94FFE8662AF45AF975A297D9D94173617BD1B00E589D","MutatedBytes":5776},{"Id":"MU-B08","TargetRole":"binding","Before":"QUALIFIER = \"DATA_CONSISTENCY_ONLY_NO_SOURCE_OR_AUTHORITY\"","After":"QUALIFIER = \"DATA_CONSISTENCY_ONLY\"","ExpectedAssertion":"P-ONE.QUALIFIER","Topic":"非权威限定语不完整","Matches":1,"MutatedSHA256":"5B3351956372A90A10A86A4EEC8D47C37595DE8289C6105CAF954F45B9C6BA88","MutatedBytes":5776}]' | ConvertFrom-Json
$cases = '[{"Id":"BASE-BINDING","Mode":"binding","ExpectedAssertion":null,"Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"32535D3E4800E39E8AAF510166AD2AF04E0436D39E7C0BAD528B329D24E66821","Bytes":5799},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},{"Id":"MU-B01","Mode":"binding","ExpectedAssertion":"L-LABEL-STALE-FULL-SHA","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"11EBD7A12AF07BEAA4EDD8245EE13100629BEACA8302B41E06C67B7CB8EFB973","Bytes":5764},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},{"Id":"MU-B02","Mode":"binding","ExpectedAssertion":"B-AGGREGATE-MISMATCH","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"03CD28E0F619ED747DEFBCCF2264461B1D668E10E5D2AEA38809CFD0E115358B","Bytes":5770},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},{"Id":"MU-B03","Mode":"binding","ExpectedAssertion":"B-COUNT-MISMATCH","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"EC5113EE8477E692805F5BCB0E59750D322A4FD7D4719655E4165B72FEE86886","Bytes":5770},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},{"Id":"MU-B04","Mode":"binding","ExpectedAssertion":"B-TOTAL-MISMATCH","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"73D3A0FAD551855816817F11A42D5B0014172CB19E645F9AE2D473A58438CD59","Bytes":5771},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},{"Id":"MU-B05","Mode":"binding","ExpectedAssertion":"D-MISMATCH-AGGREGATE_SHA256","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"9F1E2087EA471904969BF58ADF34C4F129ACC038D5D8F971F3326C9F2A941183","Bytes":5765},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},{"Id":"MU-B06","Mode":"binding","ExpectedAssertion":"D-MISMATCH-ENTRY_COUNT","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"E38808C8846B503EC9E7EA2D9C806DDF6DB7DEEEAF8765AF4612A141C4874D0A","Bytes":5775},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},{"Id":"MU-B07","Mode":"binding","ExpectedAssertion":"D-MISMATCH-BYTE_TOTAL","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"D2547E6CBA6574643CAB94FFE8662AF45AF975A297D9D94173617BD1B00E589D","Bytes":5776},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},{"Id":"MU-B08","Mode":"binding","ExpectedAssertion":"P-ONE.QUALIFIER","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"5B3351956372A90A10A86A4EEC8D47C37595DE8289C6105CAF954F45B9C6BA88","Bytes":5776},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}}]' | ConvertFrom-Json
$protectedInputs = '[{"Path":"validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_CANDIDATE_REV1.py","SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},{"Path":"validation/route_b_c03/wp_008/RDM_CANON2_STRUCTURAL_LAYOUT_CANDIDATE_REV1.py","SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},{"Path":"validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_CANDIDATE_REV1.py","SHA256":"32535D3E4800E39E8AAF510166AD2AF04E0436D39E7C0BAD528B329D24E66821","Bytes":5799},{"Path":"validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_VALIDATION_REV1.py","SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142},{"Path":"validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_LOCAL_RUN_REV1.ps1","SHA256":"20AD3881CB7EAD15930290537AE1921B617909F51D950CC21704C6695D2612E2","Bytes":10172},{"Path":"docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_CANON2_DETACHED_PROJECTION_BINDING_PLAN_REV1.md","SHA256":"BC93B49AF201F8E33D04CC477BA7CEA7EF5376CF55F71930B04C984680FE3939","Bytes":6803},{"Path":"validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_REV1_OBSERVED_RESULT.json","SHA256":"5F3755FC6CB37BE210710FC8CB0287ABB0EDDAC6CEF550F9A7F557081701B63C","Bytes":10762},{"Path":"docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_CANON2_DETACHED_PROJECTION_BINDING_RESULT_REV1.md","SHA256":"CF972802BF1E75C5EFF32AAD04C9DB46F860FD3CE27086562B022655475BF6A4","Bytes":9331},{"Path":"validation/route_b_c03/wp_008/RDM_CANON2_PREDECLARED_MUTATION_SENSITIVITY_REV1.ps1","SHA256":"70B28D732BCB5FF1B34673E6A23835469FF981D2A15AB719A6960D9A3C225140","Bytes":24249}]' | ConvertFrom-Json
function Digest([byte[]]$Bytes) { [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($Bytes)) }
function Zip([byte[]]$Bytes) {
  $output = [IO.MemoryStream]::new()
  $gzip = [IO.Compression.GZipStream]::new($output, [IO.Compression.CompressionMode]::Compress, $true)
  try { $gzip.Write($Bytes, 0, $Bytes.Length) } finally { $gzip.Dispose() }
  $result = $output.ToArray(); $output.Dispose()
  return ,$result
}
function Assert-ProtectedInputs {
  foreach ($p in $protectedInputs) {
    $b = [IO.File]::ReadAllBytes($root + $p.Path)
    if ($b.Length -ne $p.Bytes -or (Digest $b) -cne $p.SHA256) { throw 'PROTECTED_INPUT_CHANGED' }
  }
}
Assert-ProtectedInputs
$originals = @{}
foreach ($s in $sources) {
  $bytes = [IO.File]::ReadAllBytes($root + $s.Path)
  if ($bytes.Length -ne $s.Bytes -or (Digest $bytes) -cne $s.SHA256) { throw 'FIXED_SOURCE_IDENTITY' }
  $null = $utf8.GetString($bytes)
  $originals[$s.Role] = $bytes
}
if ((Digest ([IO.File]::ReadAllBytes($executable))) -cne $executableSha) { throw 'PYTHON_EXECUTABLE_IDENTITY' }
$mutants = @{}
$snapshots = [Collections.Generic.List[object]]::new()
foreach ($d in $definitions) {
  $original = $originals[$d.TargetRole]
  $text = $utf8.GetString($original)
  $matches = ([regex]::Matches($text, [regex]::Escape($d.Before))).Count
  if ($matches -ne 1) { throw 'MUTATION_SITE_NOT_UNIQUE' }
  $bytes = $utf8.GetBytes($text.Replace($d.Before, $d.After))
  if ($bytes.Length -ne $d.MutatedBytes -or (Digest $bytes) -cne $d.MutatedSHA256) { throw 'MUTANT_IDENTITY' }
  $mutants[$d.Id] = $bytes
  $zipBytes = Zip $bytes
  $snapshots.Add([ordered]@{Id=$d.Id;TargetRole=$d.TargetRole;OriginalSHA256=(Digest $original);PatchMatches=$matches;Before=$d.Before;After=$d.After;ExpectedAssertion=$d.ExpectedAssertion;UTF8Bytes=$bytes.Length;SHA256=(Digest $bytes);GZipBytes=$zipBytes.Length;GZipBase64=[Convert]::ToBase64String($zipBytes);Qualification='IN-MEMORY SINGLE-FAULT TEST FIXTURE ONLY; NO PHYSICAL SOURCE MODIFIED'})
}
$bootstrap = @'
import ast, base64, hashlib, json, re, sys, types
sys.stdout.reconfigure(encoding="utf-8", errors="strict", newline="\n")
CASES = json.loads(r'''{"BASE-BINDING":{"Id":"BASE-BINDING","Mode":"binding","ExpectedAssertion":null,"Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"32535D3E4800E39E8AAF510166AD2AF04E0436D39E7C0BAD528B329D24E66821","Bytes":5799},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},"MU-B01":{"Id":"MU-B01","Mode":"binding","ExpectedAssertion":"L-LABEL-STALE-FULL-SHA","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"11EBD7A12AF07BEAA4EDD8245EE13100629BEACA8302B41E06C67B7CB8EFB973","Bytes":5764},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},"MU-B02":{"Id":"MU-B02","Mode":"binding","ExpectedAssertion":"B-AGGREGATE-MISMATCH","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"03CD28E0F619ED747DEFBCCF2264461B1D668E10E5D2AEA38809CFD0E115358B","Bytes":5770},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},"MU-B03":{"Id":"MU-B03","Mode":"binding","ExpectedAssertion":"B-COUNT-MISMATCH","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"EC5113EE8477E692805F5BCB0E59750D322A4FD7D4719655E4165B72FEE86886","Bytes":5770},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},"MU-B04":{"Id":"MU-B04","Mode":"binding","ExpectedAssertion":"B-TOTAL-MISMATCH","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"73D3A0FAD551855816817F11A42D5B0014172CB19E645F9AE2D473A58438CD59","Bytes":5771},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},"MU-B05":{"Id":"MU-B05","Mode":"binding","ExpectedAssertion":"D-MISMATCH-AGGREGATE_SHA256","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"9F1E2087EA471904969BF58ADF34C4F129ACC038D5D8F971F3326C9F2A941183","Bytes":5765},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},"MU-B06":{"Id":"MU-B06","Mode":"binding","ExpectedAssertion":"D-MISMATCH-ENTRY_COUNT","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"E38808C8846B503EC9E7EA2D9C806DDF6DB7DEEEAF8765AF4612A141C4874D0A","Bytes":5775},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},"MU-B07":{"Id":"MU-B07","Mode":"binding","ExpectedAssertion":"D-MISMATCH-BYTE_TOTAL","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"D2547E6CBA6574643CAB94FFE8662AF45AF975A297D9D94173617BD1B00E589D","Bytes":5776},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}},"MU-B08":{"Id":"MU-B08","Mode":"binding","ExpectedAssertion":"P-ONE.QUALIFIER","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"binding":{"SHA256":"5B3351956372A90A10A86A4EEC8D47C37595DE8289C6105CAF954F45B9C6BA88","Bytes":5776},"validation":{"SHA256":"944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476","Bytes":13142}}}}''')
phase = "STARTUP"
names = {"scalar": "rdm_canon2_scalar_fixed_dependency_rev1", "tree": "rdm_canon2_tree_fixed_dependency_rev1"}
owned = {}
cleanup = {}
record = {"RunOutcome": "UNEXPECTED_OR_INVALID", "ValidatorResult": None, "SubjectValidationPassed": False, "ObservedSources": []}
case = None
try:
    if not (sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode):
        raise RuntimeError("STARTUP_FLAGS")
    phase = "CLOSED_CASE_INPUT"
    payload = json.loads(sys.stdin.buffer.read().decode("utf-8", "strict"))
    if set(payload) != {"CaseId", "Sources"} or payload["CaseId"] not in CASES:
        raise RuntimeError("CASE_INPUT")
    case = CASES[payload["CaseId"]]
    record["CaseId"] = case["Id"]
    record["ExpectedAssertion"] = case["ExpectedAssertion"]
    if set(payload["Sources"]) != set(case["Sources"]) or any(name in sys.modules for name in names.values()):
        raise RuntimeError("SOURCE_MEMBERS_OR_SLOT")
    loaded = {}
    for role, identity in case["Sources"].items():
        field = payload["Sources"][role]
        if set(field) != {"Base64"}:
            raise RuntimeError("SOURCE_FIELD")
        snapshot = base64.b64decode(field["Base64"], validate=True)
        digest = hashlib.sha256(snapshot).hexdigest().upper()
        if len(snapshot) != identity["Bytes"] or digest != identity["SHA256"]:
            raise RuntimeError("SOURCE_IDENTITY")
        record["ObservedSources"].append({"Role": role, "SHA256": digest, "Bytes": len(snapshot)})
        text = snapshot.decode("utf-8", "strict")
        phase = "STATIC_PARSE_" + role.upper()
        ast.parse(text, filename="<fixed-memory-case-" + role + ">")
        if role in names:
            module = types.ModuleType(names[role])
            namespace = module.__dict__
        else:
            namespace = {"__name__": "rdm_binding_mutation_private_" + role}
        phase = "LOCAL_LOAD_" + role.upper()
        exec(compile(snapshot, "<fixed-memory-case-" + role + ">", "exec", dont_inherit=True, optimize=0), namespace)
        loaded[role] = namespace
        if role in names:
            name = names[role]
            if name in sys.modules:
                raise RuntimeError("DEPENDENCY_SLOT_CHANGED")
            sys.modules[name] = module
            owned[name] = module
    phase = "RUN_CLOSED_VALIDATOR"
    result = loaded["validation"]["run_synthetic_checks"](loaded["binding"])
    record["ValidatorResult"] = result
    record["SubjectValidationPassed"] = True
    if case["ExpectedAssertion"] is None:
        if result["Summary"]["CheckCount"] != 106 or result["Summary"]["VectorCount"] != 3 or result["Summary"]["AllChecksPassed"] is not True:
            raise RuntimeError("BASELINE_COUNTS_OR_OUTCOME")
        record["RunOutcome"] = "BASELINE_VALIDATOR_PASS"
    else:
        record["RunOutcome"] = "MUTANT_SURVIVED"
except BaseException as error:
    record["FailurePhase"] = phase
    record["FailureType"] = type(error).__name__
    identifier = error.args[0] if type(error) is AssertionError and len(error.args) == 1 and type(error.args[0]) is str else None
    if identifier is not None and re.fullmatch(r"[A-Z0-9_.-]{1,100}", identifier):
        record["FailureAssertion"] = identifier
    if case is not None and case["ExpectedAssertion"] is not None and phase == "RUN_CLOSED_VALIDATOR" and type(error) is AssertionError and identifier == case["ExpectedAssertion"]:
        record["RunOutcome"] = "EXPECTED_ASSERTION_OBSERVED"
finally:
    for role, name in reversed(tuple(names.items())):
        if name not in owned:
            cleanup[role] = "NOT_REGISTERED"
        elif sys.modules.get(name) is owned[name]:
            del sys.modules[name]
            cleanup[role] = "OWNED_ENTRY_REMOVED"
        else:
            cleanup[role] = "OWNERSHIP_LOST_NOT_REMOVED"
record["DependencyCleanupState"] = cleanup
record["Runtime"] = {"Version": sys.version.split()[0], "Isolated": sys.flags.isolated, "NoSite": sys.flags.no_site, "DontWriteBytecode": sys.flags.dont_write_bytecode}
ok = record["RunOutcome"] in ("BASELINE_VALIDATOR_PASS", "EXPECTED_ASSERTION_OBSERVED") and all(state == "OWNED_ENTRY_REMOVED" for state in cleanup.values())
print(json.dumps(record, ensure_ascii=False, indent=2, allow_nan=False))
sys.exit(0 if ok else 1)
'@
function Invoke-ClosedProcess([object]$payload) {
  $start = [Diagnostics.ProcessStartInfo]::new($executable)
  $start.UseShellExecute = $false
  $start.CreateNoWindow = $true
  $start.RedirectStandardInput = $true
  $start.RedirectStandardOutput = $true
  $start.RedirectStandardError = $true
  $start.WorkingDirectory = $root
  $start.Environment.Clear()
  $systemDirectory = [Environment]::GetFolderPath([Environment+SpecialFolder]::Windows)
  $start.Environment['SystemRoot'] = $systemDirectory
  $start.Environment['WINDIR'] = $systemDirectory
  $start.Environment['PYTHONIOENCODING'] = 'utf-8'
  foreach ($arg in @('-I', '-S', '-B', '-c', $bootstrap)) { $start.ArgumentList.Add($arg) }
  $process = [Diagnostics.Process]::new()
  $process.StartInfo = $start
  $outBytes = [IO.MemoryStream]::new()
  $errBytes = [IO.MemoryStream]::new()
  $timer = [Diagnostics.Stopwatch]::StartNew()
  $timedOut = $false
  $started = $false
  try {
    if (-not $process.Start()) { throw 'LOCAL_PROCESS_START' }
    $started = $true
    $outTask = $process.StandardOutput.BaseStream.CopyToAsync($outBytes)
    $errTask = $process.StandardError.BaseStream.CopyToAsync($errBytes)
    $inputBytes = $utf8.GetBytes(($payload | ConvertTo-Json -Depth 5 -Compress))
    $writeTask = $process.StandardInput.BaseStream.WriteAsync($inputBytes, 0, $inputBytes.Length)
    if (-not $writeTask.Wait(5000)) { throw 'LOCAL_INPUT_WAIT' }
    $null = $writeTask.GetAwaiter().GetResult()
    $process.StandardInput.Close()
    if (-not $process.WaitForExit(30000)) {
      $timedOut = $true
      $process.Kill($true)
      if (-not $process.WaitForExit(5000)) { throw 'LOCAL_STOP_NOT_OBSERVED' }
    }
    if (-not [Threading.Tasks.Task]::WaitAll([Threading.Tasks.Task[]]@($outTask, $errTask), 5000)) { throw 'LOCAL_STREAM_WAIT' }
    $null = $outTask.GetAwaiter().GetResult()
    $null = $errTask.GetAwaiter().GetResult()
    $raw = $outBytes.ToArray()
    $stderr = $errBytes.ToArray()
    $exitCode = $process.ExitCode
    $elapsed = $timer.ElapsedMilliseconds
  } finally {
    if ($started -and -not $process.HasExited) { $process.Kill($true); $null = $process.WaitForExit(5000) }
    $process.Dispose()
    $outBytes.Dispose()
    $errBytes.Dispose()
  }
  return [pscustomobject]@{Raw=$raw;Stderr=$stderr;ExitCode=$exitCode;ElapsedMilliseconds=$elapsed;TimedOut=$timedOut}
}
$batchTimer = [Diagnostics.Stopwatch]::StartNew()
$runs = [Collections.Generic.List[object]]::new()
$batchError = $null
$baselinePasses = 0
$mutantsDetected = 0
foreach ($case in $cases) {
  try {
    if ($batchTimer.ElapsedMilliseconds -ge 60000) { throw 'LOGICAL_BATCH_DEADLINE' }
    $caseSources = [ordered]@{}
    foreach ($p in $case.Sources.PSObject.Properties) {
      $bytes = if ($mutants.ContainsKey($case.Id) -and $p.Name -ceq ($definitions | Where-Object Id -CEQ $case.Id).TargetRole) { $mutants[$case.Id] } else { $originals[$p.Name] }
      if ($bytes.Length -ne $p.Value.Bytes -or (Digest $bytes) -cne $p.Value.SHA256) { throw 'CASE_SOURCE_SNAPSHOT' }
      $caseSources[$p.Name] = @{Base64=[Convert]::ToBase64String($bytes)}
    }
    $capture = Invoke-ClosedProcess ([ordered]@{CaseId=$case.Id;Sources=$caseSources})
    $raw = $capture.Raw; $stderr = $capture.Stderr
    $parseFailure = $null; $record = $null
    try {
      if ($raw.Length -gt 262144 -or $stderr.Length -ne 0 -or $capture.TimedOut) { throw 'CASE_CAPTURE_BOUNDARY' }
      $record = ConvertFrom-Json -InputObject ($utf8.GetString($raw)) -Depth 40
    } catch { $parseFailure = $_.Exception.GetType().Name }
    $rawZip = Zip $raw; $errZip = Zip $stderr
    $isBaseline = $null -eq $case.ExpectedAssertion
    $expectedOutcome = if ($isBaseline) { 'BASELINE_VALIDATOR_PASS' } else { 'EXPECTED_ASSERTION_OBSERVED' }
    $expectedCleanup = $record.DependencyCleanupState.scalar -ceq 'OWNED_ENTRY_REMOVED' -and $record.DependencyCleanupState.tree -ceq 'OWNED_ENTRY_REMOVED'
    $satisfied = $null -ne $record -and $capture.ExitCode -eq 0 -and $null -eq $parseFailure -and $record.CaseId -ceq $case.Id -and $record.RunOutcome -ceq $expectedOutcome -and $expectedCleanup
    if (-not $isBaseline) { $satisfied = $satisfied -and $record.SubjectValidationPassed -eq $false -and $record.FailureType -ceq 'AssertionError' -and $record.FailurePhase -ceq 'RUN_CLOSED_VALIDATOR' -and $record.FailureAssertion -ceq $case.ExpectedAssertion }
    $runs.Add([ordered]@{CaseId=$case.Id;Mode=$case.Mode;ExpectedAssertion=$case.ExpectedAssertion;ExpectedRunOutcome=$expectedOutcome;EvaluationSatisfied=$satisfied;ObservedExitCode=$capture.ExitCode;ObservedElapsedMilliseconds=$capture.ElapsedMilliseconds;WaitTimedOut=$capture.TimedOut;StrictUTF8OrJsonFailureType=$parseFailure;RawStdoutBytes=$raw.Length;RawStdoutSHA256=(Digest $raw);RawStdoutGZipBytes=$rawZip.Length;RawStdoutGZipBase64=[Convert]::ToBase64String($rawZip);RawStderrBytes=$stderr.Length;RawStderrSHA256=(Digest $stderr);RawStderrGZipBytes=$errZip.Length;RawStderrGZipBase64=[Convert]::ToBase64String($errZip);Record=$record})
    if (-not $satisfied) { throw 'CASE_EXPECTATION_NOT_MET' }
    if ($isBaseline) { $baselinePasses++ } else { $mutantsDetected++ }
    if ($batchTimer.ElapsedMilliseconds -ge 60000) { throw 'LOGICAL_BATCH_DEADLINE' }
  } catch { $batchError = [ordered]@{CaseId=$case.Id;Type=$_.Exception.GetType().Name;Code='BATCH_STOPPED_NO_AUTOMATIC_RETRY'}; break }
}
foreach ($s in $sources) {
  $after = [IO.File]::ReadAllBytes($root + $s.Path)
  if ($after.Length -ne $s.Bytes -or (Digest $after) -cne $s.SHA256) { throw 'ORIGINAL_SOURCE_CHANGED' }
}
Assert-ProtectedInputs
$complete = $null -eq $batchError -and $runs.Count -eq 9 -and $baselinePasses -eq 1 -and $mutantsDetected -eq 8
$summary = [ordered]@{Outcome=if($complete){'LOCAL_PREDECLARED_BINDING_MUTATION_SENSITIVITY_PASS'}else{'LOCAL_BINDING_MUTATION_SENSITIVITY_INCOMPLETE'};BaselineRuns=$baselinePasses;PredeclaredMutants=8;MutantsDetectedAtExpectedAssertions=$mutantsDetected;ObservedProcesses=$runs.Count;OriginalBoundSourceModifications=0;FormalManifestGenerated=$false;SourceAdmission=$false;GeneralizedMutationScore='NOT CLAIMED';DSP004='OPEN / HOLD';B01='OPEN';B02='OPEN'}
$fullRecord = [ordered]@{Summary=$summary;FixedSources=$sources;ProtectedInputs=$protectedInputs;CaseSpecifications=$cases;MutatedMemorySnapshots=$snapshots;Runs=$runs;BatchError=$batchError;ObservedBatchElapsedMilliseconds=$batchTimer.ElapsedMilliseconds;BootstrapUTF8SHA256=(Digest ($utf8.GetBytes($bootstrap)));PythonExecutableSHA256=$executableSha;BudgetQualification='PER-PROCESS 5000/30000/5000 MS; LOGICAL BATCH 60000 MS; POST-CAPTURE OUTPUT CHECKS; NOT PHYSICAL STOP/MEMORY PROOF'}
$text = ($fullRecord | ConvertTo-Json -Depth 50).Replace("`r`n","`n").TrimEnd([char]10)+[char]10
$bytes = $utf8.GetBytes($text); $compressed = Zip $bytes
[ordered]@{ArchiveVersion='RDM-CANON2-BINDING-PREDECLARED-MUTATION-REV1-OBSERVED';FullRecordUTF8Bytes=$bytes.Length;FullRecordSHA256=(Digest $bytes);GZipBytes=$compressed.Length;GZipBase64=[Convert]::ToBase64String($compressed);Summary=$summary}|ConvertTo-Json -Depth 10
