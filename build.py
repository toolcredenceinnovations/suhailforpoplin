import json,re,pathlib
root=pathlib.Path(__file__).parent
order=json.loads((root/'deck/deck.json').read_text())['order']
slides=[]
for sid in order:
    h=(root/f'deck/slides/{sid}.html').read_text()
    h=h.replace('/_blob/6fce1a3fc9597ad62fd5057ba5ca61fe','assets/minneapolis_map.png')
    h=re.sub(r'<x-embed[^>]*>(<style>.*?</style>)?','<div class="embed">',h,flags=re.S).replace('</x-embed>','</div>')
    h=re.sub(r'<x-shape[^>]*></x-shape>','<div style="position:absolute;left:50px;top:650px;width:1820px;height:1px;background:#E4E4E4"></div>',h)
    h=re.sub(r'<aside>.*?</aside>','',h,flags=re.S)
    h=re.sub(r' data-build-in="[^"]*"','',h)
    slides.append(h)
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Suhail for Poplin</title>
<style>html,body{margin:0;height:100%;background:#151515;overflow:hidden;font-family:Arial,sans-serif}
#stage{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0}
#stage section{position:absolute;left:0;top:0;width:1920px;height:1080px;box-sizing:border-box;overflow:hidden;opacity:0;pointer-events:none;transition:opacity .35s}
#stage section.on{opacity:1;pointer-events:auto}
#stage p,#stage h1,#stage h2{margin:0}#stage hr{margin:0;border-left:0;border-right:0;border-bottom:0;height:0}#stage *{box-sizing:content-box}
.embed{position:absolute;left:1000px;top:0;width:920px;height:1080px}
#nav{position:fixed;bottom:12px;left:50%;transform:translateX(-50%);display:flex;gap:10px;align-items:center;color:#ADADAD;font-size:14px;z-index:9}
#nav button{background:#404040;color:#fff;border:0;border-radius:5px;padding:6px 12px;cursor:pointer}</style></head><body>
<div id="stage">'''+'\n'.join(slides)+'''</div>
<div id="nav"><button id="p">Prev</button><span id="c"></span><button id="n">Next</button></div>
<script>
var s=[].slice.call(document.querySelectorAll('#stage section')),i=0,st=document.getElementById('stage');
function fit(){var k=Math.min(innerWidth/1920,innerHeight/1080);st.style.transform='scale('+k+')';st.style.left=(innerWidth-1920*k)/2+'px';st.style.top=(innerHeight-1080*k)/2+'px'}
function show(n){i=Math.max(0,Math.min(s.length-1,n));s.forEach(function(e,j){e.classList.toggle('on',j==i)});document.getElementById('c').textContent=(i+1)+' / '+s.length;location.hash=i+1}
addEventListener('resize',fit);addEventListener('keydown',function(e){if(['ArrowRight','ArrowDown',' ','PageDown'].indexOf(e.key)>-1)show(i+1);if(['ArrowLeft','ArrowUp','PageUp'].indexOf(e.key)>-1)show(i-1)});
document.getElementById('n').onclick=function(){show(i+1)};document.getElementById('p').onclick=function(){show(i-1)};
addEventListener('hashchange',function(){var n=(parseInt(location.hash.slice(1))||1)-1;if(n!=i)show(n)});fit();show((parseInt(location.hash.slice(1))||1)-1);
</script></body></html>'''
(root/'index.html').write_text(page)
