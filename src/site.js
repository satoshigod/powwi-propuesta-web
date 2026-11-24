/* Powwi · propuesta de rediseño. Un solo guion para los dos modos de salida:
   sitio de varias páginas y archivo único con vistas internas (#nombre). */
(function () {
  var root = document.documentElement;
  var store = document.getElementById('paginas');
  var data = store ? JSON.parse(store.textContent) : null;
  var app = document.getElementById('app');
  var actual = null; // vista visible en el archivo único
  var ancla = null;  // sección a la que hay que bajar al cambiar de vista

  function selectTab(tab) {
    var tabs = tab.closest('[role=tablist]').querySelectorAll('[role=tab]');
    for (var i = 0; i < tabs.length; i++) {
      var on = tabs[i] === tab;
      tabs[i].setAttribute('aria-selected', on);
      tabs[i].tabIndex = on ? 0 : -1;
      var panel = document.getElementById(tabs[i].getAttribute('aria-controls'));
      if (panel) panel.hidden = !on;
    }
    tab.focus();
  }

  // Al cambiar de vista el salto es inmediato; el desplazamiento suave queda para las anclas.
  function arriba() {
    try { window.scrollTo({ top: 0, left: 0, behavior: 'instant' }); } catch (e) { window.scrollTo(0, 0); }
  }

  function scrollToId(id, alInstante) {
    var el = document.getElementById(id);
    if (!el) return false;
    try { el.scrollIntoView(alInstante ? { behavior: 'instant', block: 'start' } : true); } catch (e) { el.scrollIntoView(); }
    if (!el.hasAttribute('tabindex')) el.setAttribute('tabindex', '-1');
    el.focus({ preventScroll: true });
    return true;
  }

  function mostrar(nombre) {
    var pg = data.paginas[nombre];
    app.innerHTML = pg.html;
    document.title = pg.title;
    root.lang = pg.lang;
    actual = nombre;
    var id = ancla;
    ancla = null;
    if (!(id && scrollToId(id, true))) arriba();
  }

  function ruta() {
    var nombre = location.hash.slice(1);
    if (!nombre) nombre = data.inicio;
    if (!data.paginas[nombre]) {            // nombre ajeno al sitio: se conserva la vista
      if (actual) return;
      nombre = data.inicio;
    }
    if (nombre !== actual) mostrar(nombre);
  }

  document.addEventListener('click', function (e) {
    var t = e.target.closest('.menu-btn');
    if (t) {
      var abierta = t.closest('.hdr').classList.toggle('open');
      t.setAttribute('aria-expanded', abierta);
      return;
    }
    t = e.target.closest('[role=tab]');
    if (t) { selectTab(t); return; }
    var panel = document.querySelector('.junta[open]');
    if (panel && !e.target.closest('.junta')) panel.removeAttribute('open');
    if (!data) return;

    var link = e.target.closest('a[href^="#"]');
    if (!link || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var nombre = link.getAttribute('href').slice(1);
    e.preventDefault();
    if (!link.hasAttribute('data-v')) { scrollToId(nombre); return; }  // ancla de la misma página
    ancla = link.getAttribute('data-frag');
    if (nombre === actual) {
      var id = ancla;
      ancla = null;
      var hdr = document.querySelector('.hdr.open');
      if (hdr) hdr.classList.remove('open');
      if (!(id && scrollToId(id))) arriba();
    } else {
      mostrar(nombre);
    }
    if (location.hash.slice(1) !== nombre) location.hash = nombre;
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      var abierto = document.querySelector('.junta[open]');
      if (abierto) { abierto.removeAttribute('open'); abierto.querySelector('summary').focus(); }
    }
    var tab = e.target.closest && e.target.closest('[role=tab]');
    if (!tab || (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft')) return;
    var tabs = Array.prototype.slice.call(tab.closest('[role=tablist]').querySelectorAll('[role=tab]'));
    var i = tabs.indexOf(tab) + (e.key === 'ArrowRight' ? 1 : -1);
    selectTab(tabs[(i + tabs.length) % tabs.length]);
    e.preventDefault();
  });

  // Prototipo: ningún formulario envía datos.
  document.addEventListener('submit', function (e) { e.preventDefault(); });

  if (data) {
    window.addEventListener('hashchange', ruta);
    ruta();
  }
})();
