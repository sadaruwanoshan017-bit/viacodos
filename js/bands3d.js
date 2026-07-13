/* ============================================================
   VIA CODOS — 3D constellation for dark bands (landing page)
   Lightweight 2D-canvas particle field with depth (z) — drifting
   nodes, connective lines, parallax with scroll. No Three.js
   needed outside the hero; ~zero GC pressure.
   ============================================================ */
(function () {
  'use strict';
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var bands = document.querySelectorAll('.band-dark[data-p3d]');
  if (!bands.length) return;

  var SKY = '200,217,230';    /* #C8D9E6 */
  var TEAL = '86,124,141';    /* #567C8D */
  var GOLD = '201,162,75';    /* #C9A24B */

  bands.forEach(function (band) {
    var canvas = document.createElement('canvas');
    canvas.className = 'band-canvas';
    canvas.setAttribute('aria-hidden', 'true');
    band.insertBefore(canvas, band.firstChild);
    var ctx = canvas.getContext('2d');
    var DPR = Math.min(window.devicePixelRatio || 1, 2);
    var W = 0, H = 0, pts = [];
    var density = parseFloat(band.getAttribute('data-p3d')) || 1;

    function resize() {
      W = band.clientWidth; H = band.clientHeight;
      canvas.width = W * DPR; canvas.height = H * DPR;
      canvas.style.width = W + 'px'; canvas.style.height = H + 'px';
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
      var n = Math.round(Math.min(70, (W * H) / 26000) * density);
      pts = [];
      for (var i = 0; i < n; i++) {
        var z = 0.35 + Math.random() * 0.65; /* depth 0.35..1 */
        pts.push({
          x: Math.random() * W, y: Math.random() * H, z: z,
          vx: (Math.random() - 0.5) * 0.22 * z,
          vy: (Math.random() - 0.5) * 0.16 * z,
          r: (Math.random() * 1.6 + 0.7) * z,
          gold: Math.random() < 0.08
        });
      }
    }
    resize();
    window.addEventListener('resize', resize);

    var visible = false, raf = null;
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) {
        visible = en[0].isIntersecting;
        if (visible && !raf) raf = requestAnimationFrame(tick);
      }, { threshold: 0 }).observe(band);
    } else { visible = true; raf = requestAnimationFrame(tick); }

    function draw() {
      ctx.clearRect(0, 0, W, H);
      var LINK = 110;
      for (var i = 0; i < pts.length; i++) {
        var p = pts[i];
        /* links (only near depth-mates, keeps it airy) */
        for (var j = i + 1; j < pts.length; j++) {
          var q = pts[j];
          var dx = p.x - q.x, dy = p.y - q.y;
          var d2 = dx * dx + dy * dy;
          if (d2 < LINK * LINK && Math.abs(p.z - q.z) < 0.25) {
            var a = (1 - Math.sqrt(d2) / LINK) * 0.14 * p.z;
            ctx.strokeStyle = 'rgba(' + TEAL + ',' + a.toFixed(3) + ')';
            ctx.lineWidth = 1;
            ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y); ctx.stroke();
          }
        }
        var col = p.gold ? GOLD : SKY;
        ctx.fillStyle = 'rgba(' + col + ',' + (0.16 + 0.4 * p.z).toFixed(3) + ')';
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fill();
      }
    }

    function tick() {
      raf = null;
      if (!visible) return;
      if (!reduceMotion) {
        for (var i = 0; i < pts.length; i++) {
          var p = pts[i];
          p.x += p.vx; p.y += p.vy;
          if (p.x < -10) p.x = W + 10; if (p.x > W + 10) p.x = -10;
          if (p.y < -10) p.y = H + 10; if (p.y > H + 10) p.y = -10;
        }
      }
      draw();
      if (!reduceMotion) raf = requestAnimationFrame(tick);
    }
    draw(); /* static first paint (also covers reduced motion) */
    if (!reduceMotion) raf = requestAnimationFrame(tick);
  });
})();
