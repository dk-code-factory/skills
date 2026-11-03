#!/usr/bin/env python3
"""Organization catalogs contain independent released-main plugin sources only."""
import json
from pathlib import Path
root=Path(__file__).resolve().parent.parent
expected=['dk-workflows','dk-architecture','code-review-ad','code-review-matpocock','code-review-qodo']
for filename,kind in [('.agents/plugins/marketplace.json','url'),('.claude-plugin/marketplace.json','github')]:
    data=json.loads((root/filename).read_text())
    assert data['name']=='dk-code-factory'
    assert [e['name'] for e in data['plugins']]==expected
    for e in data['plugins']:
        source=e['source'];assert source['source']==kind and source['ref']=='main'
        assert source.get('repo',source.get('url')) in ('dk-code-factory/'+e['name'],'https://github.com/dk-code-factory/'+e['name']+'.git')
assert not (root/'.codex-plugin/plugin.json').exists() and not (root/'runtime').exists()
print('Both organization catalogs are valid; no runtime dependencies.')
