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
assert len(pages)==28
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
 assert docs.count('class="line-scan"')==5 and len(re.findall(r'class="document-section[ "]',docs))>=8
 nav=re.search(r'<nav class="nav".*?</nav>',docs).group()
 assert 'marie-de-medicis.html' in re.search(r'<div class="nav-sub".*?</div>',nav).group() and 'documents.html' in nav and 'methode.html' in nav
 assert 'data-language-select' in docs and 'Satoshi Tomokiyo' in sources and 'Daniel Bourdeau' in sources
 assert '../data/' not in sources
 article=(root/lang/'marie-de-medicis.html').read_text()
 method=(root/lang/'methode.html').read_text()
 assert 'id="synthese"' in article and 'Satoshi Tomokiyo' in article
 lines=''.join(re.findall(r'<section class="source-passage" id="(?:septembre|novembre)-l\d">.*?</section>',docs,re.S));assert lines.count('class="corroborated"')==6, 'Six numerical occurrences must show their updated support'
 assert len(re.findall(r'\[(?:b|c|z|s|de)\?\]',lines))==4, 'Keep the four unresolved September readings visible (November confirmed by G. Lasry, Oct. 2026)'
 assert 'class="inferred"' not in docs, 'These four values are no longer supported solely by context'
 assert all(code+'~' in method for code in ['72','79','86','90'])
 assert all(x in sources for x in ['QUE','RE','SE','TION'])
 assert 'id="ferducci-1532"' in docs and 'Daniel Bourdeau' in docs and 'Türkei I 2-2-19' in docs and 'solve/498' in docs and 'id="s13"' in sources
 assert 'id="stade-1710"' in docs and 'Rep. 5a Nr. 670' in docs and 'solve/599' in docs and 'Public Domain Mark' in docs and 'id="s16"' in sources and 'Riksarkivet' in docs
 assert 'archivinformationssystem.at/getimage' not in docs, 'No ÖStA image may be republished'
 assert 'id="hoeg-1675"' in docs and 'solve/465' in docs and 'kopibog' in docs and 'epid=15553654' in docs and 'id="s465a"' in sources, 'Høeg 1675 card with credits'
 assert 'id="meyercrone-1675"' in docs and 'id="meyercrone-texte"' in docs and 'id="s465c"' in sources, 'Meyercrone 1675 sister record'
 assert 'id="mornay-1593"' in docs and 'solve/371' in docs and 'Daniel Bourdeau' in docs and 'mmoiresetcorre05morn' in docs and 'id="s371"' in sources, 'Duplessis-Mornay 1593 card with credits'
 assert 'id="vilaflor-1663"' in docs and 'solve/391' in docs and 'PT/TT/LMP/0002' in docs and 'Daniel Bourdeau' in docs and 'id="s391a"' in sources and 'id="s391b"' in sources, 'Vila Flor 1663 card with credits'
 assert 'rdigital/dissemination' not in docs, 'No ANTT/DigitArq image may be republished'
 assert 'api.rigsarkivet.dk' not in docs, 'No Rigsarkivet image may be republished'
 assert 'id="dana-1783"' in docs and 'solve/485' in docs and 'Daniel Bourdeau' in docs and 'PCC 89' in docs and 'id="s485a"' in sources and 'id="s485b"' in sources, 'Dana 1783 card with credits'
 assert 'id="everett-1825"' in docs and 'solve/638' in docs and 'Daniel Bourdeau' in docs and 'targets/jqa' in docs and 'M31-027-0119' in docs and 'id="everett-pages"' in docs and 'M31-027-0114' in docs and 'id="s638a"' in sources and 'id="s638b"' in sources, 'Everett 1825 card with credits'
 assert 'id="krakow-1663"' in docs and 'solve/439' in docs and 'Daniel Bourdeau' in docs and 'AKPot 3227' in docs and 'id="s439a"' in sources and 'id="s439b"' in sources, 'Krakow 1663 card with credits'
 assert 'krakow-1662' not in docs and 'de-crypt.org/decrypt-web/Image' not in docs and 'assets/img/krakow' not in docs, 'No DECODE image may be republished'
 assert 'id="huyson-1547"' in docs and 'solve/500' in docs and 'Daniel Bourdeau' in docs and 'Türkei I 7-2-18' in docs and 'ID=6567149' in docs and 'id="s500a"' in sources and 'id="s500b"' in sources and 'id="s500c"' in sources, 'Huyson 1547 card with credits'
 assert 'id="nisa-1644"' in docs and 'joao1642.html' in docs and 'Daniel Bourdeau' in docs and 'MSLIV/1017' in docs and 'id="s380a"' in sources and 'id="s380b"' in sources, 'Nisa 1644 card with credits'
 assert 'Dear Mr Dudout' not in sources and 'Best wishes' not in sources
print(json.dumps({'pages':len(pages),'languages':3,'localReferences':refs,'publication':'final pages and images only'}))
