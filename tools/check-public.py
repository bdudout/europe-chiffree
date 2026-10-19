#!/usr/bin/env python3
"""Validate the final static publication, without private research inputs."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re
root=Path(__file__).resolve().parents[1]/'dist'
assert not (root/'data').exists(), 'Research datasets must remain outside the public site'
assert not (root/'assets/img/glyphs').exists(), 'Intermediate glyph crops must remain local'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[];self.images=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  self.h1+=tag=='h1'
  if tag=='img':assert 'alt' in a;self.images.append(a['src'])
  for key in ['href','src']:
   if a.get(key):self.refs.append(a[key])
pages={}
for file in root.rglob('*.html'):
 p=Page();raw=file.read_text();p.feed(raw)
 assert len(p.ids)==len(set(p.ids)) and p.h1==1,file
 assert not re.search(r'/Users/|localhost:|https?://[^/]*\.chatgpt\.site|appgprj_|\{\{|<details|data-filter=',raw),file
 pages[file.resolve()]=p
assert len(pages)==19
refs=0
for file,page in pages.items():
 for ref in page.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  dest=(file.parent/unquote(u.path)).resolve() if u.path else file
  assert dest.is_relative_to(root.resolve()) and dest.exists(),(file,ref)
  if u.fragment and dest.suffix=='.html':assert unquote(u.fragment) in pages[dest].ids,(file,ref)
  refs+=1
for lang in ['fr','en','ja']:
 docs=(root/lang/'documents.html').read_text();sources=(root/lang/'sources.html').read_text()
 assert docs.count('class="line-scan"')==5 and docs.count('class="document-section"')==2
 nav=re.search(r'<nav class="nav".*?</nav>',docs).group()
 assert nav.index('methode.html')<nav.index('documents.html')
 assert 'data-language-select' in docs and 'Satoshi Tomokiyo' in sources and 'Daniel Bourdeau' in sources
 assert '../data/' not in sources
 article=(root/lang/'marie-de-medicis.html').read_text()
 method=(root/lang/'methode.html').read_text()
 assert 'id="synthese"' in article and 'Satoshi Tomokiyo' in article
 assert docs.count('class="corroborated"')==6, 'Six numerical occurrences must show their updated support'
 assert len(re.findall(r'\[(?:b|c|z|s|de)\?\]',docs))==8, 'Keep the eight unresolved readings visible'
 assert 'class="inferred"' not in docs, 'These four values are no longer supported solely by context'
 assert all(code+'~' in method for code in ['72','79','86','90'])
 assert all(x in sources for x in ['QUE','RE','SE','TION'])
 assert 'Dear Mr Dudout' not in sources and 'Best wishes' not in sources
print(json.dumps({'pages':len(pages),'languages':3,'localReferences':refs,'publication':'final pages and images only'}))
