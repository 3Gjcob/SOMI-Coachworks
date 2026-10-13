"""Build the bilingual static site. Run from the repository root."""
from pathlib import Path
from html import escape
import json
from repair_gallery import gallery
from icons import icon, GOOGLE_G

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
ORIGIN = 'https://somicoachworks.jkalka28227.chatgpt.site'
IG = 'https://www.instagram.com/somicoachworks/'
MAP = 'https://www.google.com/maps/search/?api=1&query=South+Miami+Coach+Works+5780+SW+68th+St'
DIRECTIONS = 'https://www.google.com/maps/dir/?api=1&destination=South+Miami+Coach+Works+5780+SW+68th+St+South+Miami+FL+33143'
DFS = 'https://www.myfloridacfo.com/docs-sf/consumer-services-libraries/consumerservices-documents/understanding-coverage/consumer-guides/english---automobile-insurance-toolkit.pdf?sfvrsn=6b999793_9'

EN = {
 'lang':'en','home':'/','other':'/es/','other_label':'Español','title':'Auto Body & Collision Repair in South Miami',
 'description':'South Miami Coach Works: collision repair, paint, bodywork and free estimates at 5780 SW 68th St. Call (305) 397-8911. Se habla español.',
 'skip':'Skip to content','services':'Services','work':'Our work','about':'About us','reviews':'Reviews','visit':'Visit us','estimate':'Free estimate','privacy':'Privacy',
 'hero':'Collision &amp; Body Repair<br><span>in South Miami</span>',
 'hero_eyebrow':'SOUTH MIAMI COACH WORKS',
 'hero_copy':'Collision repair, bodywork and paint for all makes and models. Free estimates on every job.',
 'call':'Call (305) 397-8911','explore':'Explore services','spanish':'Se habla español','rating':'5.0 on Google · 14 reviews','rating_date':'Google rating shown from October 2026.',
 'trust':['Free estimates','All makes & models','Insurance claim help','Se habla español'],
 'services_title':'Our Services',
 'services_intro':'Tell us what happened. We’ll inspect the car and explain the work before you decide.',
 'learn':'Service details','not_sure':'Not sure which service you need?','ask':'Call and describe the damage.',
 'service_data':[
  ['collision-repair','Collision repair','After an accident, we assess the damaged areas and discuss the repair plan with you. Bring your claim information if you’re using insurance so we can help with the next steps.','Damage assessment · Repair planning · Insurance assistance',
   'An estimate starts with a look at the vehicle, not a promise based on one photograph. We’ll discuss the visible damage, which areas need a closer inspection, and what information your insurer may need.',
   'Bring the year, make and model, photos of the damaged areas, and your claim number if one has been assigned. Ask the team about parts availability and the expected schedule before arranging a drop-off.'],
  ['paint-refinishing','Paint & refinishing','We assess scratches, paint damage and panels that need refinishing. We’ll talk through the finish you’re looking for and the preparation your vehicle needs before providing an estimate.','Scratches · Panel refinishing · Paint assessment',
   'Paint repairs begin with assessing the affected finish and the condition of the panel underneath. Tell us whether you’re addressing accident damage, a scratch or a larger cosmetic project.',
   'The scope of preparation and refinishing depends on the condition of the vehicle. Ask us about the areas included in your estimate, the expected finish and aftercare before authorizing the work.'],
  ['body-dent-repair','Body & dent repair','Dents, scrapes and damaged panels need a closer look before a repair method is chosen. We’ll inspect the affected areas and explain the available bodywork options for your vehicle.','Dents · Scrapes · Body panels',
   'Parking damage, scrapes and dents can affect both the shape of a panel and its finish. We’ll look at the location, size and depth of the damage before discussing repair options.',
   'Photos are a useful starting point, but some damage needs an in-person inspection. Ask us which repairs and any associated paintwork are included in your written estimate.'],
  ['glass-detailing','Glass & finishing care','Ask us about automotive glass replacement, detailing and headlight restoration. We’ll confirm the right service for your vehicle and discuss any related work before you book.','Glass replacement · Detailing · Headlight restoration',
   'Tell us whether you need damaged glass assessed, headlights restored or detailing for your vehicle. We’ll confirm the service and scope when you contact the shop.',
   'For glass work, ask about any camera or sensor calibration your vehicle may require. Availability, the repair method and any specialist work need to be confirmed for your particular vehicle.']
 ],
 'work_title':'SEE WHAT’S<br>IN THE SHOP.',
 'work_copy':'Follow @somicoachworks for the photos and updates shared by our team. Explore the shop’s posts, then call us about your own repair.',
 'ig_cta':'View our work on Instagram','ig_label':'PHOTOS & SHOP UPDATES','ig_note':'Opens the shop’s Instagram profile.',
 'about_title':'About the Shop',
 'about_copy':'We’re South Miami Coach Works, also known as SOMI Coachworks. Our paint and body shop is on SW 68th Street, just off Red Road in South Miami.',
 'about_more':'Our team brings more than 20 years of experience to the work. Speak with us in English or Spanish about collision damage, bodywork or your next paint project.',
 'experience':'20+','experience_label':'years of experience','experience_note':'As shared on our shop’s Instagram profile.',
 'areas_title':'Areas we serve','areas':'Visit us from South Miami, Coral Gables, Pinecrest, Kendall, Westchester and nearby Miami neighborhoods.',
 'process_title':'How it works',
 'steps':[['Call for an estimate','Tell us about the vehicle and the damage, and we’ll set up an inspection.'],['Review the repair','We go over the work, your insurance claim and the schedule with you.'],['Drop off your car','Bring the vehicle in once the work and timing are confirmed.']],
 'reviews_title':'Customer Reviews', 'review_excerpt':'','read_reviews':'Read reviews on Google','leave_review':'Leave us a review','leave_note':'','review_label':'Google review',
 'estimate_title':'Get a Free Estimate',
 'estimate_copy':'Call the shop to set up a free estimate. Have the year, make and model ready, and tell us where the damage is.',
 'contact_title':'Call or email us','contact_text':'Talk to us about the repair and a time to bring the car in, or email your details and a few photos of the damage.',
 'email':'Email the shop','send_photos':'You can attach damage photos to your email.','estimate_note':'The shop confirms all appointments, repair pricing and availability.',
 'form_title':'Request an estimate','form_intro':'Tell us about the vehicle and add photos of the damage. The shop will confirm next steps; submitting does not reserve an appointment.',
 'name':'Your name','phone':'Phone number','email_label':'Email address','year':'Vehicle year','vehicle':'Make & model','service':'Service','select':'Select a service','other_service':'Something else / not sure','details':'Describe the damage','insurance':'Insurance company (optional)','photos':'Damage photos (optional)','photo_help':'Up to 5 JPG, PNG or WebP images, 5 MB each.','consent':'I agree that the shop may contact me about this request.','submit':'Send estimate request','form_privacy':'We use your contact details and photos to respond to this request.','form_error':'We couldn’t send your request. Your details are still here. Try again or call (305) 397-8911.','form_success':'Your request was submitted. The shop will confirm the next steps.','form_sending':'Sending…','form_invalid':'Please add up to 5 JPG, PNG or WebP images of 5 MB or less each.','form_phone_error':'Enter a valid phone number with area code.','form_photo_count':'photos selected','form_external':'Open secure estimate form',
 'visit_title':'Hours &amp; Location','directions':'Get directions','hours':'Shop hours','monday':'Monday','weekdays':'Tuesday – Friday','weekends':'Saturday – Sunday','closed':'Closed','hours_note':'Please call before visiting, especially on holidays.','hours_open':'Open now','hours_closed':'Closed now','maps':'Open in Google Maps',
 'faq_title':'Common Questions','faq_intro':'Have another question? Call us.',
 'faqs':[
  ['Are estimates free?','Yes. Call us at (305) 397-8911 to arrange an assessment. Have the vehicle’s year, make, model and a description of the damage ready.'],
  ['Can you help with my insurance claim?','Yes. We offer insurance claim assistance and work with claims from all insurance companies. Bring your insurer’s name and claim number; coverage, deductibles and payment are determined by your policy and insurer.'],
  ['Can I choose my repair shop?','Yes. Florida’s Department of Financial Services says you may select the shop that repairs your car after an accident. Discuss coverage, the estimate and any differences in cost with your insurer before authorizing work.'],
  ['Do you work on my make and model?','Yes. We work on all makes and models. Call us with your vehicle details so we can confirm the appropriate work, parts and any specialist services needed.'],
  ['What warranty applies to my repair?','Ask us for the written warranty terms for your specific repair before approving the work. We’ll discuss what is covered, how long coverage lasts and any exclusions.'],
  ['Can you help with towing or a rental?','Call us before arranging a tow so we can confirm where and when to bring the vehicle. Ask about current towing assistance and rental options; rental coverage depends on your insurance policy.'],
  ['How long will my repair take?','The timing depends on the damage, parts and the work required. We’ll discuss the expected schedule after assessing your vehicle. Call us directly for an update on an existing repair.']
 ],
 'consumer_guide':'Florida consumer guide','claims':'Insurance claims','back':'Back to home','top':'Back to top','footer_line':'5780 SW 68th St · South Miami, FL 33143','footer_areas':'Auto body and collision repair serving South Miami, Coral Gables, Pinecrest, Kendall and Westchester.','footer_cta':'Call about your repair',
 'privacy_title':'Your privacy','privacy_text':'When you call or email the shop, your contact details and any photos are used to respond to your repair inquiry. An online request form, when available, also shares those details with the form provider and the shop. Do not send payment details, identification documents or unnecessary personal information.','privacy_more':'Google Maps and Instagram have their own privacy policies. This site does not use advertising analytics. For questions about information sent to the shop, contact somicoachworks@gmail.com.',
 'photo_title':'Photography','photo_text':'The hero image is an automotive stock photograph from Unsplash. It is not presented as a SOMI customer project or the shop’s premises.','photo_link':'View photo source','close':'Close dialog',
 'claim_title':'Insurance Claim Assistance','claim_intro':'Bring your claim information. We’ll discuss the vehicle assessment and the next steps for the repair.',
 'claim_sections':[['What to have ready','Bring your vehicle details, insurer’s name, claim number and adjuster’s contact information if you have them. Keep copies of the estimate and any authorization you sign.'],['Your choice of shop','Florida consumer guidance says you can select your repair shop after an accident. Talk with your insurer about coverage and any difference between its estimate and the shop’s estimate before work begins.'],['Know what is approved','Confirm the work, deductible, payment arrangements and any additional authorization needed if more damage is found. The shop cannot guarantee insurance coverage or a rental reimbursement.']],
 'detail_next':'Ready to talk about your car?','detail_note':'An in-person assessment may be needed to confirm scope and pricing.'
}

ES = {
 'lang':'es','home':'/es/','other':'/','other_label':'English','title':'Reparación de carrocería y choques en South Miami',
 'description':'South Miami Coach Works: reparación de choques, carrocería, pintura y estimados gratis. 5780 SW 68th St. Llame al (305) 397-8911. Se habla español.',
 'skip':'Ir al contenido','services':'Servicios','work':'Trabajos','about':'Nosotros','reviews':'Reseñas','visit':'Visítenos','estimate':'Estimado gratis','privacy':'Privacidad',
 'hero':'Carrocería y choques<br><span>en South Miami</span>','hero_eyebrow':'SOUTH MIAMI COACH WORKS',
 'hero_copy':'Reparación de choques, carrocería y pintura para todas las marcas y modelos. Estimados gratis en todos los trabajos.',
 'call':'Llame al (305) 397-8911','explore':'Ver servicios','spanish':'Se habla español','rating':'5.0 en Google · 14 reseñas','rating_date':'Calificación de Google de octubre de 2026.',
 'trust':['Estimados gratis','Todas las marcas y modelos','Ayuda con reclamos','Se habla español'],
 'services_title':'Nuestros servicios','services_intro':'Cuéntenos qué pasó. Revisaremos el vehículo y le explicaremos el trabajo antes de que decida.',
 'learn':'Detalles del servicio','not_sure':'¿No sabe qué servicio necesita?','ask':'Llámenos y describa el daño.',
 'service_data':[
  ['collision-repair','Reparación de choques','Después de un accidente, evaluamos las zonas dañadas y hablamos con usted sobre el plan de reparación. Traiga la información del reclamo si usará su seguro para que podamos ayudarle con los próximos pasos.','Evaluación de daños · Plan de reparación · Ayuda con el seguro',
   'El estimado comienza con una revisión del vehículo. Hablaremos de los daños visibles, las zonas que necesitan una inspección más detallada y la información que podría pedir su aseguradora.',
   'Tenga a mano el año, la marca y el modelo, fotos de las zonas dañadas y el número del reclamo, si lo tiene. Pregunte por la disponibilidad de piezas y el plazo previsto antes de dejar el vehículo.'],
  ['paint-refinishing','Pintura y acabado','Evaluamos rayones, daños en la pintura y paneles que necesitan un nuevo acabado. Hablaremos del resultado que busca y la preparación que necesita su vehículo antes de darle un estimado.','Rayones · Pintura de paneles · Evaluación del acabado',
   'La reparación de pintura comienza con una evaluación del acabado y del panel. Díganos si se trata de daños por un choque, un rayón o un proyecto estético más amplio.',
   'La preparación y el trabajo de pintura dependen del estado del vehículo. Pregunte qué zonas incluye el estimado, qué resultado puede esperar y cómo cuidar la pintura antes de autorizar el trabajo.'],
  ['body-dent-repair','Carrocería y abolladuras','Las abolladuras, los roces y los paneles dañados necesitan una inspección antes de elegir el método de reparación. Revisamos las zonas afectadas y explicamos las opciones para su vehículo.','Abolladuras · Roces · Paneles de carrocería',
   'Los golpes de estacionamiento, los roces y las abolladuras pueden afectar tanto la forma del panel como la pintura. Evaluamos la ubicación, el tamaño y la profundidad del daño antes de hablar de las opciones.',
   'Las fotos ayudan a comenzar, pero algunos daños requieren una inspección en persona. Pregunte qué reparaciones y trabajos de pintura están incluidos en su estimado por escrito.'],
  ['glass-detailing','Cristales y cuidado final','Pregunte por el reemplazo de cristales, la limpieza detallada y la restauración de faros. Confirmaremos el servicio adecuado para su vehículo y cualquier trabajo relacionado antes de coordinar una cita.','Reemplazo de cristales · Limpieza detallada · Restauración de faros',
   'Díganos si necesita revisar un cristal dañado, restaurar los faros o hacer una limpieza detallada. Confirmaremos el servicio y su alcance cuando se comunique con el taller.',
   'Para los cristales, pregunte si su vehículo requiere calibración de cámaras o sensores. La disponibilidad, el método y cualquier trabajo especializado deben confirmarse para su vehículo.']
 ],
 'work_title':'CONOZCA<br>NUESTRO TALLER.','work_copy':'Siga a @somicoachworks para ver las fotos y novedades que comparte nuestro equipo. Explore las publicaciones y llámenos para hablar de su reparación.',
 'ig_cta':'Ver trabajos en Instagram','ig_label':'FOTOS Y NOVEDADES','ig_note':'Abre el perfil de Instagram del taller.',
 'about_title':'Sobre el taller','about_copy':'Somos South Miami Coach Works, también conocido como SOMI Coachworks. Nuestro taller de carrocería y pintura está en SW 68th Street, cerca de Red Road, en South Miami.',
 'about_more':'Nuestro equipo cuenta con más de 20 años de experiencia. Hable con nosotros en español o inglés sobre daños por choques, carrocería o su próximo proyecto de pintura.',
 'experience':'20+','experience_label':'años de experiencia','experience_note':'Según el perfil de Instagram de nuestro taller.',
 'areas_title':'Zonas que atendemos','areas':'Visítenos desde South Miami, Coral Gables, Pinecrest, Kendall, Westchester y las comunidades cercanas de Miami.',
 'process_title':'Cómo funciona','steps':[['Llame para un estimado','Cuéntenos sobre el vehículo y los daños, y coordinamos una revisión.'],['Revise la reparación','Repasamos con usted el trabajo, el reclamo del seguro y el plazo.'],['Traiga su vehículo','Traiga el vehículo cuando el trabajo y la fecha estén confirmados.']],
 'reviews_title':'Reseñas de clientes','review_excerpt':'Reseñas de Google en su idioma original (inglés).','read_reviews':'Leer reseñas en Google','leave_review':'Déjenos una reseña','leave_note':'','review_label':'Reseña de Google',
 'estimate_title':'Pida un estimado gratis','estimate_copy':'Llame al taller para coordinar un estimado gratis. Tenga a mano el año, la marca y el modelo, y cuéntenos dónde está el daño.',
 'contact_title':'Llámenos o escríbanos','contact_text':'Hable con nosotros sobre la reparación y cuándo traer el vehículo, o envíenos los detalles y algunas fotos de los daños por correo.',
 'email':'Escribir al taller','send_photos':'Puede adjuntar las fotos de los daños al correo.','estimate_note':'El taller confirma todas las citas, los precios y la disponibilidad.',
 'form_title':'Solicite un estimado','form_intro':'Describa el vehículo y agregue fotos de los daños. El taller confirmará los próximos pasos; enviar la solicitud no reserva una cita.',
 'name':'Su nombre','phone':'Número de teléfono','email_label':'Correo electrónico','year':'Año del vehículo','vehicle':'Marca y modelo','service':'Servicio','select':'Seleccione un servicio','other_service':'Otro / no estoy seguro','details':'Describa los daños','insurance':'Compañía de seguros (opcional)','photos':'Fotos de los daños (opcional)','photo_help':'Hasta 5 imágenes JPG, PNG o WebP, de 5 MB cada una.','consent':'Acepto que el taller me contacte sobre esta solicitud.','submit':'Enviar solicitud','form_privacy':'Usamos sus datos de contacto y fotos para responder a esta solicitud.','form_error':'No pudimos enviar su solicitud. Sus datos siguen aquí. Inténtelo de nuevo o llame al (305) 397-8911.','form_success':'Su solicitud fue enviada. El taller confirmará los próximos pasos.','form_sending':'Enviando…','form_invalid':'Agregue hasta 5 imágenes JPG, PNG o WebP de 5 MB o menos cada una.','form_phone_error':'Ingrese un teléfono válido con código de área.','form_photo_count':'fotos seleccionadas','form_external':'Abrir formulario seguro',
 'visit_title':'Horario y ubicación','directions':'Cómo llegar','hours':'Horario del taller','monday':'Lunes','weekdays':'Martes a viernes','weekends':'Sábado y domingo','closed':'Cerrado','hours_note':'Llame antes de venir, especialmente en días festivos.','hours_open':'Abierto ahora','hours_closed':'Cerrado ahora','maps':'Abrir en Google Maps',
 'faq_title':'Preguntas frecuentes','faq_intro':'¿Tiene otra pregunta? Llámenos.',
 'faqs':[
  ['¿Los estimados son gratis?','Sí. Llámenos al (305) 397-8911 para coordinar una evaluación. Tenga a mano el año, la marca, el modelo y una descripción de los daños.'],
  ['¿Me pueden ayudar con el reclamo del seguro?','Sí. Ayudamos con reclamos y trabajamos con todas las compañías de seguros. Traiga el nombre de su aseguradora y el número del reclamo; la cobertura, el deducible y el pago dependen de su póliza y aseguradora.'],
  ['¿Puedo elegir mi taller?','Sí. El Departamento de Servicios Financieros de Florida indica que usted puede seleccionar el taller que repare su auto después de un accidente. Hable con su aseguradora sobre la cobertura, el estimado y cualquier diferencia de costo antes de autorizar el trabajo.'],
  ['¿Trabajan con mi marca y modelo?','Sí. Trabajamos con todas las marcas y modelos. Llame con los datos del vehículo para confirmar el trabajo, las piezas y cualquier servicio especializado necesario.'],
  ['¿Qué garantía tiene mi reparación?','Pídanos los términos de la garantía por escrito para su reparación antes de autorizar el trabajo. Hablaremos de la cobertura, su duración y las exclusiones.'],
  ['¿Me pueden ayudar con una grúa o un auto de alquiler?','Llámenos antes de coordinar una grúa para confirmar dónde y cuándo recibir el vehículo. Pregunte por la asistencia de grúa y las opciones de alquiler disponibles; la cobertura del alquiler depende de su póliza.'],
  ['¿Cuánto tarda la reparación?','El plazo depende de los daños, las piezas y el trabajo necesario. Hablaremos del tiempo previsto después de revisar el vehículo. Para consultar el estado de una reparación, llámenos directamente.']
 ],
 'consumer_guide':'Guía de Florida para consumidores (inglés)','claims':'Reclamos de seguros','back':'Volver al inicio','top':'Volver arriba','footer_line':'5780 SW 68th St · South Miami, FL 33143','footer_areas':'Carrocería y reparación de choques para South Miami, Coral Gables, Pinecrest, Kendall y Westchester.','footer_cta':'Llame por su reparación',
 'privacy_title':'Su privacidad','privacy_text':'Cuando llama o escribe al taller, sus datos de contacto y fotos se usan para responder a su consulta. Un formulario en línea, cuando esté disponible, también comparte esos datos con el proveedor del formulario y el taller. No envíe datos de pago, documentos de identidad ni información personal innecesaria.',
 'privacy_more':'Google Maps e Instagram tienen sus propias políticas de privacidad. Este sitio no usa analítica publicitaria. Si tiene preguntas sobre datos enviados al taller, escriba a somicoachworks@gmail.com.',
 'photo_title':'Fotografía','photo_text':'La imagen principal es una fotografía de automóviles de Unsplash. No se presenta como un trabajo de SOMI ni como una imagen de sus instalaciones.','photo_link':'Ver fuente de la foto','close':'Cerrar ventana',
 'claim_title':'Ayuda con su reclamo','claim_intro':'Traiga la información de su reclamo. Hablaremos de la evaluación y los próximos pasos de la reparación.',
 'claim_sections':[['Qué debe tener a mano','Traiga los datos del vehículo, el nombre de la aseguradora, el número del reclamo y la información del ajustador, si la tiene. Guarde copias del estimado y de las autorizaciones que firme.'],['Usted elige el taller','La guía de Florida para consumidores indica que puede elegir su taller después de un accidente. Hable con su aseguradora sobre la cobertura y cualquier diferencia entre los estimados antes de comenzar.'],['Confirme lo autorizado','Confirme el trabajo, el deducible, la forma de pago y cualquier autorización adicional si se descubren otros daños. El taller no puede garantizar la cobertura ni el reembolso de un vehículo de alquiler.']],
 'detail_next':'¿Hablamos de su vehículo?','detail_note':'Puede ser necesaria una evaluación en persona para confirmar el alcance y el precio.'
}

SERVICE_ICONS = {'collision-repair':'collision','paint-refinishing':'paint','body-dent-repair':'body','glass-detailing':'glass'}

REVIEWS = [('NC','Nelson Colon','Great job by Carlos and his team. Great quality and turn around time was quick.'),('AG','Andrew Gamil','My car looked brand new! I plan on bringing my other vehicle to get the same treatment! Highly recommend!'),('MT','Martin Thiry','I highly recommend this auto body shop. The service is excellent and work is completed on time and perfect the first time.')]

def button(text, href, style='red', extra=''):
 return f'<a class="button button-{style}" href="{escape(href)}" {extra}>{text}</a>'

def logo(home, white=False):
 src = '/assets/somi-logo-white.png' if white else '/assets/somi-logo.png'
 return f'<a class="wordmark brand-mark" href="{home}#top" aria-label="Somi Coach Works — home"><img src="{src}" alt="SoMi Coach Works — We Meet By Accident" width="520" height="297"></a>'

AREAS = ['South Miami','Coral Gables','Pinecrest','Kendall','Westchester']

# Page-specific titles and meta descriptions (visible in search results).
SEO = {
 'en': {
  'collision-repair': ('Collision Repair in South Miami, FL', 'Collision repair in South Miami, FL. We assess accident damage, plan the repair with you and help with insurance claims. Free estimates: (305) 397-8911.'),
  'paint-refinishing': ('Auto Paint & Refinishing in South Miami, FL', 'Auto paint and refinishing in South Miami, FL: scratches, paint damage and panel refinishing for all makes and models. Free estimates: (305) 397-8911.'),
  'body-dent-repair': ('Body & Dent Repair in South Miami, FL', 'Body and dent repair in South Miami, FL for dents, scrapes and damaged panels. We inspect the damage and explain your options. Call (305) 397-8911.'),
  'glass-detailing': ('Auto Glass, Detailing & Headlight Restoration in South Miami', 'Auto glass replacement, detailing and headlight restoration in South Miami, FL. Ask South Miami Coach Works about your vehicle: (305) 397-8911.'),
  'insurance-claims': ('Insurance Claim Help for Auto Body Repair in South Miami', 'Insurance claim help for collision and auto body repair in South Miami, FL. What to bring, your choice of shop in Florida, and next steps.'),
 },
 'es': {
  'collision-repair': ('Reparación de choques en South Miami, FL', 'Reparación de choques en South Miami, FL. Evaluamos los daños, planificamos la reparación y le ayudamos con el seguro. Estimados gratis: (305) 397-8911.'),
  'paint-refinishing': ('Pintura y acabado de autos en South Miami, FL', 'Pintura y acabado de autos en South Miami, FL: rayones, daños en la pintura y paneles, todas las marcas. Estimados gratis: (305) 397-8911.'),
  'body-dent-repair': ('Carrocería y abolladuras en South Miami, FL', 'Reparación de carrocería y abolladuras en South Miami, FL: golpes, roces y paneles dañados. Revisamos el daño y le explicamos las opciones.'),
  'glass-detailing': ('Cristales, limpieza detallada y faros en South Miami', 'Reemplazo de cristales, limpieza detallada y restauración de faros en South Miami, FL. Consulte a South Miami Coach Works: (305) 397-8911.'),
  'insurance-claims': ('Ayuda con reclamos de seguro en South Miami, FL', 'Ayuda con reclamos de seguro para reparación de choques y carrocería en South Miami, FL. Qué traer, cómo elegir taller en Florida y próximos pasos.'),
 },
}

# Security policy for a static site: only this site's own scripts, styles and fonts;
# Google for the map frame; Formspree only if the estimate form is ever enabled.
CSP = ("default-src 'self'; script-src 'self'; style-src 'self'; font-src 'self'; img-src 'self' data: blob:; "
       "connect-src 'self' https://formspree.io; frame-src https://www.google.com https://maps.google.com; "
       "form-action 'self' https://formspree.io; base-uri 'self'; object-src 'none'; upgrade-insecure-requests")

def business():
 return {'@type':'AutoBodyShop','@id':ORIGIN+'/#business','name':'South Miami Coach Works','alternateName':['SOMI Coachworks','Somi Coach Works'],
  'description':'Auto body shop in South Miami, FL offering collision repair, paint and refinishing, body and dent repair, auto glass and detailing, with insurance claim assistance. Se habla español.',
  'url':ORIGIN+'/','logo':ORIGIN+'/assets/somi-logo.png','image':[ORIGIN+'/assets/shop-share.jpg',ORIGIN+'/assets/shop-exterior.jpg'],
  'telephone':'+1-305-397-8911','email':'somicoachworks@gmail.com',
  'address':{'@type':'PostalAddress','streetAddress':'5780 SW 68th St','addressLocality':'South Miami','addressRegion':'FL','postalCode':'33143','addressCountry':'US'},
  'hasMap':MAP,
  'openingHoursSpecification':[{'@type':'OpeningHoursSpecification','dayOfWeek':['Monday'],'opens':'07:30','closes':'17:00'},{'@type':'OpeningHoursSpecification','dayOfWeek':['Tuesday','Wednesday','Thursday','Friday'],'opens':'07:30','closes':'17:30'}],
  'areaServed':[{'@type':'City','name':a,'containedInPlace':{'@type':'State','name':'Florida'}} for a in AREAS],
  'knowsLanguage':['en','es'],
  'contactPoint':{'@type':'ContactPoint','telephone':'+1-305-397-8911','contactType':'customer service','availableLanguage':['English','Spanish'],'areaServed':'US'},
  'makesOffer':[{'@type':'Offer','itemOffered':{'@type':'Service','@id':ORIGIN+'/services/'+slug+'/#service','name':name}} for slug,name in [('collision-repair','Collision repair'),('paint-refinishing','Auto paint and refinishing'),('body-dent-repair','Body and dent repair'),('glass-detailing','Auto glass, detailing and headlight restoration')]],
  'sameAs':[IG,MAP]}
 # Geo coordinates and aggregateRating are intentionally omitted: coordinates are unverified,
 # and Google does not show self-published review ratings for a local business.

def ld(nodes):
 # Escape "</" so structured data can never close the script element early.
 return json.dumps({'@context':'https://schema.org','@graph':nodes},ensure_ascii=False).replace('</','<\\/')

def head(d, path='', detail=None, desc=None, extra=(), noindex=False):
 url=ORIGIN+d['home']+path
 title=(detail or d['title'])+' | South Miami Coach Works'
 desc=desc or d['description']
 lang='es-US' if d['lang']=='es' else 'en-US'
 nodes=[business(),
  {'@type':'WebSite','@id':ORIGIN+'/#website','url':ORIGIN+'/','name':'South Miami Coach Works','inLanguage':['en-US','es-US'],'publisher':{'@id':ORIGIN+'/#business'}},
  {'@type':'WebPage','@id':url+'#webpage','url':url,'name':title,'description':desc,'inLanguage':lang,'isPartOf':{'@id':ORIGIN+'/#website'},'about':{'@id':ORIGIN+'/#business'},'primaryImageOfPage':ORIGIN+'/assets/shop-share.jpg'},
  *extra]
 links=('<meta name="robots" content="noindex">' if noindex else
  f'<meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="{url}"><link rel="alternate" hreflang="en" href="{ORIGIN}/{path}"><link rel="alternate" hreflang="es" href="{ORIGIN}/es/{path}"><link rel="alternate" hreflang="x-default" href="{ORIGIN}/{path}">')
 copy=json.dumps({k:d[k] for k in ['lang','hours_open','hours_closed','form_error','form_success','form_sending','submit','form_invalid','form_phone_error','form_photo_count']},ensure_ascii=False).replace('</','<\\/')
 return f'''<!doctype html><html lang="{d['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="{CSP}"><meta name="referrer" content="strict-origin-when-cross-origin"><meta name="theme-color" content="#0c1e3c"><title>{escape(title)}</title><meta name="description" content="{escape(desc,quote=True)}">{links}<meta property="og:site_name" content="South Miami Coach Works"><meta property="og:title" content="{escape(title,quote=True)}"><meta property="og:description" content="{escape(desc,quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:image" content="{ORIGIN}/assets/shop-share.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="South Miami Coach Works shop exterior at 5780 SW 68th St"><meta property="og:locale" content="{'es_US' if d['lang']=='es' else 'en_US'}"><meta property="og:locale:alternate" content="{'en_US' if d['lang']=='es' else 'es_US'}"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/assets/icon-32.png" sizes="32x32" type="image/png"><link rel="apple-touch-icon" href="/assets/icon-180.png"><link rel="preload" href="/assets/fonts/archivo-latin-wdth.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/assets/fonts/inter-latin-wght.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/assets/fonts/fonts.css"><link rel="stylesheet" href="/styles.css"><link rel="stylesheet" href="/updates.css"><link rel="stylesheet" href="/brand.css"><link rel="stylesheet" href="/polish.css"><script src="/app.js" defer></script><script id="site-copy" type="application/json">{copy}</script><script type="application/ld+json">{ld(nodes)}</script></head><body id="top"><a class="skip-link" href="#main">{d['skip']}</a>'''

def breadcrumbs(d, items):
 return {'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':i+1,'name':n,'item':ORIGIN+u} for i,(n,u) in enumerate(items)]}

def header(d,path=''):
 links=''.join(f'<a href="{d["home"]}#{a}">{d[b]}</a>' for a,b in [('services','services'),('work','work'),('about','about'),('reviews','reviews'),('visit','visit')])
 return f'''<header class="header"><div class="container nav-inner">{logo(d['home'])}<nav class="desktop-nav" aria-label="{'Navegación' if d['lang']=='es' else 'Main navigation'}">{links}</nav><a class="button button-red nav-call" href="tel:+13053978911" aria-label="{d['call']}">{icon('phone')}<span>(305) 397-8911</span></a><a class="language-toggle" href="{d['other']}{path}" lang="{'en' if d['lang']=='es' else 'es'}" hreflang="{'en' if d['lang']=='es' else 'es'}">{d['other_label']}</a><button class="menu-toggle" type="button" aria-label="{'Abrir menú' if d['lang']=='es' else 'Open menu'}" aria-expanded="false" aria-controls="mobile-nav"><span></span><span></span></button></div><nav class="mobile-nav" id="mobile-nav" aria-label="{'Menú móvil' if d['lang']=='es' else 'Mobile navigation'}" hidden>{links}<a href="{d['home']}#estimate">{d['estimate']}</a></nav></header>'''

def footer(d):
 links=''.join(f'<a href="{d["home"]}{path}">{label}</a>' for path,label in [('#services',d['services']),('#about',d['about']),('#reviews',d['reviews']),('insurance-claims/',d['claims'])])
 return f'''<footer class="footer"><div class="container"><div class="footer-top">{logo(d['home'], True)}<p>{d['footer_line']}<br>{d['footer_areas']}</p><a class="footer-cta" href="tel:+13053978911">{d['footer_cta']}</a></div><div class="footer-links">{links}<a href="{IG}" target="_blank" rel="noopener noreferrer">Instagram</a><a href="tel:+13053978911">(305) 397-8911</a><a href="mailto:somicoachworks@gmail.com">somicoachworks@gmail.com</a></div><div class="footer-bottom"><span>© <span id="copyright-year">2026</span> South Miami Coach Works.</span><button type="button" data-open-dialog="privacy-dialog">{d['privacy']}</button><a href="#top" class="back-top">{d['top']}</a></div></div></footer><div class="mobile-actions"><a href="tel:+13053978911">{d['call']}</a><a href="{d['home']}#estimate">{d['estimate']}</a></div><dialog id="privacy-dialog" aria-labelledby="privacy-title"><div class="dialog-header"><h2 id="privacy-title">{d['privacy_title']}</h2><button class="dialog-close" type="button" aria-label="{d['close']}">×</button></div><p>{d['privacy_text']}</p><p>{d['privacy_more']}</p></dialog></body></html>'''

def form(d):
 fields=''
 for name,kind,auto in [('name','text','name'),('phone','tel','tel'),('email_label','email','email'),('year','number','off'),('vehicle','text','off')]:
  key='email' if name=='email_label' else name
  limits='min="1900" max="2028"' if name=='year' else ('maxlength="25"' if name=='phone' else 'maxlength="120"')
  fields+=f'<div><label for="{key}">{d[name]} *</label><input id="{key}" name="{key}" type="{kind}" autocomplete="{auto}" {limits} required></div>'
 options=''.join(f'<option value="{s[0]}">{s[1]}</option>' for s in d['service_data'])
 return f'''<div id="online-request" hidden><h3>{d['form_title']}</h3><p>{d['form_intro']}</p><form id="estimate-form" enctype="multipart/form-data"><div class="field-grid">{fields}</div><label for="service">{d['service']} *</label><select id="service" name="service" required><option value="">{d['select']}</option>{options}<option value="other">{d['other_service']}</option></select><label for="details">{d['details']} *</label><textarea id="details" name="details" rows="4" maxlength="2000" required></textarea><label for="insurance">{d['insurance']}</label><input id="insurance" name="insurance" maxlength="100"><label for="photos">{d['photos']}</label><input type="file" id="photos" name="attachment" accept="image/jpeg,image/png,image/webp" multiple aria-describedby="photo-help"><p id="photo-help" class="form-disclosure">{d['photo_help']}</p><div id="photo-previews" class="photo-previews"></div><label class="consent"><input type="checkbox" name="consent" value="yes" required><span>{d['consent']}</span></label><div class="honeypot" aria-hidden="true"><label for="website">Website</label><input id="website" name="_gotcha" tabindex="-1" autocomplete="off"></div><button class="button button-red form-next" id="submit-request" type="submit">{d['submit']}</button><p id="form-status" role="status" aria-live="polite" tabindex="-1"></p><p class="form-disclosure">{d['form_privacy']}</p></form></div>'''

def home(d):
 faq={'@type':'FAQPage','@id':ORIGIN+d['home']+'#faq','inLanguage':'es-US' if d['lang']=='es' else 'en-US','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in d['faqs']]}
 h=head(d,extra=[faq])+header(d)+'<main id="main">'
 h+=f'''<section class="hero" aria-labelledby="hero-title"><picture class="hero-picture"><source srcset="/assets/shop-exterior.webp" type="image/webp"><img class="hero-photo" src="/assets/shop-exterior.jpg" alt="{'Fachada y estacionamiento de South Miami Coach Works en 5780 SW 68th St' if d['lang']=='es' else 'South Miami Coach Works exterior and front parking lot at 5780 SW 68th St'}" width="1525" height="1031" fetchpriority="high"></picture><div class="hero-shade"></div><div class="container hero-content"><h1 id="hero-title">{d['hero']}</h1><p class="hero-description">{d['hero_copy']}</p><div class="hero-actions">{button(d['call'],'tel:+13053978911')}{button(d['estimate'],'#estimate','outline')}</div><a class="hero-proof" href="{MAP}" target="_blank" rel="noopener noreferrer"><span class="stars" aria-hidden="true">★★★★★</span><span>{d['rating']}</span></a></div></section><div class="trust-strip"><div class="container trust-inner">{''.join('<span>'+icon(k)+x+'</span>' for k,x in zip(['estimate','makes','insurance','language'],d['trust']))}</div></div>'''
 h+=f'''<section class="section services-section" id="services"><div class="container"><div class="section-heading"><div><h2>{d['services_title']}</h2></div><p>{d['services_intro']}</p></div><div class="service-card-grid">'''
 for s in d['service_data']:
  h+=f'<article class="service-card"><span class="service-icon">{icon(SERVICE_ICONS[s[0]])}</span><h3>{s[1]}</h3><p>{s[2]}</p><a class="text-link" href="{d["home"]}services/{s[0]}/">{d["learn"]}</a></article>'
 h+=f'''</div><div class="services-footnote"><span>{d['not_sure']}</span><a href="tel:+13053978911">{d['ask']}</a></div></div></section>{gallery(d)}'''
 h+=f'''<section class="section approach-section" id="about"><div class="container approach-top"><div><h2>{d['about_title']}</h2></div><div class="approach-intro"><p>{d['about_copy']}</p><p>{d['about_more']}</p><div class="experience"><strong>{d['experience']}</strong><span>{d['experience_label']}</span></div></div></div><div class="container process-label"><h3>{d['process_title']}</h3></div><div class="container process-grid">'''
 for n,step in enumerate(d['steps'],1):h+=f'<article><span class="process-number">0{n}</span><h3>{step[0]}</h3><p>{step[1]}</p></article>'
 h+=f'''</div><div class="container service-area"><h3>{d['areas_title']}</h3><p>{d['areas']}</p></div></section><section class="section reviews-section" id="reviews"><div class="container"><div class="section-heading"><div><h2>{d['reviews_title']}</h2></div><a class="rating-block" href="{MAP}" target="_blank" rel="noopener noreferrer"><span class="rating-score">5.0<span class="stars" aria-hidden="true">★★★★★</span></span><span class="rating-caption">{GOOGLE_G}{d['rating'].split(' · ')[1]}</span></a></div>{f'<p class="review-context">{d["review_excerpt"]}</p>' if d['review_excerpt'] else ''}<div class="review-grid">'''
 for _,name,quote in REVIEWS:h+=f'<figure class="review-card"><span class="stars" role="img" aria-label="5 / 5">★★★★★</span><blockquote lang="en">“{quote}”</blockquote><figcaption><b>{name}</b><small>{GOOGLE_G}{d['review_label']}</small></figcaption></figure>'
 h+=f'''</div><div class="reviews-bottom"><a class="text-link" href="{MAP}" target="_blank" rel="noopener noreferrer">{d['read_reviews']}</a><a class="text-link" href="{MAP}" target="_blank" rel="noopener noreferrer">{d['leave_review']}</a></div></div></section>'''
 h+=f'''<section class="contact-section" id="estimate"><div class="container contact-grid"><div class="contact-copy"><h2>{d['estimate_title']}</h2><p>{d['estimate_copy']}</p><div class="contact-note"><p>{d['estimate_note']}</p></div></div><div class="estimate-card"><div id="contact-options"><h3>{d['contact_title']}</h3><p>{d['contact_text']}</p>{button(d['call'],'tel:+13053978911')}<a class="text-link contact-email" href="mailto:somicoachworks@gmail.com" aria-label="{d['email']}: somicoachworks@gmail.com">{icon('mail')}somicoachworks@gmail.com</a><p class="form-disclosure">{d['send_photos']}</p><a id="external-form" class="button button-dark" hidden>{d['form_external']}</a></div>{form(d)}</div></div></section>'''
 h+=f'''<section class="section visit-section" id="visit"><div class="container visit-grid"><div class="visit-copy"><h2>{d['visit_title']}</h2><address>{icon('pin')}<span>South Miami Coach Works<br>5780 SW 68th St<br>South Miami, FL 33143</span></address><div class="visit-actions">{button(d['directions'],DIRECTIONS,'dark','target="_blank" rel="noopener noreferrer"')}</div></div><div class="hours-card"><div class="hours-title"><h3>{icon('clock')}{d['hours']}</h3><span class="hours-status" id="hours-status"></span></div><dl><div data-days="1"><dt>{d['monday']}</dt><dd>7:30 AM – 5:00 PM</dd></div><div data-days="2,3,4,5"><dt>{d['weekdays']}</dt><dd>7:30 AM – 5:30 PM</dd></div><div data-days="6,0"><dt>{d['weekends']}</dt><dd>{d['closed']}</dd></div></dl><p>{d['hours_note']}</p><a href="tel:+13053978911">(305) 397-8911</a></div><div class="map-wrap"><iframe title="South Miami Coach Works — 5780 SW 68th St" src="https://www.google.com/maps?q=South+Miami+Coach+Works+5780+SW+68th+St+South+Miami+FL+33143&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe><a class="map-fallback" href="{MAP}" target="_blank" rel="noopener noreferrer">{d['maps']}</a></div></div></section><section class="faq-section"><div class="container faq-grid"><div><h2>{d['faq_title']}</h2><p><a href="tel:+13053978911">{d['faq_intro']}</a></p><a class="text-link" href="{d['home']}insurance-claims/">{d['claims']}</a></div><div class="faq-list">'''
 for n,(q,a) in enumerate(d['faqs']):
  source=f' <a href="{DFS}" target="_blank" rel="noopener noreferrer">{d["consumer_guide"]}</a>' if n==2 else ''
  h+=f'<details><summary>{q}<span aria-hidden="true">+</span></summary><p>{a}{source}</p></details>'
 return h+'</div></div></section></main>'+footer(d)

def detail(d,s=None):
 path='services/'+s[0]+'/' if s else 'insurance-claims/'
 title=s[1] if s else d['claims']
 intro=s[2] if s else d['claim_intro']
 slug=s[0] if s else 'insurance-claims'
 seo_title,seo_desc=SEO[d['lang']][slug]
 home_name='Inicio' if d['lang']=='es' else 'Home'
 crumbs=[(home_name,d['home'])]+([(d['services'],d['home']+'#services')] if s else [])+[(title,d['home']+path)]
 extra=[breadcrumbs(d,crumbs)]
 if s: extra.append({'@type':'Service','@id':ORIGIN+d['home']+path+'#service','name':title,'serviceType':title,'description':s[2],'provider':{'@id':ORIGIN+'/#business'},'areaServed':[{'@type':'City','name':a} for a in AREAS],'url':ORIGIN+d['home']+path,'inLanguage':'es-US' if d['lang']=='es' else 'en-US'})
 h=head(d,path,seo_title,seo_desc,extra)+header(d,path)+f'<main id="main"><section class="detail-hero"><div class="container"><a class="text-link light" href="{d["home"]}">{d["back"]}</a><h1>{escape(title)}</h1><p>{intro}</p>{button(d["call"],"tel:+13053978911")}</div></section><section class="section"><div class="container detail-body">'
 if s:h+=f'<p class="detail-tags">{s[3]}</p><p>{s[4]}</p><p>{s[5]}</p>'
 else:
  for t,p in d['claim_sections']:h+=f'<h2>{t}</h2><p>{p}</p>'
  h+=f'<a class="text-link" href="{DFS}" target="_blank" rel="noopener noreferrer">{d["consumer_guide"]}</a>'
 h+=f'<div class="detail-contact"><h2>{d["detail_next"]}</h2><p>{d["detail_note"]}</p>{button(d["estimate"],d["home"]+"#estimate")}</div></div></section></main>'
 return path,h+footer(d)

paths=[]
for d in (EN,ES):
 base=DIST / d['home'].lstrip('/')
 base.mkdir(parents=True,exist_ok=True)
 (base/'index.html').write_text(home(d))
 paths.append(d['home'])
 for s in [*d['service_data'],None]:
  path,html=detail(d,s);target=base/path;target.mkdir(parents=True,exist_ok=True);(target/'index.html').write_text(html);paths.append(d['home']+path)
def not_found(d):
 msg={'title':'Page not found','h1':'Page not found','p':'The page you’re looking for doesn’t exist or has moved.'}
 return head(d,'',msg['title'],msg['p'],noindex=True)+header(d)+f'''<main id="main"><section class="detail-hero"><div class="container"><h1>{msg['h1']}</h1><p>{msg['p']} <span lang="es">La página que busca no existe o cambió de dirección.</span></p>{button(d['call'],'tel:+13053978911')} <a class="button button-outline" href="/">Home</a> <a class="button button-outline" href="/es/" lang="es">Inicio en español</a></div></section></main>'''+footer(d)
(DIST/'404.html').write_text(not_found(EN))
pairs=[p for p in paths if not p.startswith('/es/')]
def alt(p): return ''.join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{ORIGIN}{u}"/>' for l,u in [('en',p),('es','/es'+p),('x-default',p)])
(DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'+''.join(f'<url><loc>{ORIGIN}{u}</loc>{alt(p)}</url>' for p in pairs for u in (p,'/es'+p))+'</urlset>\n')
(DIST/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+ORIGIN+'/sitemap.xml\n')
print('Built',len(paths),'pages with matching English/Spanish routes, canonical links and sitemap.')
