(() => {
  'use strict';
  const $ = s => document.querySelector(s);
  const $$ = s => [...document.querySelectorAll(s)];
  const copy = JSON.parse($('#site-copy').textContent);
  const menu = $('.menu-toggle'), nav = $('#mobile-nav');
  const setMenu = open => {
    menu.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-label', copy.lang === 'es' ? (open ? 'Cerrar menú' : 'Abrir menú') : (open ? 'Close menu' : 'Open menu'));
    nav.hidden = !open;
    document.body.classList.toggle('menu-open', open);
  };
  menu.addEventListener('click', () => setMenu(nav.hidden));
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && !nav.hidden) { setMenu(false); menu.focus(); } });
  window.matchMedia('(min-width: 901px)').addEventListener('change', e => { if (e.matches) setMenu(false); });
  const updateHours = () => {
    if (!$('#hours-status')) return;
    const parts = Object.fromEntries(new Intl.DateTimeFormat('en-US', {timeZone:'America/New_York',weekday:'short',hour:'numeric',minute:'numeric',hourCycle:'h23'}).formatToParts(new Date()).map(p => [p.type,p.value]));
    const day = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].indexOf(parts.weekday);
    const minute = +parts.hour * 60 + +parts.minute;
    const open = day >= 1 && day <= 5 && minute >= 450 && minute < (day === 1 ? 1020 : 1050);
    $('#hours-status').textContent = copy[open ? 'hours_open' : 'hours_closed'];
    $('#hours-status').classList.toggle('open', open);
    $$('[data-days]').forEach(row => row.classList.toggle('today', row.dataset.days.split(',').includes(String(day))));
  };
  updateHours();
  if ($('#hours-status')) window.setInterval(updateHours, 60000);
  $('#copyright-year').textContent = new Date().getFullYear();
  let trigger;
  $$('[data-open-dialog]').forEach(button => button.addEventListener('click', () => {trigger = button; $('#' + button.dataset.openDialog).showModal();}));
  $$('dialog').forEach(dialog => {
    dialog.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
    dialog.addEventListener('close', () => trigger?.focus());
    dialog.addEventListener('click', e => {
      if (e.target !== dialog) return;
      const r = dialog.getBoundingClientRect();
      if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dialog.close();
    });
  });
  // Paired repair stories use separate photographs, preserving the original viewpoints.
  const storyTabs = $$('[data-story-tab]');
  const stories = $$('[data-story]');
  if (storyTabs.length) {
    $('.repair-tabs').hidden = false;
    const selectStory = (tab, focus = false) => {
      storyTabs.forEach(t => {
        const selected = t === tab;
        t.setAttribute('aria-selected', String(selected)); t.tabIndex = selected ? 0 : -1;
      });
      stories.forEach(story => {
        story.hidden = story.dataset.story !== tab.dataset.storyTab;
        story.setAttribute('role', 'tabpanel'); story.setAttribute('aria-labelledby', 'tab-' + story.dataset.story);
        story.tabIndex = 0;
      });
      if (focus) tab.focus();
    };
    storyTabs.forEach((tab, index) => {
      tab.addEventListener('click', () => selectStory(tab));
      tab.addEventListener('keydown', e => {
        let next;
        if (e.key === 'ArrowRight') next = (index + 1) % storyTabs.length;
        if (e.key === 'ArrowLeft') next = (index + storyTabs.length - 1) % storyTabs.length;
        if (e.key === 'Home') next = 0;
        if (e.key === 'End') next = storyTabs.length - 1;
        if (next !== undefined) { e.preventDefault(); selectStory(storyTabs[next], true); }
      });
    });
    selectStory(storyTabs[0]);
    stories.forEach(story => {
      story.querySelector('.view-switch').hidden = false;
      story.querySelectorAll('[data-view-button]').forEach(button => button.addEventListener('click', () => {
        const view = button.dataset.viewButton; story.dataset.view = view;
        story.querySelectorAll('[data-view-button]').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
        story.querySelectorAll('[data-photo-state]').forEach(photo => {photo.hidden = view !== 'both' && photo.dataset.photoState !== view;});
      }));
    });
    const lightbox = $('#repair-lightbox');
    let photos = [], photoIndex = 0;
    const showPhoto = index => {
      photoIndex = (index + photos.length) % photos.length;
      const link = photos[photoIndex], original = link.querySelector('img');
      $('#lightbox-image').src = link.href;
      $('#lightbox-image').alt = original.alt;
      $('#lightbox-title').textContent = link.dataset.caption;
      $('#lightbox-count').textContent = `${photoIndex + 1} / ${photos.length}`;
    };
    $$('[data-photo-open]').forEach(link => link.addEventListener('click', e => {
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      e.preventDefault(); trigger = link;
      photos = [...link.closest('[data-story]').querySelectorAll('[data-photo-open]')];
      showPhoto(photos.indexOf(link)); lightbox.showModal(); document.body.classList.add('lightbox-open');
    }));
    $('#lightbox-prev').addEventListener('click', () => showPhoto(photoIndex - 1));
    $('#lightbox-next').addEventListener('click', () => showPhoto(photoIndex + 1));
    lightbox.addEventListener('keydown', e => {
      if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') { e.preventDefault(); showPhoto(photoIndex + (e.key === 'ArrowLeft' ? -1 : 1)); }
    });
    lightbox.addEventListener('close', () => document.body.classList.remove('lightbox-open'));
  }

  // Do not accept leads without a verified, shop-owned destination.
  const form = $('#estimate-form');
  if (!form) return;
  $('#year').max = new Date().getFullYear() + 2;
  let endpoint, sending = false, previews = [];
  const clearPreviews = () => {previews.forEach(URL.revokeObjectURL); previews = []; $('#photo-previews').replaceChildren();};
  const validFiles = () => {
    const files = [...$('#photos').files];
    const ok = files.length <= 5 && files.every(f => ['image/jpeg','image/png','image/webp'].includes(f.type) && f.size > 0 && f.size <= 5 * 1024 * 1024);
    $('#photos').setCustomValidity(ok ? '' : copy.form_invalid);
    return ok;
  };
  $('#photos').addEventListener('change', () => {
    clearPreviews();
    if (!validFiles()) {$('#photos').reportValidity(); return;}
    [...$('#photos').files].forEach(file => {
      const url = URL.createObjectURL(file); previews.push(url);
      const figure = document.createElement('figure'), img = document.createElement('img'), caption = document.createElement('figcaption');
      img.src = url; img.alt = file.name; caption.textContent = file.name;
      figure.append(img, caption); $('#photo-previews').append(figure);
    });
  });
  $('#phone').addEventListener('input', () => $('#phone').setCustomValidity(''));
  fetch('/site-config.json', {cache:'no-store'}).then(r => r.ok ? r.json() : null).then(config => {
    if (!config) return;
    if (config.formspreeEndpoint && config.photoUploadsVerified === true && /^https:\/\/formspree\.io\/f\/[a-zA-Z0-9]+$/.test(config.formspreeEndpoint)) {
      endpoint = config.formspreeEndpoint;
      $('#online-request').hidden = false;
      $('#contact-options').hidden = true;
    } else if (config.jotformUrl && /^https:\/\/form\.jotform\.com\/\d+\/?$/.test(config.jotformUrl)) {
      const link = $('#external-form'); link.href = config.jotformUrl; link.target = '_blank'; link.rel = 'noopener noreferrer'; link.hidden = false;
    }
  }).catch(() => {});
  form.addEventListener('submit', async e => {
    e.preventDefault();
    if (!endpoint || sending) return;
    const phone = $('#phone'), digitCount = phone.value.replace(/\D/g,'').length;
    phone.setCustomValidity(digitCount >= 7 && digitCount <= 15 ? '' : copy.form_phone_error);
    const fileOK = validFiles();
    if (!form.reportValidity() || !fileOK) return;
    sending = true;
    const button = $('#submit-request'), status = $('#form-status');
    button.disabled = true; button.textContent = copy.form_sending; status.textContent = copy.form_sending; status.className = '';
    const data = new FormData(form); data.set('_subject','SOMI — Estimate request'); data.set('language',copy.lang);
    if (!$('#photos').files.length) data.delete('attachment');
    try {
      const response = await fetch(endpoint, {method:'POST',headers:{Accept:'application/json'},body:data,signal:AbortSignal.timeout(45000)});
      const result = await response.json();
      if (!response.ok || result.ok !== true) throw new Error('Submission not confirmed');
      status.textContent = copy.form_success; status.className = 'success';
      form.reset(); clearPreviews(); status.focus();
    } catch {
      status.textContent = copy.form_error; status.className = 'error'; status.focus();
    } finally {sending = false; button.disabled = false; button.textContent = copy.submit;}
  });
})();
