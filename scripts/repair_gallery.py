"""Paired repair photographs with accessible project navigation; photos remain unaltered."""
from html import escape

CONTENT = {
 'en': {
  'eyebrow':'THE WORK, UP CLOSE', 'title':'EVERY REPAIR<br>HAS A <em>STORY.</em>',
  'intro':'From the damage that brought it in to the finish that takes it home. Explore two repairs from our shop.',
  'tabs':'Choose a repair story', 'case':'REPAIR STORY', 'before':'Before', 'after':'After', 'both':'Side by side',
  'view':'Choose a photo view', 'expand':'View full photo', 'close':'Close photo viewer',
  'arrival':'HOW IT ARRIVED', 'return':'HOW IT LEFT', 'hint':'Choose a vehicle. Open either photo for a closer look.',
  'more':'More from the shop on Instagram', 'your_car':'Let’s talk about your car',
  'previous':'Previous photo', 'next':'Next photo',
  'projects':[
   {'id':'mustang','name':'Ford Mustang','tag':'Front-end repair','note':'A closer look at the front-end transformation.','before_caption':'Hood and front-end damage','after_caption':'The finished Mustang','before_alt':'Red Ford Mustang before repair, with a crumpled hood and damaged front bumper','after_alt':'Red Ford Mustang after repair, photographed from the front corner outside the shop','before_size':(1122,2048),'after_size':(1206,1745)},
   {'id':'bronco','name':'Ford Bronco','tag':'Side-body repair','note':'From damaged side panels to a clean exterior.','before_caption':'Damage along the driver’s side','after_caption':'The finished Bronco','before_alt':'Black Ford Bronco before repair, showing damage along the driver-side door and lower body','after_alt':'Black Ford Bronco after repair, photographed outside the shop','before_size':(1206,1819),'after_size':(1206,1669)}
  ]
 },
 'es': {
  'eyebrow':'EL TRABAJO, DE CERCA','title':'CADA REPARACIÓN<br>TIENE SU <em>HISTORIA.</em>',
  'intro':'Desde los daños con los que llegó hasta el acabado con el que se va. Conozca dos reparaciones de nuestro taller.',
  'tabs':'Elija una reparación','case':'HISTORIA DE REPARACIÓN','before':'Antes','after':'Después','both':'Lado a lado',
  'view':'Elija una vista','expand':'Ver foto completa','close':'Cerrar visor de fotos',
  'arrival':'ASÍ LLEGÓ','return':'ASÍ SALIÓ','hint':'Elija un vehículo. Abra cualquiera de las fotos para verla de cerca.',
  'more':'Más del taller en Instagram','your_car':'Hablemos de su vehículo',
  'previous':'Foto anterior','next':'Foto siguiente',
  'projects':[
   {'id':'mustang','name':'Ford Mustang','tag':'Reparación frontal','note':'Vea de cerca la transformación de la parte delantera.','before_caption':'Daños en el capó y la parte delantera','after_caption':'El Mustang terminado','before_alt':'Ford Mustang rojo antes de la reparación, con el capó deformado y el parachoques delantero dañado','after_alt':'Ford Mustang rojo después de la reparación, fotografiado de frente y de lado fuera del taller','before_size':(1122,2048),'after_size':(1206,1745)},
   {'id':'bronco','name':'Ford Bronco','tag':'Reparación lateral','note':'De los paneles laterales dañados a un exterior reparado.','before_caption':'Daños en el lado del conductor','after_caption':'El Bronco terminado','before_alt':'Ford Bronco negro antes de la reparación, con daños en la puerta del conductor y la parte inferior de la carrocería','after_alt':'Ford Bronco negro después de la reparación, fotografiado fuera del taller','before_size':(1206,1819),'after_size':(1206,1669)}
  ]
 }
}

def gallery(d):
 c=CONTENT[d['lang']]
 h=f'''<section class="repair-stories section" id="work" aria-labelledby="repair-title"><div class="container"><div class="repair-heading"><div><p class="eyebrow dark"><span class="red-line"></span>{c['eyebrow']}</p><h2 id="repair-title">{c['title']}</h2></div><div class="repair-heading-copy"><p>{c['intro']}</p><span class="repair-hint">{c['hint']}</span></div></div><div class="repair-tabs" role="tablist" aria-label="{c['tabs']}" hidden>'''
 for n,p in enumerate(c['projects']):
  h+=f'''<button type="button" role="tab" id="tab-{p['id']}" aria-controls="story-{p['id']}" aria-selected="{'true' if n==0 else 'false'}" tabindex="{0 if n==0 else -1}" data-story-tab="{p['id']}"><span class="tab-thumb"><img src="/assets/repairs/{p['id']}-after.jpg" alt="" width="70" height="60" loading="lazy"></span><span><b>{p['name']}</b><small>{p['tag']}</small></span><span class="tab-index" aria-hidden="true">0{n+1}</span></button>'''
 h+='</div><div class="repair-deck">'
 for n,p in enumerate(c['projects']):
  h+=f'''<article class="repair-story" id="story-{p['id']}" aria-label="{p['name']}" data-story="{p['id']}" data-view="both"><div class="story-header"><div><span class="story-kicker">{c['case']} / 0{n+1}</span><h3>{p['name']}<span>{p['tag']}</span></h3></div><div class="view-switch" role="group" aria-label="{c['view']}" hidden>'''
  for mode in ['both','before','after']:
   h+=f'<button type="button" data-view-button="{mode}" aria-pressed="{str(mode=="both").lower()}">{c[mode]}</button>'
  h+='</div></div><div class="photo-pair">'
  for state in ['before','after']:
   w,height=p[state+'_size']; src=f'/assets/repairs/{p["id"]}-{state}.jpg'
   h+=f'''<figure class="repair-photo {state}" data-photo-state="{state}"><div class="photo-stage"><span>{c['arrival' if state=='before' else 'return']}</span><b>{c[state]}</b></div><a class="photo-open" href="{src}" data-photo-open data-caption="{escape(p['name']+' — '+c[state],quote=True)}" aria-label="{c['expand']}: {p['name']}, {c[state]}"><img src="{src}" alt="{p[state+'_alt']}" width="{w}" height="{height}" loading="lazy" decoding="async"><span class="photo-zoom"><span aria-hidden="true">＋</span> {c['expand']}</span></a><figcaption><span class="caption-dot" aria-hidden="true"></span>{p[state+'_caption']}</figcaption></figure>'''
  h+=f'''</div><div class="story-footer"><p>{p['note']}</p><a class="text-link" href="{d['home']}#estimate">{c['your_car']}</a></div></article>'''
 h+=f'''</div><div class="repair-more"><span>@somicoachworks</span><a href="https://www.instagram.com/somicoachworks/" target="_blank" rel="noopener noreferrer">{c['more']} <span aria-hidden="true">↗</span></a></div></div></section><dialog class="photo-lightbox" id="repair-lightbox" aria-labelledby="lightbox-title"><div class="lightbox-bar"><h2 id="lightbox-title"></h2><button class="dialog-close" type="button" aria-label="{c['close']}">×</button></div><img id="lightbox-image" alt=""><div class="lightbox-controls"><button type="button" id="lightbox-prev">← {c['previous']}</button><span id="lightbox-count" aria-live="polite"></span><button type="button" id="lightbox-next">{c['next']} →</button></div></dialog>'''
 return h
