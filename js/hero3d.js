/* ============================================================
   VIA CODOS — Hero 3D background (Three.js r128)
   Minimal deep-space scene: layered starfield, drifting blue
   particles, faint wireframe globe. Mouse + scroll depth.
   Homepage only. Respects prefers-reduced-motion.
   ============================================================ */
(function () {
  'use strict';
  var canvas = document.getElementById('hero-canvas');
  if (!canvas || typeof THREE === 'undefined') return;

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var MOBILE = window.innerWidth < 760;
  var DPR = Math.min(window.devicePixelRatio || 1, MOBILE ? 1.5 : 2);
  var Q = MOBILE ? 0.45 : 1; /* particle budget on phones */

  var scene = new THREE.Scene();
  scene.fog = new THREE.FogExp2(0x1B2732, 0.0009);

  var camera = new THREE.PerspectiveCamera(60, 1, 1, 3000);
  camera.position.z = 420;

  var renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
  renderer.setPixelRatio(DPR);

  /* ---------- Starfield: three depth layers ---------- */
  function makeStars(count, spread, size, color, opacity) {
    var geo = new THREE.BufferGeometry();
    var pos = new Float32Array(count * 3);
    for (var i = 0; i < count * 3; i += 3) {
      pos[i]     = (Math.random() - 0.5) * spread;
      pos[i + 1] = (Math.random() - 0.5) * spread * 0.7;
      pos[i + 2] = (Math.random() - 0.5) * spread;
    }
    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    var mat = new THREE.PointsMaterial({
      color: color, size: size, transparent: true, opacity: opacity,
      depthWrite: false, blending: THREE.AdditiveBlending, sizeAttenuation: true
    });
    return new THREE.Points(geo, mat);
  }

  var starsFar  = makeStars(Math.round(900 * Q), 1900, 1.6, 0xe4edf4, 0.5);
  var starsMid  = makeStars(Math.round(500 * Q), 1400, 2.4, 0xc8d9e6, 0.6);
  var starsNear = makeStars(Math.round(180 * Q), 1000, 3.6, 0x9fbdd1, 0.75);
  scene.add(starsFar, starsMid, starsNear);

  /* ---------- Faint wireframe globe (the "bridge to talent" world) ---------- */
  var globeGroup = new THREE.Group();
  var globeGeo = new THREE.SphereGeometry(190, 28, 28);
  var globeMat = new THREE.MeshBasicMaterial({
    color: 0x567c8d, wireframe: true, transparent: true, opacity: 0.085
  });
  var globe = new THREE.Mesh(globeGeo, globeMat);
  globeGroup.add(globe);

  // Glowing nodes on the globe surface (hub points)
  var nodeGeo = new THREE.BufferGeometry();
  var NODES = 90;
  var nPos = new Float32Array(NODES * 3);
  for (var n = 0; n < NODES; n++) {
    var phi = Math.acos(2 * Math.random() - 1);
    var theta = Math.random() * Math.PI * 2;
    var r = 191;
    nPos[n * 3]     = r * Math.sin(phi) * Math.cos(theta);
    nPos[n * 3 + 1] = r * Math.cos(phi);
    nPos[n * 3 + 2] = r * Math.sin(phi) * Math.sin(theta);
  }
  nodeGeo.setAttribute('position', new THREE.BufferAttribute(nPos, 3));
  var nodes = new THREE.Points(nodeGeo, new THREE.PointsMaterial({
    color: 0xc8d9e6, size: 3.0, transparent: true, opacity: 0.75,
    depthWrite: false, blending: THREE.AdditiveBlending
  }));
  globeGroup.add(nodes);

  globeGroup.position.set(300, -20, -140);
  globeGroup.rotation.z = 0.25;
  scene.add(globeGroup);

  /* ---------- Slow drifting dust ---------- */
  var dust = makeStars(Math.round(220 * Q), 800, 2.0, 0xc9a24b, 0.22);
  scene.add(dust);

  /* ---------- Interaction state ---------- */
  var mx = 0, my = 0, tx = 0, ty = 0, scrollY = 0;
  if (!reduceMotion) {
    window.addEventListener('mousemove', function (e) {
      tx = (e.clientX / window.innerWidth - 0.5) * 2;
      ty = (e.clientY / window.innerHeight - 0.5) * 2;
    }, { passive: true });
    window.addEventListener('scroll', function () { scrollY = window.scrollY; }, { passive: true });
  }

  /* ---------- Resize ---------- */
  function resize() {
    var w = canvas.clientWidth || canvas.parentElement.clientWidth;
    var h = canvas.clientHeight || canvas.parentElement.clientHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    // Pull the globe inward on small screens so it stays visible but subtle
    globeGroup.position.x = w < 760 ? 0 : 300;
    globeGroup.position.z = w < 760 ? -260 : -140;
  }
  resize();
  window.addEventListener('resize', resize);

  /* ---------- Render loop (pauses off-screen / hidden tab) ---------- */
  var running = true;
  document.addEventListener('visibilitychange', function () {
    running = !document.hidden; if (running) requestAnimationFrame(tick);
  });
  var hero = canvas.closest('.hero');
  var visible = true;
  if ('IntersectionObserver' in window && hero) {
    new IntersectionObserver(function (en) {
      visible = en[0].isIntersecting;
      if (visible && running) requestAnimationFrame(tick);
    }, { threshold: 0 }).observe(hero);
  }

  var clock = new THREE.Clock();
  function tick() {
    if (!running || !visible) return;
    var t = clock.getElapsedTime();

    if (!reduceMotion) {
      mx += (tx - mx) * 0.035;
      my += (ty - my) * 0.035;

      starsFar.rotation.y  = t * 0.004;
      starsMid.rotation.y  = t * 0.008;
      starsNear.rotation.y = t * 0.014;
      dust.rotation.y      = -t * 0.006;
      dust.rotation.x      = Math.sin(t * 0.1) * 0.02;

      globeGroup.rotation.y = t * 0.05;
      nodes.material.opacity = 0.55 + Math.sin(t * 1.4) * 0.2;

      camera.position.x = mx * 26;
      camera.position.y = -my * 18 + scrollY * -0.06;   // scroll-driven depth
      camera.position.z = 420 + scrollY * 0.12;
      camera.lookAt(scene.position);
    } else {
      renderer.render(scene, camera);
      return; // static single frame
    }

    renderer.render(scene, camera);
    requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
})();
