/* ============================================================
   VIA CODOS — Shared UI behaviour v2
   GSAP + ScrollTrigger (with IO fallback) · nav · mega menu
   counters · video end-cards · parallax depth
   ============================================================ */
(function () {
  'use strict';
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasGsap = typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined' && !reduceMotion;
  if (hasGsap) { gsap.registerPlugin(ScrollTrigger); document.body.classList.add('gsap-on'); }

  /* ---------- Header state ---------- */
  var header = document.querySelector('.header');
  var isHome = document.body.classList.contains('page-home');
  function setHeader() {
    if (!header) return;
    var past = window.scrollY > 40;
    if (isHome) {
      header.classList.toggle('solid', past);
      header.classList.toggle('on-dark', !past);
    } else {
      header.classList.add('solid');
    }
  }
  setHeader();
  window.addEventListener('scroll', setHeader, { passive: true });

  /* ---------- Mobile nav ---------- */
  var burger = document.querySelector('.nav-burger');
  var nav = document.querySelector('.nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.classList.toggle('active', open);
      burger.setAttribute('aria-expanded', open);
      document.body.classList.toggle('nav-locked', open);
    });
  }

  /* ---------- Mega menu (touch/mobile click) ---------- */
  document.querySelectorAll('.nav-item.has-mega > .nav-link').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var mobile = window.matchMedia('(max-width:1080px)').matches;
      var touch = window.matchMedia('(hover: none)').matches;
      if (mobile || touch) {
        e.preventDefault();
        var item = link.parentElement;
        var wasOpen = item.classList.contains('open');
        document.querySelectorAll('.nav-item.open').forEach(function (o) { o.classList.remove('open'); });
        if (!wasOpen) item.classList.add('open');
      }
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav-item')) {
      document.querySelectorAll('.nav-item.open').forEach(function (o) { o.classList.remove('open'); });
    }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('.nav-item.open').forEach(function (o) { o.classList.remove('open'); });
      if (nav && nav.classList.contains('open')) {
        nav.classList.remove('open');
        if (burger) { burger.classList.remove('active'); burger.setAttribute('aria-expanded', 'false'); }
        document.body.classList.remove('nav-locked');
      }
    }
  });

  /* ---------- Scroll reveals ---------- */
  var revealEls = Array.prototype.slice.call(document.querySelectorAll('.reveal, .reveal-l, .reveal-r'));
  if (hasGsap) {
    revealEls.forEach(function (el) {
      var fromX = el.classList.contains('reveal-l') ? -46 : el.classList.contains('reveal-r') ? 46 : 0;
      var fromY = fromX === 0 ? 44 : 0;
      var delay = (parseInt(el.getAttribute('data-delay') || '0', 10)) * 0.09;
      gsap.fromTo(el,
        { opacity: 0, x: fromX, y: fromY },
        {
          opacity: 1, x: 0, y: 0, duration: 1.05, delay: delay, ease: 'power3.out',
          scrollTrigger: { trigger: el, start: 'top 88%', once: true },
          onStart: function () { el.classList.add('in'); }
        });
    });
    /* scroll-driven depth: glows, orbs, and hero media drift */
    gsap.utils.toArray('.band-glow, .orb').forEach(function (el) {
      var speed = parseFloat(el.getAttribute('data-speed') || (el.classList.contains('orb') ? '0.25' : '0.15'));
      gsap.to(el, {
        yPercent: -60 * speed * 4, ease: 'none',
        scrollTrigger: { trigger: el.parentElement, start: 'top bottom', end: 'bottom top', scrub: 0.6 }
      });
    });
    var heroMedia = document.querySelector('.hero-media');
    if (heroMedia) {
      gsap.to(heroMedia, {
        y: -46, ease: 'none',
        scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: 0.5 }
      });
      gsap.from(heroMedia, { opacity: 0, y: 60, rotateY: -10, duration: 1.4, delay: .25, ease: 'power3.out' });
    }
    /* section headings: slight rise + settle */
    gsap.utils.toArray('.section-head h2').forEach(function (h) {
      gsap.from(h, {
        y: 26, opacity: 0, duration: 1, ease: 'power3.out',
        scrollTrigger: { trigger: h, start: 'top 90%', once: true }
      });
    });
    /* case media parallax scale */
    gsap.utils.toArray('.case-media img').forEach(function (im) {
      gsap.fromTo(im, { scale: 1.12 }, {
        scale: 1, ease: 'none',
        scrollTrigger: { trigger: im, start: 'top bottom', end: 'bottom top', scrub: 0.8 }
      });
    });
  } else if ('IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- Animated counters ---------- */
  function animateCount(el) {
    var raw = el.getAttribute('data-count');
    var suffix = el.getAttribute('data-suffix') || '';
    var target = parseFloat(raw);
    if (isNaN(target) || reduceMotion) { el.textContent = Number(raw).toLocaleString() + suffix; return; }
    var dur = 1900, t0 = null;
    function frame(t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased).toLocaleString() + suffix;
      if (p < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }
  var counters = document.querySelectorAll('[data-count]');
  if ('IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { animateCount(en.target); cio.unobserve(en.target); }
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { cio.observe(el); });
  } else {
    counters.forEach(animateCount);
  }

  /* ---------- Fallback parallax (no GSAP) ---------- */
  if (!hasGsap && !reduceMotion) {
    var pEls = document.querySelectorAll('.parallax, .band-glow, .orb');
    if (pEls.length) {
      var ticking = false;
      var para = function () {
        pEls.forEach(function (el) {
          var speed = parseFloat(el.getAttribute('data-speed') || '0.12');
          var rect = el.getBoundingClientRect();
          var mid = rect.top + rect.height / 2 - window.innerHeight / 2;
          el.style.transform = 'translate3d(0,' + (-mid * speed).toFixed(1) + 'px,0)';
        });
        ticking = false;
      };
      window.addEventListener('scroll', function () {
        if (!ticking) { requestAnimationFrame(para); ticking = true; }
      }, { passive: true });
      para();
    }
  }

  /* ---------- Project videos: contact end-card ---------- */
  document.querySelectorAll('.video-wrap').forEach(function (wrap) {
    var video = wrap.querySelector('video');
    var end = wrap.querySelector('.video-end');
    if (!video || !end) return;
    video.addEventListener('ended', function () {
      end.classList.add('show');
      end.removeAttribute('hidden');
    });
    video.addEventListener('play', function () { end.classList.remove('show'); });
    var replay = wrap.querySelector('.ve-replay');
    if (replay) replay.addEventListener('click', function () {
      end.classList.remove('show');
      video.currentTime = 0;
      video.play();
    });
    video.addEventListener('error', function () {
      var badge = wrap.querySelector('.video-badge');
      if (badge) badge.textContent = 'Video coming soon';
    }, true);
  });

  /* ---------- Back to top ---------- */
  var toTop = document.getElementById('toTop');
  if (toTop) {
    window.addEventListener('scroll', function () {
      toTop.classList.toggle('show', window.scrollY > 700);
    }, { passive: true });
    toTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  }

  /* ---------- Contact form (mailto) ---------- */
  var form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = form.querySelector('#f-name').value.trim();
      var company = form.querySelector('#f-company').value.trim();
      var email = form.querySelector('#f-email').value.trim();
      var service = form.querySelector('#f-service').value;
      var msg = form.querySelector('#f-message').value.trim();
      var body = 'Name: ' + name + '\nCompany: ' + company + '\nEmail: ' + email +
                 '\nService: ' + service + '\n\n' + msg;
      window.location.href = 'mailto:info@viacodos.com?subject=' +
        encodeURIComponent('Free Consultation Request — ' + (company || name)) +
        '&body=' + encodeURIComponent(body);
    });
  }
})();
