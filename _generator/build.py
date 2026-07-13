# -*- coding: utf-8 -*-
"""Via Codos — static site generator. Generates all pages into the project folder."""
import os
from data import SERVICES, INDUSTRIES, CASE_STUDIES, INSIGHTS, TEAM, JOBS

import pathlib
OUT = str(pathlib.Path(__file__).resolve().parent.parent)  # project root

# ----------------------------------------------------------------- icons
def svg(paths, vb="0 0 24 24"):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s" fill="none" '
            'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">%s</svg>' % (vb, paths))

I = {
 "arrow": svg('<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>'),
 "up": svg('<path d="m5 12 7-7 7 7"/><path d="M12 19V5"/>'),
 "chev": svg('<path d="m6 9 6 6 6-6"/>'),
 "chevr": svg('<path d="m9 18 6-6-6-6"/>'),
 "users": svg('<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>'),
 "code": svg('<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>'),
 "layers": svg('<path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>'),
 "globe": svg('<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>'),
 "smartphone": svg('<rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/>'),
 "pen": svg('<path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/>'),
 "cpu": svg('<rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/>'),
 "cloud": svg('<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/>'),
 "shield": svg('<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1 1 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>'),
 "flask": svg('<path d="M10 2v7.527a2 2 0 0 1-.211.896L4.72 20.55a1 1 0 0 0 .9 1.45h12.76a1 1 0 0 0 .9-1.45l-5.069-10.127A2 2 0 0 1 14 9.527V2"/><path d="M8.5 2h7"/><path d="M7 16h10"/>'),
 "chart": svg('<path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>'),
 "building": svg('<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4"/><path d="M10 10h4"/><path d="M10 14h4"/><path d="M10 18h4"/>'),
 "car": svg('<path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/>'),
 "heart": svg('<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/><path d="M3.22 12H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27"/>'),
 "cart": svg('<circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/>'),
 "factory": svg('<path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/><path d="M17 18h1"/><path d="M12 18h1"/><path d="M7 18h1"/>'),
 "truck": svg('<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>'),
 "grad": svg('<path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>'),
 "plane": svg('<path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/>'),
 "bank": svg('<line x1="3" x2="21" y1="22" y2="22"/><line x1="6" x2="6" y1="18" y2="11"/><line x1="10" x2="10" y1="18" y2="11"/><line x1="14" x2="14" y1="18" y2="11"/><line x1="18" x2="18" y1="18" y2="11"/><polygon points="12 2 20 7 4 7"/>'),
 "bell": svg('<path d="M3 20a1 1 0 0 1-1-1v-1a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v1a1 1 0 0 1-1 1Z"/><path d="M20 16a8 8 0 1 0-16 0"/><path d="M12 4v4"/><path d="M10 4h4"/>'),
 "briefcase": svg('<path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/><rect width="20" height="14" x="2" y="6" rx="2"/>'),
 "network": svg('<rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/><path d="M12 12V8"/>'),
 "mail": svg('<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>'),
 "phone": svg('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>'),
 "pin": svg('<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>'),
 "zap": svg('<path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/>'),
 "monitor": svg('<rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/>'),
 "wrench": svg('<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>'),
 "lock": svg('<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>'),
 "message": svg('<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>'),
 "tagicon": svg('<path d="M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42z"/><circle cx="7.5" cy="7.5" r=".5" fill="currentColor"/>'),
 "award": svg('<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/>'),
 "check": svg('<path d="M21.801 10A10 10 0 1 1 17 3.335"/><path d="m9 11 3 3L22 4"/>'),
 "target": svg('<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>'),
 "trend": svg('<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>'),
 "eye": svg('<path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/>'),
 "alert": svg('<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>'),
 "book": svg('<path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H19a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H6.5a1 1 0 0 1 0-5H20"/>'),
 "wa": ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164'
        '-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606'
        '.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207'
        '-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462'
        '1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118'
        '.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004'
        'a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884'
        '2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0'
        'C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005'
        'c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>'),
}

WA_LINK = "https://wa.me/94721980060"

# ----------------------------------------------------------------- chrome
def head(title, desc, p, home=False):
    three = ('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js" defer></script>\n'
             '<script src="%sjs/hero3d.js" defer></script>' % p) if home else ""
    fav = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='14' fill='%232563EB'/%3E"
           "%3Ctext x='32' y='44' font-family='Arial,sans-serif' font-weight='800' font-size='34' fill='white' text-anchor='middle'%3EV%3C/text%3E%3C/svg%3E")
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:type" content="website">
<link rel="icon" href="%s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="%scss/style.css">
%s
</head>
""" % (title, desc.replace('"','&quot;'), title, desc.replace('"','&quot;'), fav, p, three)

def mega_link(href, icon, label):
    return '<a href="%s">%s<span>%s</span></a>' % (href, I.get(icon, ""), label)

def header(p, home=False):
    sv_cols = {"Build": [], "Run & Scale": [], "Talent & Intelligence": []}
    for s in SERVICES:
        sv_cols[s["group"]].append(mega_link(p + "services/" + s["slug"] + ".html", s["icon"], s["name"]))
    ind_links = [mega_link(p + "industries/" + i["slug"] + ".html", i["icon"], i["name"]) for i in INDUSTRIES]
    half = 6
    why_links = [
        mega_link(p + "why/why-us.html", "award", "Why Us"),
        mega_link(p + "why/sri-lanka-advantage.html", "globe", "The Sri Lanka Advantage"),
        mega_link(p + "why/how-we-work.html", "target", "How We Work"),
        mega_link(p + "why/our-promise.html", "check", "Our Promise"),
    ]
    co_links = [
        mega_link(p + "company/about.html", "building", "About Us"),
        mega_link(p + "company/team.html", "users", "Our Team"),
        mega_link(p + "company/careers.html", "briefcase", "Careers"),
        mega_link(p + "portfolio/index.html", "layers", "Portfolio & Case Studies"),
        mega_link(p + "contact.html", "mail", "Contact Us"),
    ]
    cls = "header on-dark" if home else "header solid"
    return """<a class="skip-link" href="#main">Skip to main content</a>
<header class="%s">
 <div class="header-inner">
  <a class="logo" href="%sindex.html" aria-label="Via Codos — home">
   <span class="logo-mark">V</span><span>Via&nbsp;<em>Codos</em></span>
  </a>
  <button class="nav-burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  <nav class="nav" aria-label="Primary">
   <div class="nav-item has-mega">
    <button class="nav-link" type="button">Industries %s</button>
    <div class="mega mega-cols-2">
     <div class="mega-col"><h5>Industries</h5>%s</div>
     <div class="mega-col"><h5>&nbsp;</h5>%s</div>
     <div class="mega-foot">Not sure where your business fits? <a href="%scontact.html">Talk to us →</a></div>
    </div>
   </div>
   <div class="nav-item has-mega">
    <button class="nav-link" type="button">Services %s</button>
    <div class="mega mega-cols-3">
     <div class="mega-col"><h5>Build</h5>%s</div>
     <div class="mega-col"><h5>Run &amp; Scale</h5>%s</div>
     <div class="mega-col"><h5>Talent &amp; Intelligence</h5>%s</div>
     <div class="mega-foot">Eleven service lines, one accountable partner. <a href="%sservices/index.html">View all services →</a></div>
    </div>
   </div>
   <div class="nav-item has-mega">
    <button class="nav-link" type="button">Why Via Codos %s</button>
    <div class="mega"><div class="mega-col"><h5>Why Via Codos</h5>%s</div></div>
   </div>
   <div class="nav-item has-mega">
    <button class="nav-link" type="button">Company %s</button>
    <div class="mega"><div class="mega-col"><h5>Company</h5>%s</div></div>
   </div>
   <div class="nav-item"><a class="nav-link" href="%sinsights/index.html">Insights</a></div>
   <div class="nav-cta"><a class="btn btn-primary btn-sm" href="%scontact.html">Book a Free Consultation %s</a></div>
  </nav>
 </div>
</header>
""" % (cls, p, I["chev"], "".join(ind_links[:half]), "".join(ind_links[half:]), p,
       I["chev"], "".join(sv_cols["Build"]), "".join(sv_cols["Run & Scale"]),
       "".join(sv_cols["Talent & Intelligence"]), p,
       I["chev"], "".join(why_links), I["chev"], "".join(co_links), p, p, I["arrow"])

def footer(p):
    ind = "".join('<a href="%sindustries/%s.html">%s</a>' % (p, i["slug"], i["name"]) for i in INDUSTRIES)
    srv = "".join('<a href="%sservices/%s.html">%s</a>' % (p, s["slug"], s["name"]) for s in SERVICES)
    return """<footer class="footer">
 <div class="container">
  <div class="footer-top">
   <div class="footer-brand">
    <a class="logo" href="%sindex.html"><span class="logo-mark">V</span><span>Via&nbsp;<em>Codos</em></span></a>
    <p>We take care of your IT. So you may focus on your business, with peace of mind.</p>
    <div class="footer-contact">
     <div>%s &nbsp;Galle, Ginthota, Sri Lanka</div>
     <div>%s &nbsp;<a href="tel:+94769047552">+94 76 904 7552</a></div>
     <div>%s &nbsp;<a href="mailto:info@viacodos.com">info@viacodos.com</a></div>
    </div>
   </div>
   <div class="footer-col"><h5>Industries</h5>%s</div>
   <div class="footer-col"><h5>Services</h5>%s</div>
   <div class="footer-col"><h5>Company</h5>
    <a href="%scompany/about.html">About Us</a>
    <a href="%scompany/team.html">Our Team</a>
    <a href="%scompany/careers.html">Careers</a>
    <a href="%scontact.html">Contact Us</a>
    <a href="%scontact.html">Get a Quote</a>
   </div>
   <div class="footer-col"><h5>Resources</h5>
    <a href="%sportfolio/index.html">Portfolio &amp; Case Studies</a>
    <a href="%sinsights/index.html">Insights / Blog</a>
    <a href="%swhy/why-us.html">Why Via Codos</a>
    <a href="%swhy/sri-lanka-advantage.html">The Sri Lanka Advantage</a>
    <a href="%slegal/nda-security.html">NDA &amp; Security Commitment</a>
   </div>
  </div>
  <div class="footer-bottom">
   <span>© 2026 Via Codos Private Limited. All rights reserved.</span>
   <div class="footer-legal">
    <a href="%slegal/privacy-policy.html">Privacy Policy</a>
    <a href="%slegal/terms-of-service.html">Terms of Service</a>
    <a href="%slegal/nda-security.html">NDA &amp; Security Commitment</a>
   </div>
  </div>
 </div>
</footer>
<button id="toTop" aria-label="Back to top">%s</button>
<a class="wa-float" href="%s" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">%s</a>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
<script src="%sjs/main.js" defer></script>
</body>
</html>""" % (p, I["pin"], I["phone"], I["mail"], ind, srv, p, p, p, p, p, p, p, p, p, p,
              p, p, p, I["up"], WA_LINK, I["wa"], p)

def page_hero(p, crumb, tagline, h1, lead=""):
    crumbs = ['<a href="%sindex.html">Home</a>' % p]
    for label, href in crumb[:-1]:
        crumbs.append(I["chevr"])
        crumbs.append('<a href="%s">%s</a>' % (href, label))
    crumbs.append(I["chevr"])
    crumbs.append('<span class="cur">%s</span>' % crumb[-1][0])
    lead_html = '<p class="lead reveal" data-delay="2">%s</p>' % lead if lead else ""
    return """<section class="page-hero">
 <div class="container">
  <nav class="breadcrumb" aria-label="Breadcrumb">%s</nav>
  <span class="eyebrow reveal">%s</span>
  <h1 class="reveal" data-delay="1">%s</h1>
  %s
 </div>
</section>
""" % ("".join(crumbs), tagline, h1, lead_html)

def cta_band(p, title="Ready to Build Your Dream Team?",
             sub="Get started with a free consultation today. No obligation, just expert advice from people who have done this before.",
             btn="Get a Free Consultation"):
    return """<section class="band-dark cta-band">
 <div class="band-glow" style="width:520px;height:520px;background:rgba(86,124,141,.32);top:-260px;left:50%%;transform:translateX(-50%%)"></div>
 <div class="container">
  <h2 class="reveal">%s</h2>
  <p class="sub reveal" data-delay="1">%s</p>
  <div class="reveal" data-delay="2"><a class="btn btn-primary" href="%scontact.html">%s %s</a></div>
 </div>
</section>
""" % (title, sub, p, btn, I["arrow"])

def write(path, html):
    lp = "../" if "/" in path else ""
    html = html.replace('<span class="logo-mark">V</span>',
        '<span class="logo-mark"><img src="%sassets/logo.png" alt=""></span>' % lp)
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("  +", path)

def body_open(home=False):
    return '<body class="%s">\n' % ("page-home" if home else "page-inner")

# ----------------------------------------------------------------- HOME
def build_home():
    p = ""
    sv_cards = ""
    for n, s in enumerate(SERVICES):
        sv_cards += """<a class="card reveal" data-delay="%d" href="services/%s.html">
 <div class="icon-badge">%s</div><h3>%s</h3><p>%s</p>
 <span class="link-arrow">Learn more %s</span></a>""" % (
            n % 3 + 1, s["slug"], I[s["icon"]], s["name"], s["oneliner"], I["arrow"])
    chips = "".join('<a class="chip reveal" data-delay="%d" href="industries/%s.html">%s%s</a>' %
                    (n % 5 + 1, i["slug"], I[i["icon"]], i["name"]) for n, i in enumerate(INDUSTRIES[:10]))
    cases = ""
    for n, c in enumerate(CASE_STUDIES):
        cases += """<a class="card case-card reveal" data-delay="%d" href="portfolio/%s.html">
 <div class="case-media"><span class="ph">%s</span>
  <img src="assets/%s" alt="%s screenshot" loading="lazy" onerror="this.style.display='none'"></div>
 <div class="case-body"><span class="case-tag">%s</span><h3>%s</h3>
  <div class="case-metric">%s</div>
  <span class="link-arrow">Read the case study %s</span></div></a>""" % (
            n + 1, c["slug"], c["name"], c["image"], c["name"], c["sector"], c["name"], c["headline"], I["arrow"])
    steps = [
        ("zap", "Quick Response", "We respond to every inquiry within 12 seconds during business hours, and within one business day outside them."),
        ("monitor", "Remote Resolution", "Our teams remote in and resolve the majority of issues without ever needing an on-site visit."),
        ("wrench", "On-Site Support", "If a problem genuinely requires a physical presence, we coordinate on-site support rather than leaving you stuck."),
        ("lock", "Security First", "Every engagement begins under NDA, with responsibility for your data security and backup built into how we work, not added as an afterthought."),
    ]
    steps_html = "".join("""<div class="card step-card reveal" data-delay="%d">
 <div class="step-num">0%d</div><div class="icon-badge">%s</div><h3>%s</h3><p>%s</p></div>""" %
                         (n + 1, n + 1, I[ic], t, d) for n, (ic, t, d) in enumerate(steps))
    promises = [
        ("message", "No Tech Talk", "We will never use technical jargon to talk over your head or obscure what we're actually doing."),
        ("tagicon", "No Haggling", "We offer one fair, transparent price with no hidden fees and no scope-creep surprises."),
        ("award", "Satisfaction Guarantee", "Everything we deliver is backed by a 100% satisfaction guarantee."),
    ]
    promises_html = "".join("""<div class="card reveal" data-delay="%d">
 <div class="icon-badge">%s</div><h3>%s</h3><p>%s</p></div>""" %
                            (n + 1, I[ic], t, d) for n, (ic, t, d) in enumerate(promises))

    html = head("Via Codos | IT Outsourcing, Custom Software & AI Solutions",
                "Connect with pre-vetted software engineers, AI specialists, and full-stack developers at 40-70% cost savings. Custom software, ERP, AI automation, and IT outsourcing from Sri Lanka's top tech talent.",
                p, home=True)
    html += body_open(home=True)
    html += header(p, home=True)
    html += """<main id="main">
<section class="hero">
 <canvas id="hero-canvas" aria-hidden="true"></canvas>
 <div class="container">
  <div class="hero-grid">
  <div class="hero-content">
   <span class="eyebrow reveal in">Global IT Solutions Provider</span>
   <h1 class="reveal in">Your Bridge to <span class="grad">Sri Lanka's Top Tech&nbsp;Talent</span></h1>
   <p class="lead reveal in">Connect with pre-vetted software engineers, AI specialists, and full-stack developers at 40-70%% cost savings. From startups to enterprises, build your dream team with Via Codos — without the recruitment overhead, the visa paperwork, or the guesswork.</p>
   <div class="hero-ctas reveal in">
    <a class="btn btn-primary" href="contact.html">Get a Free Consultation %s</a>
    <a class="btn btn-outline-light" href="services/index.html">Explore Services %s</a>
   </div>
   <div class="hero-trust reveal in">
    <div><b data-count="500" data-suffix="+">500+</b><span>Projects Completed</span></div>
    <div><b data-count="200" data-suffix="+">200+</b><span>Businesses worldwide trust us</span></div>
    <div><b data-count="100" data-suffix="+">100+</b><span>Pre-vetted engineers ready to deploy</span></div>
   </div>
  </div>
  <div class="hero-media">
   <div class="frame">
    <img src="assets/hero-image.jpg" alt="Via Codos engineering team collaborating" onerror="this.closest('.hero-media').style.display='none'">
   </div>
   <div class="hero-chip">
    <div class="icon-badge"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg></div>
    <div><b>40-70%%</b><span>Typical cost savings</span></div>
   </div>
  </div>
  </div>
 </div>
 <div class="hero-scroll" aria-hidden="true"></div>
</section>

<section class="band-dark strip grain" data-p3d="1">
 <div class="band-glow" style="width:420px;height:420px;background:rgba(86,124,141,.3);top:-180px;right:-100px"></div>
 <div class="orb" data-speed="0.3" style="width:240px;height:240px;right:5%%;top:-70px"></div>
 <div class="orb orb-gold" data-speed="0.5" style="width:130px;height:130px;left:3%%;bottom:-40px"></div>
 <div class="container strip-inner">
  <p class="reveal">Engineering talent and AI solutions built specifically for <em>how your industry actually runs</em> — not generic outsourcing, and not off-the-shelf software.</p>
  <a class="btn btn-outline-light reveal" data-delay="1" href="industries/index.html">Explore Industries %s</a>
 </div>
</section>

<section class="section">
 <div class="container">
  <div class="section-head center reveal">
   <span class="tagline">How We Work</span>
   <h2>Our IT Outsourcing Process</h2>
   <p class="sub">We're committed to providing the very best service for every client, from first inquiry to long-term partnership.</p>
  </div>
  <div class="grid grid-4">%s</div>
 </div>
</section>

<section class="section section-alt">
 <div class="container">
  <div class="section-head center reveal">
   <span class="tagline">Our Promise</span>
   <h2>Our IT Outsourcing Promise to You</h2>
  </div>
  <div class="grid grid-3">%s</div>
 </div>
</section>

<section class="section">
 <div class="container">
  <div class="section-head reveal">
   <span class="tagline">Our Services</span>
   <h2>Comprehensive IT Services</h2>
   <p class="sub">Eleven core service lines, one accountable partner.</p>
  </div>
  <div class="grid grid-3">%s</div>
  <div style="text-align:center;margin-top:48px" class="reveal">
   <a class="btn btn-primary" href="services/index.html">View All Services %s</a>
  </div>
 </div>
</section>

<section class="band-dark section grain" data-p3d="0.9">
 <div class="band-glow" style="width:500px;height:500px;background:rgba(200,217,230,.14);bottom:-260px;left:-140px"></div>
 <div class="container">
  <div class="section-head center reveal">
   <span class="tagline">Industries We Serve</span>
   <h2>Built for How Your Industry Runs</h2>
   <p class="sub">Industry-specific credibility sells outsourcing better than a generic capability list — because generic software solves generic problems.</p>
  </div>
  <div class="chip-grid">%s</div>
  <div style="text-align:center;margin-top:44px" class="reveal">
   <a class="btn btn-outline-light" href="industries/index.html">All Industries %s</a>
  </div>
 </div>
</section>

<section class="section section-alt">
 <div class="container">
  <div class="section-head reveal">
   <span class="tagline">Featured Work</span>
   <h2>Flagship Products, Real Results</h2>
   <p class="sub">Four products we designed, built, and still run in production today.</p>
  </div>
  <div class="grid grid-2">%s</div>
 </div>
</section>

<section class="band-dark section grain" data-p3d="0.9">
 <div class="band-glow" style="width:600px;height:600px;background:rgba(200,217,230,.12);top:-300px;left:50%%;transform:translateX(-50%%)"></div>
 <div class="container">
  <div class="orb" data-speed="0.35" style="width:300px;height:300px;right:-80px;bottom:-100px"></div>
  <div class="orb orb-gold" data-speed="0.55" style="width:110px;height:110px;left:6%%;top:-30px"></div>
  <div class="section-head center reveal">
   <span class="tagline">The Sri Lanka Advantage</span>
   <h2>The Numbers Behind the Talent</h2>
  </div>
  <div class="stats-grid">
   <div class="stat reveal"><b data-count="150000" data-suffix="+">150,000+</b><span>Active Software Engineers in Sri Lanka</span></div>
   <div class="stat reveal" data-delay="1"><b data-count="100000" data-suffix="+">100,000+</b><span>STEM Graduates Annually</span></div>
   <div class="stat reveal" data-delay="2"><b data-count="90" data-suffix="%%+">90%%+</b><span>Literacy Rate with Business English</span></div>
   <div class="stat reveal" data-delay="3"><b>40-70%%</b><span>Typical Cost Savings</span></div>
  </div>
 </div>
</section>
%s
</main>
""" % (I["arrow"], I["arrow"], I["arrow"], steps_html, promises_html, sv_cards,
       I["arrow"], chips, I["arrow"], cases,
       cta_band(p))
    html += footer(p)
    html = html.replace("</body>", '<script src="js/bands3d.js" defer></script>\n</body>')
    write("index.html", html)

# ----------------------------------------------------------------- SERVICES
def build_services():
    p = "../"
    # overview
    groups = [("Build", "What we design and engineer from the ground up."),
              ("Run & Scale", "What keeps your systems reliable, tested, and informed as you grow."),
              ("Talent & Intelligence", "The people and the AI that extend your team's capacity.")]
    sections = ""
    for gname, gdesc in groups:
        cards = ""
        for n, s in enumerate([x for x in SERVICES if x["group"] == gname]):
            cards += """<a class="card reveal" data-delay="%d" href="%s.html">
 <div class="icon-badge">%s</div><h3>%s</h3><p>%s</p>
 <span class="link-arrow">Learn more %s</span></a>""" % (n + 1, s["slug"], I[s["icon"]], s["name"], s["oneliner"], I["arrow"])
        sections += """<div class="section-head reveal" style="margin-top:56px">
 <span class="tagline">%s</span><h2 style="font-size:28px">%s</h2></div>
<div class="grid grid-3">%s</div>""" % (gname, gdesc, cards)
    html = head("IT Services | Via Codos",
                "From custom software to AI automation, explore all 11 Via Codos service lines — IT outsourcing, ERP, web and mobile development, cloud, security, QA, and data engineering.", p)
    html += body_open() + header(p)
    html += page_hero(p, [("Services", "index.html")], "Our Services",
                      "Comprehensive IT Solutions",
                      "From custom development to AI-powered automation, we deliver enterprise-grade solutions that drive growth, efficiency, and innovation — eleven service lines, one accountable partner.")
    html += '<main id="main"><section class="section" style="padding-top:70px"><div class="container">%s</div></section>%s</main>' % (
        sections, cta_band(p, "Need a custom solution?", "Let's discuss your requirements — no obligation, just expert advice.", "Talk to Us"))
    html += footer(p)
    write("services/index.html", html)

    for s in SERVICES:
        related = [x for x in SERVICES if x["group"] == s["group"] and x["slug"] != s["slug"]][:3]
        rel_html = "".join('<a href="%s.html">%s %s</a>' % (r["slug"], r["name"], I["chevr"]) for r in related)
        paras = "".join("<p>%s</p>" % b for b in s["body"])
        inc = "".join("<li>%s</li>" % x for x in s["included"])
        html = head(s["meta_title"], s["meta_desc"], p)
        html += body_open() + header(p)
        html += page_hero(p, [("Services", "index.html"), (s["name"], "#")], s["tagline"], s["name"], s["oneliner"])
        html += """<main id="main"><section class="section"><div class="container detail-layout">
 <div class="prose reveal">%s
  <h2>What's Included</h2><ul>%s</ul>
 </div>
 <aside class="aside-card reveal-r">
  <div class="aside-stat"><b>%s</b><span>%s</span></div>
  <h4>Start the conversation</h4>
  <p>Tell us what you're trying to build or fix — we'll respond fast, under NDA, with a clear next step.</p>
  <a class="btn btn-primary" href="%scontact.html">Get a Free Consultation %s</a>
  <div class="aside-links"><h5>Related services</h5>%s</div>
 </aside>
</div></section>%s</main>""" % (paras, inc, s["stat"][0], s["stat"][1], p, I["arrow"], rel_html, cta_band(p))
        html += footer(p)
        write("services/%s.html" % s["slug"], html)

# ----------------------------------------------------------------- INDUSTRIES
def build_industries():
    p = "../"
    cards = ""
    for n, i in enumerate(INDUSTRIES):
        cards += """<a class="card reveal" data-delay="%d" href="%s.html">
 <div class="icon-badge">%s</div><h3>%s</h3><p>%s</p>
 <span class="link-arrow">Explore solutions %s</span></a>""" % (
            n % 3 + 1, i["slug"], I[i["icon"]], i["name"], i["intro"][:150].rsplit(" ", 1)[0] + "…", I["arrow"])
    html = head("Industries We Serve | Via Codos",
                "Via Codos delivers industry-specific software and outsourcing solutions across real estate, automotive, healthcare, retail, manufacturing, logistics, education, travel, finance, and hospitality.", p)
    html += body_open() + header(p)
    html += page_hero(p, [("Industries", "index.html")], "Industries",
                      "Solutions for Every Industry",
                      "We deliver industry-specific solutions designed to address unique challenges, drive efficiency, and unlock new opportunities for growth. Generic software solves generic problems — our teams build with your industry's specific operational realities in mind from the first requirements conversation.")
    html += '<main id="main"><section class="section"><div class="container"><div class="grid grid-3">%s</div></div></section>%s</main>' % (
        cards, cta_band(p, "Looking for industry-specific solutions?", "Let's talk about the operational realities of your business — and the software that should match them.", "Let's Talk"))
    html += footer(p)
    write("industries/index.html", html)

    for i in INDUSTRIES:
        ch = "".join("<li>%s</li>" % c for c in i["challenges"])
        so = "".join("<li>%s</li>" % s for s in i["solutions"])
        html = head(i["meta_title"], i["intro"][:158], p)
        html += body_open() + header(p)
        html += page_hero(p, [("Industries", "index.html"), (i["name"], "#")], "Industry", i["name"], i["intro"])
        html += """<main id="main"><section class="section"><div class="container">
 <div class="duo">
  <div class="panel panel-challenge reveal-l"><h3>%s Common Challenges We Solve</h3><ul>%s</ul></div>
  <div class="panel panel-solution reveal-r"><h3>%s Solutions We Deliver</h3><ul>%s</ul></div>
 </div>
</div></section>%s</main>""" % (I["alert"], ch, I["check"], so, cta_band(p))
        html += footer(p)
        write("industries/%s.html" % i["slug"], html)

# ----------------------------------------------------------------- WHY GROUP
def build_why():
    p = "../"
    # Why Us
    feats = [
        ("Top 1% Talent Pool", "We recruit from the top percentile of Sri Lankan graduates and certification holders. Our rigorous vetting process includes technical assessments, behavioural interviews, and real-world coding challenges — the same bar you'd hold an in-house senior hire to.", "100+", "Pre-vetted Engineers", "award"),
        ("40-70% Cost Savings", "Significant cost reduction compared to onshore hiring in the USA, UK, or Australia. You get the same quality of talent at a fraction of the cost, because the savings come from cost-of-living economics, not from lower standards.", "$15,000+", "Average savings per engineer, per month", "trend"),
        ("Global Experience", "We have successfully served clients across the USA, UK, Australia, Dubai, South Africa, and beyond. We understand the practical nuances of working with international teams — timezone overlap, communication cadence, and cultural context included.", "200+", "Clients Worldwide", "globe"),
        ("Security & Compliance", "NDA-first discipline in handling client code, credentials, and sensitive data. We follow industry-standard security practices and ensure complete confidentiality on every engagement, regardless of size.", "100%", "NDA Compliance", "shield"),
    ]
    cards = ""
    for n, (t, d, st, sl, ic) in enumerate(feats):
        cards += """<div class="card reveal" data-delay="%d"><div class="step-num">0%d</div>
 <div class="icon-badge">%s</div><h3>%s</h3><p>%s</p>
 <div class="case-metric"><b style="font-size:22px;font-family:var(--font-head)">%s</b> — %s</div></div>""" % (
            n % 2 + 1, n + 1, I[ic], t, d, st, sl)
    html = head("Why Via Codos | Your Strategic Technology Advantage",
                "Discover why leading companies choose Via Codos: top 1% Sri Lankan talent, 40-70% cost savings, global experience, and NDA-first security.", p)
    html += body_open() + header(p)
    html += page_hero(p, [("Why Via Codos", "why-us.html")], "Why Via Codos", "Your Strategic Advantage",
                      "Discover why leading companies choose Via Codos as their trusted technology partner — and why \"outsourcing\" doesn't have to mean the compromises it once did.")
    html += '<main id="main"><section class="section"><div class="container"><div class="grid grid-2">%s</div></div></section>%s</main>' % (cards, cta_band(p))
    html += footer(p)
    write("why/why-us.html", html)

    # Sri Lanka Advantage
    blocks = [
        ("A Growing, Diversifying Talent Pool", "Sri Lanka's software engineering workforce has grown steadily as the country has invested heavily in STEM education. That growth means a genuinely deep bench across specialisations — from mobile and web engineering to AI/ML and DevOps — rather than a narrow pool concentrated in one skill set.", "trend"),
        ("Fresh Talent, Every Year", "Over 100,000 STEM graduates enter the Sri Lankan workforce annually, giving Via Codos continuous access to newly trained talent alongside experienced senior engineers, and giving our clients a pipeline that doesn't dry up as demand grows.", "grad"),
        ("A Business-English Standard", "With a literacy rate exceeding 90% and English taught as a core subject from an early age, communication friction — the single biggest hidden cost in many outsourcing relationships — is dramatically reduced.", "message"),
    ]
    bl = "".join("""<div class="card reveal" data-delay="%d"><div class="icon-badge">%s</div><h3>%s</h3><p>%s</p></div>""" %
                 (n + 1, I[ic], t, d) for n, (t, d, ic) in enumerate(blocks))
    html = head("The Sri Lanka Advantage | Via Codos",
                "Sri Lanka is one of the fastest-growing tech hubs in the world. Learn why 150,000+ engineers, business-fluent English, and a strong education culture make it the smart choice for IT outsourcing.", p)
    html += body_open() + header(p)
    html += page_hero(p, [("Why Via Codos", "why-us.html"), ("The Sri Lanka Advantage", "#")],
                      "The Sri Lanka Advantage", "One of the World's Fastest-Growing Tech Hubs",
                      "Sri Lanka is recognised as one of the fastest-growing tech hubs in the world, with a strong culture of education, innovation, and technical excellence. Here is the \"why this country\" answer, before you even ask it.")
    html += """<main id="main">
<section class="band-dark" style="padding:64px 0">
 <div class="container stats-grid">
  <div class="stat reveal"><b data-count="150000" data-suffix="+">150,000+</b><span>Active Software Engineers</span></div>
  <div class="stat reveal" data-delay="1"><b data-count="100000" data-suffix="+">100,000+</b><span>STEM Graduates Annually</span></div>
  <div class="stat reveal" data-delay="2"><b data-count="90" data-suffix="%%+">90%%+</b><span>Business-Fluent English Literacy Rate</span></div>
  <div class="stat reveal" data-delay="3"><b>40-70%%</b><span>Typical Cost Savings</span></div>
 </div>
</section>
<section class="section"><div class="container"><div class="grid grid-3">%s</div></div></section>%s</main>""" % (bl, cta_band(p))
    html += footer(p)
    write("why/sri-lanka-advantage.html", html)

    # How We Work
    steps = [
        ("Quick Response", "Every inquiry receives an initial response within 12 seconds during business hours. Speed at first contact sets the tone for everything that follows.", "zap"),
        ("Remote Resolution", "The large majority of technical issues and delivery tasks are handled remotely, by design — this keeps costs down and turnaround fast without sacrificing quality.", "monitor"),
        ("On-Site Support", "When something genuinely requires a physical presence, we coordinate on-site support rather than forcing a remote workaround that won't actually solve the problem.", "wrench"),
        ("Security First", "We take direct responsibility for the security and backup of your data throughout the engagement — this isn't an add-on service, it's baked into how every project is scoped from day one.", "lock"),
    ]
    st = "".join("""<div class="card step-card reveal" data-delay="%d"><div class="step-num">Step %d</div>
 <div class="icon-badge">%s</div><h3>%s</h3><p>%s</p></div>""" %
                 (n % 2 + 1, n + 1, I[ic], t, d) for n, (t, d, ic) in enumerate(steps))
    html = head("How We Work | Via Codos IT Outsourcing Process",
                "See exactly how Via Codos delivers: 12-second response times, remote-first resolution, on-site support when needed, and security-first data handling.", p)
    html += body_open() + header(p)
    html += page_hero(p, [("Why Via Codos", "why-us.html"), ("How We Work", "#")], "How We Work",
                      "An Engagement You Never Have to Chase",
                      "Transparency about process is one of the biggest differentiators between an outsourcing partner you can trust and one you have to manage constantly. Here is exactly how an engagement runs, start to finish.")
    html += '<main id="main"><section class="section"><div class="container"><div class="grid grid-2">%s</div></div></section>%s</main>' % (st, cta_band(p))
    html += footer(p)
    write("why/how-we-work.html", html)

    # Our Promise
    proms = [
        ("No Tech Talk", "We will never use technical jargon or talk over your head. If you can't understand our explanation, that's our failure to communicate, not your failure to understand technology.", "message"),
        ("No Haggling", "We offer one fair price, quoted transparently up front. No inflated first quotes designed to be negotiated down, and no scope-creep fees sprung on you mid-project.", "tagicon"),
        ("Satisfaction Guarantee", "Everything we deliver is backed by a 100% satisfaction guarantee. If what we've built doesn't meet the agreed requirements, we make it right.", "award"),
    ]
    pr = "".join("""<div class="card reveal" data-delay="%d"><div class="icon-badge">%s</div><h3>%s</h3><p>%s</p></div>""" %
                 (n + 1, I[ic], t, d) for n, (t, d, ic) in enumerate(proms))
    html = head("Our Promise | Via Codos",
                "No jargon. No haggling. No excuses. See the three commitments Via Codos makes to every client, backed by a 100% satisfaction guarantee.", p)
    html += body_open() + header(p)
    html += page_hero(p, [("Why Via Codos", "why-us.html"), ("Our Promise", "#")], "Our Promise",
                      "Three Commitments. Every Client. Every Time.")
    html += '<main id="main"><section class="section"><div class="container"><div class="grid grid-3">%s</div></div></section>%s</main>' % (pr, cta_band(p))
    html += footer(p)
    write("why/our-promise.html", html)

# ----------------------------------------------------------------- COMPANY
def build_company():
    p = "../"
    # About
    html = head("About Via Codos | Global IT Outsourcing & AI Solutions Company",
                "Via Codos is a fast-growing technology and AI solutions company based in Sri Lanka, delivering IT outsourcing, custom software, and AI-powered solutions to 200+ clients worldwide.", p)
    html += body_open() + header(p)
    html += page_hero(p, [("Company", "about.html"), ("About Us", "#")], "About Us",
                      "We Take Care of Your IT. So You May Focus on Your Business.",
                      "Via Codos is a fast-growing technology and AI solutions company established in September 2024, based in Sri Lanka. We specialise in global IT outsourcing and delivering practical software and AI solutions that help businesses operate more efficiently and scale faster.")
    html += """<main id="main">
<section class="section"><div class="container detail-layout">
 <div class="prose reveal">
  <h2>Our Story</h2>
  <p>Founded with a vision to bridge the gap between global businesses and Sri Lanka's exceptional technology talent, Via Codos has grown rapidly since our inception in September 2024.</p>
  <p>What started as a focused IT outsourcing practice has expanded into a full-service technology partner — custom software, ERP systems, AI and automation, and cloud infrastructure — because our clients' needs grew alongside the trust they placed in us. Today, we're proud to have completed 500+ projects and built a reputation for excellence in IT outsourcing, custom software development, and AI-powered solutions.</p>
  <h2>Mission &amp; Vision</h2>
  <div class="duo" style="margin-top:24px">
   <div class="panel reveal-l"><h3>%s Mission</h3><p style="font-size:15.5px">To connect global businesses with Sri Lanka's top engineering talent, delivering innovative solutions that drive growth and efficiency.</p></div>
   <div class="panel reveal-r"><h3>%s Vision</h3><p style="font-size:15.5px">To be the leading bridge between global enterprises and Sri Lanka's technology ecosystem, recognised for excellence, integrity, and innovation.</p></div>
  </div>
 </div>
 <aside class="aside-card reveal-r">
  <div class="aside-stat"><b>Sept 2024</b><span>Established in Sri Lanka</span></div>
  <h4>Meet the people behind it</h4>
  <p>Leadership across engineering, AI, and global talent acquisition.</p>
  <a class="btn btn-primary" href="team.html">Meet Our Team %s</a>
 </aside>
</div></section>
<section class="band-dark section grain" data-p3d="0.9"><div class="container">
 <div class="section-head center reveal"><span class="tagline">By the Numbers</span><h2>Proof, Not Promises</h2></div>
 <div class="stats-grid">
  <div class="stat reveal"><b data-count="500" data-suffix="+">500+</b><span>Projects Completed</span></div>
  <div class="stat reveal" data-delay="1"><b data-count="200" data-suffix="+">200+</b><span>Clients Worldwide</span></div>
  <div class="stat reveal" data-delay="2"><b>40-70%%</b><span>Cost Savings</span></div>
  <div class="stat reveal" data-delay="3"><b data-count="100" data-suffix="+">100+</b><span>Pre-vetted Engineers</span></div>
 </div>
</div></section>
%s</main>""" % (I["target"], I["eye"], I["arrow"], cta_band(p))
    html += footer(p)
    write("company/about.html", html)

    # Team
    cards = ""
    for n, t in enumerate(TEAM):
        initials = "".join(w[0] for w in t["name"].split()[:2])
        cards += """<div class="card team-card reveal" data-delay="%d">
 <div class="team-photo">%s</div>
 <span class="team-role">%s</span><h3>%s</h3><p>%s</p></div>""" % (
            n + 1, initials, t["role"], t["name"], t["bio"])
    html = head("Our Team | Via Codos Leadership",
                "Meet the leadership team behind Via Codos — experts in strategic leadership, full-stack engineering, AI, and global talent acquisition.", p)
    html += body_open() + header(p)
    html += page_hero(p, [("Company", "about.html"), ("Our Team", "#")], "Our Team", "Meet the Experts",
                      "Our diverse team brings together expertise in AI, software engineering, data systems, DevOps, and mobile development from universities across Sri Lanka and Pakistan.")
    html += '<main id="main"><section class="section"><div class="container"><div class="grid grid-4">%s</div></div></section>%s</main>' % (cards, cta_band(p))
    html += footer(p)
    write("company/team.html", html)

    # Careers
    why = [
        ("globe", "Work with Global Clients", "Collaborate directly with clients from the USA, UK, Australia, and beyond — no layer of account managers between you and the people using what you build."),
        ("trend", "Growth Opportunities", "Continuous learning, certifications, and career advancement, with senior engineers mentoring within every pod."),
        ("cpu", "Cutting-Edge Tech", "Work with the latest technologies and modern development practices, not legacy stacks nobody else wants to maintain."),
    ]
    why_html = "".join("""<div class="card reveal" data-delay="%d"><div class="icon-badge">%s</div><h3>%s</h3><p>%s</p></div>""" %
                       (n + 1, I[ic], t, d) for n, (ic, t, d) in enumerate(why))
    jobs_html = ""
    for n, j in enumerate(JOBS):
        meta = "".join("<span>%s</span>" % m for m in j["meta"])
        resp = "".join("<li>%s</li>" % r for r in j["resp"])
        jobs_html += """<div class="card job reveal" data-delay="%d">
 <div class="job-top"><div><h3>%s</h3><div class="job-meta">%s</div></div>
 <a class="btn btn-outline btn-sm" href="mailto:info@viacodos.com?subject=Application%%20for%%20%s">Apply Now %s</a></div>
 <ul>%s</ul></div>""" % (n % 2 + 1, j["title"], meta, j["title"].replace(" ", "%20"), I["arrow"], resp)
    html = head("Careers at Via Codos | Join Our Global Engineering Team",
                "Explore open engineering, DevOps, AI, and QA roles at Via Codos. Remote-first, global clients, and continuous growth.", p)
    html += body_open() + header(p)
    html += page_hero(p, [("Company", "about.html"), ("Careers", "#")], "Careers", "Join the Via Codos Team",
                      "We're always looking for talented professionals who are passionate about technology and innovation. Join us in building the future of global IT outsourcing.")
    html += """<main id="main">
<section class="section"><div class="container">
 <div class="section-head center reveal"><span class="tagline">Why Work Here</span><h2>Engineering Without the Ceiling</h2></div>
 <div class="grid grid-3">%s</div>
</div></section>
<section class="section section-alt"><div class="container">
 <div class="section-head reveal"><span class="tagline">Open Positions</span><h2>Current Openings</h2></div>
 <div class="grid" style="grid-template-columns:1fr">%s</div>
</div></section>
%s</main>""" % (why_html, jobs_html,
                cta_band(p, "Don't see the right position?",
                         "Send us your resume anyway — we're growing faster than this list updates.",
                         "Send Your Resume"))
    html = html.replace('href="%scontact.html">Send Your Resume' % p,
                        'href="mailto:info@viacodos.com?subject=Open%20Application">Send Your Resume')
    html += footer(p)
    write("company/careers.html", html)

# ----------------------------------------------------------------- PORTFOLIO
def build_portfolio():
    p = "../"
    cards = ""
    for n, c in enumerate(CASE_STUDIES):
        cards += """<a class="card case-card reveal" data-delay="%d" href="%s.html">
 <div class="case-media"><span class="ph">%s</span>
  <img src="../assets/%s" alt="%s screenshot" loading="lazy" onerror="this.style.display='none'"></div>
 <div class="case-body"><span class="case-tag">%s</span><h3>%s</h3>
  <div class="case-metric">%s</div>
  <span class="link-arrow">Read the case study %s</span></div></a>""" % (
            n + 1, c["slug"], c["name"], c["image"], c["name"], c["sector"], c["name"], c["headline"], I["arrow"])
    html = head("Portfolio | Via Codos Case Studies",
                "Explore how Via Codos built BeltKit ERP, Qalam MMS, and AI Call Colleague — real results for real clients across automotive, community, and AI automation.", p)
    html += body_open() + header(p)
    html += page_hero(p, [("Portfolio", "index.html")], "Portfolio", "Our Featured Work",
                      "Explore our portfolio of successful projects across various industries. Each project demonstrates our commitment to quality, innovation, and delivering measurable results.")
    html += '<main id="main"><section class="section"><div class="container"><div class="grid grid-2">%s</div></div></section>%s</main>' % (
        cards, cta_band(p, "Interested in similar results for your business?",
                        "Tell us your operational problem — we'll show you what a purpose-built solution looks like.", "Start a Conversation"))
    html += footer(p)
    write("portfolio/index.html", html)

    for c in CASE_STUDIES:
        impl = "".join("<li>%s</li>" % x for x in c["implementation"])
        res = "".join("""<div class="stat reveal" data-delay="%d"><b>%s</b><span>%s</span></div>""" %
                      (n % 4, v, l) for n, (v, l) in enumerate(c["results"]))
        html = head(c["meta_title"], c["meta_desc"], p)
        html += body_open() + header(p)
        html += page_hero(p, [("Portfolio", "index.html"), (c["name"], "#")], c["sector"], c["name"], c["headline"])
        video_block = """<div class="video-wrap reveal">
   <span class="video-badge">%s — product tour</span>
   <video controls preload="metadata" playsinline poster="../assets/%s">
    <source src="../assets/%s" type="video/mp4">
    Your browser does not support the video tag.
   </video>
   <div class="video-end" hidden>
    <h4>Like what you saw?</h4>
    <p class="ve-sub">Let's talk about building the same operational clarity for your business.</p>
    <div class="ve-contacts">
     <a href="%s" target="_blank" rel="noopener">%s +94 721 980 060</a>
     <a href="mailto:info@viacodos.com">%s info@viacodos.com</a>
    </div>
    <button class="ve-replay" type="button">Watch again</button>
   </div>
  </div>""" % (c["name"], c["poster"], c["video"], WA_LINK, I["wa"], I["mail"])
        html += """<main id="main">
<section class="section"><div class="container detail-layout">
 <div class="prose reveal">
  %s
  <h2>The Client</h2><p>%s</p>
  <h2>The Challenge</h2><p>%s</p>
  <h2>Our Solution</h2><p>%s</p>
  <h2>Implementation</h2><ul>%s</ul>
  <div class="quote"><p>&ldquo;%s&rdquo;</p></div>
 </div>
 <aside class="aside-card reveal-r">
  <div class="aside-stat"><b>%s</b><span>%s</span></div>
  <h4>Want results like these?</h4>
  <p>Every flagship product on this page started as a client's operational headache.</p>
  <a class="btn btn-primary" href="%scontact.html">Get a Free Consultation %s</a>
 </aside>
</div></section>
<section class="band-dark section grain" data-p3d="0.9"><div class="container">
 <div class="section-head center reveal"><span class="tagline">Results &amp; Impact</span><h2>What Changed</h2></div>
 <div class="stats-grid">%s</div>
</div></section>
%s</main>""" % (video_block, c["client"], c["challenge"], c["solution"],
                impl, c["quote"], c["results"][0][0], c["results"][0][1], p, I["arrow"], res,
                cta_band(p, "Interested in similar results for your business?",
                         "Tell us your operational problem — we'll show you what a purpose-built solution looks like.", "Start a Conversation"))
        html += footer(p)
        write("portfolio/%s.html" % c["slug"], html)

# ----------------------------------------------------------------- INSIGHTS
def build_insights():
    p = "../"
    cards = ""
    for n, a in enumerate(INSIGHTS):
        cards += """<a class="card reveal" data-delay="%d" href="%s.html">
 <div class="post-meta"><span class="cat">%s</span><i>.</i><span>%s</span><i>.</i><span>%s</span></div>
 <h3>%s</h3><p>%s</p>
 <span class="link-arrow">Read article %s</span></a>""" % (
            n % 3 + 1, a["slug"], a["cat"], a["date"], a["read"], a["title"], a["excerpt"], I["arrow"])
    html = head("Insights | Via Codos Blog",
                "Thought leadership on IT outsourcing, AI automation, ERP, and technology trends from the Via Codos team.", p)
    html += body_open() + header(p)
    html += page_hero(p, [("Insights", "index.html")], "Insights", "Thought Leadership",
                      "Stay updated with the latest insights, trends, and best practices in technology, outsourcing, and digital transformation.")
    html += '<main id="main"><section class="section"><div class="container"><div class="grid grid-3">%s</div></div></section>%s</main>' % (
        cards, cta_band(p, "Want insights like these in your inbox?",
                        "Subscribe to our newsletter for the latest thinking on outsourcing, AI, and engineering.", "Subscribe via Contact"))
    html += footer(p)
    write("insights/index.html", html)

    for a in INSIGHTS:
        paras = "".join("<p>%s</p>" % b for b in a["body"])
        others = [x for x in INSIGHTS if x["slug"] != a["slug"]][:3]
        more = "".join("""<a class="card reveal" data-delay="%d" href="%s.html">
 <div class="post-meta"><span class="cat">%s</span><i>.</i><span>%s</span></div>
 <h3 style="font-size:17px">%s</h3><span class="link-arrow">Read article %s</span></a>""" % (
            n + 1, o["slug"], o["cat"], o["date"], o["title"], I["arrow"]) for n, o in enumerate(others))
        html = head(a["title"] + " | Via Codos Insights", a["excerpt"], p)
        html += body_open() + header(p)
        html += page_hero(p, [("Insights", "index.html"), (a["title"][:44] + "…", "#")], a["cat"], a["title"],
                          "%s · %s · %s" % (a["cat"], a["date"], a["read"]))
        html += """<main id="main">
<section class="section"><div class="container article"><div class="prose reveal">%s</div></div></section>
<section class="section section-alt"><div class="container">
 <div class="section-head reveal"><span class="tagline">Keep Reading</span><h2 style="font-size:28px">More Insights</h2></div>
 <div class="grid grid-3">%s</div>
</div></section>
%s</main>""" % (paras, more, cta_band(p))
        html += footer(p)
        write("insights/%s.html" % a["slug"], html)

# ----------------------------------------------------------------- CONTACT
def build_contact():
    p = ""
    opts = "".join('<option value="%s">%s</option>' % (s["name"], s["name"]) for s in SERVICES)
    html = head("Contact Via Codos | Get a Free IT Consultation",
                "Reach Via Codos by email, WhatsApp, or our Sri Lanka office. Get a free consultation on IT outsourcing, custom software, or AI automation.", p)
    html += body_open() + header(p)
    html += page_hero(p, [("Contact Us", "#")], "Contact Us",
                      "Tired of Waiting for Your Tech Company to Call You Back?",
                      "Connect with our team of information technology professionals and we'll help you overcome all your technology challenges — with the response time we've built our whole process around.")
    html += """<main id="main"><section class="section"><div class="container contact-grid">
 <div class="reveal-l">
  <div class="section-head" style="margin-bottom:24px"><span class="tagline">Reach Us Directly</span>
   <h2 style="font-size:28px">Talk to a Human, Fast</h2></div>
  <div class="contact-item"><div class="icon-badge">%s</div>
   <div><b>Email</b><a href="mailto:info@viacodos.com">info@viacodos.com</a></div></div>
  <div class="contact-item"><div class="icon-badge">%s</div>
   <div><b>WhatsApp</b><a href="%s" target="_blank" rel="noopener">+94 721 980 060</a></div></div>
  <div class="contact-item"><div class="icon-badge">%s</div>
   <div><b>Phone (US)</b><a href="tel:+18559543778">(855) 954-3778</a></div></div>
  <div class="contact-item" style="border-bottom:none"><div class="icon-badge">%s</div>
   <div><b>Office</b><span>Galle, Ginthota, Sri Lanka</span></div></div>
  <a class="btn btn-primary" style="margin-top:26px" href="%s" target="_blank" rel="noopener">Get Started Today %s</a>
 </div>
 <form class="form reveal-r" id="contactForm" novalidate>
  <div class="form-row">
   <div class="field"><label for="f-name">Full Name <em>*</em></label>
    <input id="f-name" name="name" type="text" autocomplete="name" required></div>
   <div class="field"><label for="f-company">Company Name</label>
    <input id="f-company" name="company" type="text" autocomplete="organization"></div>
  </div>
  <div class="form-row">
   <div class="field"><label for="f-email">Email Address <em>*</em></label>
    <input id="f-email" name="email" type="email" autocomplete="email" required></div>
   <div class="field"><label for="f-service">What service are you interested in?</label>
    <select id="f-service" name="service"><option value="Not sure yet">Not sure yet</option>%s</select></div>
  </div>
  <div class="field"><label for="f-message">Project details / message <em>*</em></label>
   <textarea id="f-message" name="message" required placeholder="Tell us what you're trying to build, fix, or scale…"></textarea></div>
  <button class="btn btn-primary" type="submit" style="width:100%%;justify-content:center">Send Message %s</button>
 </form>
</div></section></main>""" % (I["mail"], I["wa"], WA_LINK, I["phone"], I["pin"], WA_LINK, I["arrow"], opts, I["arrow"])
    html += footer(p)
    write("contact.html", html)

# ----------------------------------------------------------------- LEGAL
def legal_page(slug, title, meta_title, meta_desc, tagline, body_html):
    p = "../"
    html = head(meta_title, meta_desc, p)
    html += body_open() + header(p)
    html += page_hero(p, [(title, "#")], tagline, title, "Last updated: July 2026")
    html += '<main id="main"><section class="section"><div class="container article"><div class="prose reveal">%s</div></div></section>%s</main>' % (
        body_html, cta_band(p, "Questions about how we handle your data?",
                            "Contact us directly — we answer these questions plainly, without legal run-around.", "Contact Us"))
    html += footer(p)
    write("legal/%s.html" % slug, html)

PRIVACY = """
<h2>Introduction</h2>
<p>Via Codos Private Limited ("Via Codos," "we," "us," or "our") is committed to protecting the privacy of everyone who interacts with our website and services. This Privacy Policy explains what information we collect, why we collect it, how we use and protect it, and the rights you have over it. It applies to visitors of our website (viacodos.com) and to clients and prospective clients who engage with us directly.</p>
<h2>Information We Collect</h2>
<h3>Information you provide directly</h3>
<ul><li>Name, email address, phone number, and company name submitted through contact forms, consultation requests, or job applications</li>
<li>Project details, requirements, and business information shared during consultations or service engagements</li>
<li>Resumes, cover letters, and related application materials submitted through our Careers page</li>
<li>Any information you provide when communicating with us via email, WhatsApp, or phone</li></ul>
<h3>Information collected automatically</h3>
<ul><li>IP address, browser type, device type, and operating system</li>
<li>Pages visited, time spent on pages, and referring website</li>
<li>Cookies and similar tracking technologies (see Cookies section below)</li></ul>
<h3>Information collected during service delivery</h3>
<p>Where you engage us for software development, IT outsourcing, or related services, we may have access to business data, source code, credentials, and systems as necessary to perform the contracted work. This access is governed separately by the confidentiality and security terms in our client service agreements and our NDA &amp; Security Commitment.</p>
<h2>How We Use Your Information</h2>
<ul><li>Respond to inquiries and provide requested consultations</li>
<li>Deliver, manage, and improve our services</li>
<li>Process job applications</li>
<li>Communicate with you about your project, account, or our services</li>
<li>Send occasional updates, insights, or marketing communications (only where you have opted in or as otherwise permitted by law)</li>
<li>Comply with legal obligations and enforce our agreements</li>
<li>Improve our website's functionality and user experience</li></ul>
<h2>Legal Basis for Processing (for users in the EU/UK)</h2>
<p>Where applicable data protection law requires it, we process personal data on one or more of the following legal bases: your consent, the necessity of processing to perform a contract with you, our legitimate business interests, or compliance with a legal obligation.</p>
<h2>How We Share Information</h2>
<p>We do not sell your personal information. We may share information with:</p>
<ul><li>Employees, contractors, and engineers directly involved in delivering your project, on a need-to-know basis</li>
<li>Third-party service providers who support our operations (e.g., hosting providers, email services), under confidentiality obligations</li>
<li>Legal or regulatory authorities where required by law</li>
<li>A successor entity in the event of a merger, acquisition, or sale of assets, with notice provided where required</li></ul>
<h2>Data Security</h2>
<p>We implement administrative, technical, and physical safeguards designed to protect the confidentiality, integrity, and availability of the information we hold, including access controls, encryption where appropriate, and confidentiality agreements with all personnel. No system is completely secure, and while we work to protect your information, we cannot guarantee absolute security.</p>
<h2>Data Retention</h2>
<p>We retain personal information for as long as necessary to fulfil the purposes described in this policy, comply with legal obligations, resolve disputes, and enforce our agreements. Project-related data is generally retained for the duration of the client relationship plus a reasonable period thereafter, unless a longer or shorter period is agreed in a service contract.</p>
<h2>International Data Transfers</h2>
<p>Because Via Codos is based in Sri Lanka and serves clients internationally, your information may be transferred to, stored in, and processed in Sri Lanka or other countries where we or our service providers operate. Where required by law, we take steps to ensure such transfers are subject to appropriate safeguards.</p>
<h2>Your Rights</h2>
<p>Depending on your location, you may have the right to:</p>
<ul><li>Access the personal information we hold about you</li>
<li>Request correction of inaccurate information</li>
<li>Request deletion of your information, subject to legal and contractual limitations</li>
<li>Object to or restrict certain processing</li>
<li>Withdraw consent where processing is based on consent</li>
<li>Lodge a complaint with a relevant data protection authority</li></ul>
<p>To exercise any of these rights, contact us at <a href="mailto:info@viacodos.com">info@viacodos.com</a>.</p>
<h2>Cookies</h2>
<p>Our website uses cookies and similar technologies to improve functionality and understand how visitors use our site. You can control cookie preferences through your browser settings.</p>
<h2>Children's Privacy</h2>
<p>Our website and services are not directed at individuals under the age of 18, and we do not knowingly collect personal information from children.</p>
<h2>Changes to This Policy</h2>
<p>We may update this Privacy Policy from time to time. Material changes will be reflected by an updated "Last Updated" date, and where appropriate, we will provide additional notice.</p>
<h2>Contact Us</h2>
<p>Questions about this Privacy Policy can be directed to: Email: <a href="mailto:info@viacodos.com">info@viacodos.com</a> · Office: Galle, Ginthota, Sri Lanka</p>"""

TERMS = """
<h2>Acceptance of Terms</h2>
<p>These Terms of Service ("Terms") govern your access to and use of the Via Codos Private Limited ("Via Codos," "we," "us," "our") website and any inquiry, consultation, or engagement initiated through it. By accessing our website or engaging our services, you agree to be bound by these Terms. If you do not agree, please do not use our website or services.</p>
<p>These Terms apply to general use of our website and the formation of a service relationship. The specific scope, deliverables, fees, and timeline for any project are governed by a separate, individually negotiated Service Agreement or Statement of Work signed between Via Codos and the client, which takes precedence over these Terms in the event of a conflict.</p>
<h2>Description of Services</h2>
<p>Via Codos provides IT outsourcing, staff augmentation, custom software development, ERP development, web and mobile development, UI/UX design, AI and automation solutions, cloud and DevOps services, cybersecurity and compliance support, QA and test automation, and data engineering and analytics services, as further described on our website and in individual client agreements.</p>
<h2>Use of the Website</h2>
<p>You agree to use our website only for lawful purposes and in a manner that does not infringe the rights of, or restrict or inhibit the use and enjoyment of, the site by any third party. You agree not to attempt to gain unauthorized access to any part of our website, servers, or systems.</p>
<h2>Client Responsibilities</h2>
<p>Where you engage Via Codos for services, you agree to:</p>
<ul><li>Provide accurate, complete, and timely information necessary for us to perform the agreed work</li>
<li>Provide necessary access, credentials, and cooperation reasonably required for project delivery</li>
<li>Make payments in accordance with the agreed Service Agreement</li>
<li>Review and provide feedback on deliverables within agreed timeframes, where applicable</li></ul>
<h2>Intellectual Property</h2>
<p>Unless otherwise agreed in writing in a specific Service Agreement:</p>
<ul><li>Upon full payment for a project, ownership of the custom code, designs, and deliverables created specifically for the client transfers to the client.</li>
<li>Via Codos retains ownership of any pre-existing tools, frameworks, libraries, methodologies, or components ("Background IP") used in delivering the work, and grants the client a licence to use such Background IP to the extent embedded in the delivered work product.</li>
<li>Via Codos may retain the right to reuse general knowledge, skills, and non-client-specific techniques gained during an engagement, provided this does not involve disclosure of the client's confidential information.</li>
<li>The Via Codos name, logo, and website content remain the intellectual property of Via Codos Private Limited and may not be used without permission.</li></ul>
<h2>Confidentiality</h2>
<p>All client information, source code, business data, and credentials shared with Via Codos are treated as confidential and are protected under the terms of the Non-Disclosure Agreement (NDA) executed at the start of each engagement, and under our internal Security Commitment. These website Terms do not replace or limit the protections provided under a signed NDA.</p>
<h2>Fees and Payment</h2>
<p>Fees, payment schedules, and accepted payment methods are set out in the individual Service Agreement or invoice for each engagement. Unless otherwise agreed, invoices are due within the period specified on the invoice. Late payment may result in suspension of services until outstanding amounts are settled.</p>
<h2>Warranties and Disclaimers</h2>
<p>Via Codos will perform services with reasonable skill and care, consistent with generally accepted industry standards. Except as expressly stated in a Service Agreement, our services and website are provided "as is" without warranties of any kind, whether express or implied, including but not limited to implied warranties of merchantability, fitness for a particular purpose, or non-infringement. We do not warrant that any software, application, or system will be entirely free of defects or uninterrupted.</p>
<h2>Limitation of Liability</h2>
<p>To the maximum extent permitted by applicable law, Via Codos's total liability arising out of or related to any engagement shall not exceed the total fees paid by the client for the specific project giving rise to the claim in the twelve (12) months preceding the claim. Via Codos shall not be liable for indirect, incidental, consequential, special, or punitive damages, including loss of profits, revenue, data, or business opportunity, even if advised of the possibility of such damages.</p>
<h2>Termination</h2>
<p>Either party may terminate an ongoing engagement in accordance with the notice period and terms specified in the applicable Service Agreement. Via Codos reserves the right to suspend or terminate services immediately in cases of non-payment, breach of these Terms, or unlawful use of our services.</p>
<h2>Indemnification</h2>
<p>You agree to indemnify and hold harmless Via Codos, its officers, employees, and engineers from any claims, damages, or expenses arising from your breach of these Terms, misuse of our services, or violation of any applicable law.</p>
<h2>Governing Law and Dispute Resolution</h2>
<p>These Terms are governed by the laws of Sri Lanka, without regard to conflict of law principles, unless otherwise specified in an individual Service Agreement. Any disputes arising from these Terms or an engagement shall first be addressed through good-faith negotiation between the parties, and if unresolved, may be referred to arbitration or the courts of Sri Lanka, or such other forum as agreed in the applicable Service Agreement.</p>
<h2>Changes to These Terms</h2>
<p>We may revise these Terms from time to time. Continued use of our website or services after changes are posted constitutes acceptance of the revised Terms.</p>
<h2>Contact Us</h2>
<p>Email: <a href="mailto:info@viacodos.com">info@viacodos.com</a> · Office: Galle, Ginthota, Sri Lanka</p>"""

NDA = """
<h2>Introduction</h2>
<p>When you work with Via Codos, you are often giving us access to things that matter enormously to your business — source code, customer data, credentials, and internal systems. This page describes, in plain language, the standard we hold ourselves to in protecting that information. It is a public summary of our practices, not a substitute for the formal Non-Disclosure Agreement (NDA) signed at the start of every client engagement, which contains the full, legally binding terms.</p>
<h2>Our Confidentiality Standard</h2>
<p>Every Via Codos engagement begins under a signed mutual NDA before any project details, access, or credentials are shared. This is not an optional add-on for larger clients — it is a standard first step for every project we take on, regardless of size.</p>
<h2>What We Protect</h2>
<ul><li>Source code and technical architecture</li>
<li>Business data, customer information, and internal documents</li>
<li>Login credentials, API keys, and system access</li>
<li>Project scope, pricing, and business strategy discussed during engagements</li>
<li>Any other information reasonably understood to be confidential</li></ul>
<h2>How We Protect It</h2>
<ul><li><strong>Access on a need-to-know basis.</strong> Only engineers directly assigned to your project have access to your systems and code. Access is revoked promptly when a team member rolls off a project.</li>
<li><strong>Individual confidentiality agreements.</strong> Every engineer, designer, and team member at Via Codos signs an individual confidentiality agreement as a condition of employment, independent of the client-facing NDA.</li>
<li><strong>Secure credential handling.</strong> Credentials and access keys are stored using industry-standard secured methods and are not shared over insecure channels such as plain email or chat.</li>
<li><strong>Encrypted storage and transfer.</strong> Client data and source code are stored and transferred using encryption appropriate to the sensitivity of the information involved.</li>
<li><strong>Controlled environments.</strong> Where appropriate, development and testing work is conducted in isolated, access-controlled environments to reduce the risk of unauthorized exposure.</li></ul>
<h2>Security-Conscious Development</h2>
<p>For clients with elevated security or compliance needs — particularly in healthcare, financial services, and other regulated industries — we can apply additional practices including secure coding standards, dedicated access logging, and support in preparing technical evidence for compliance frameworks such as GDPR, SOC 2, or PCI-DSS. See our <a href="../services/cybersecurity.html">Cybersecurity &amp; Compliance</a> service page for details.</p>
<h2>Incident Response</h2>
<p>In the unlikely event of a security incident affecting client data, Via Codos is committed to prompt investigation, containment, and notification to affected clients in accordance with our contractual and legal obligations.</p>
<h2>Your NDA Is Separate From This Page</h2>
<p>This page is a public description of our general practices and is intended to build confidence before you engage us — it is not itself a legally binding confidentiality agreement. The actual Non-Disclosure Agreement you sign with Via Codos at project kickoff is the legally enforceable document governing confidentiality for your specific engagement, and its terms will take precedence over anything summarized here.</p>
<h2>Questions About Security or Confidentiality</h2>
<p>If you'd like to review our standard NDA template before starting a conversation, or have specific security or compliance requirements, contact us directly: Email: <a href="mailto:info@viacodos.com">info@viacodos.com</a> · WhatsApp: +94 76 904 7552</p>"""

def build_legal():
    legal_page("privacy-policy", "Privacy Policy", "Privacy Policy | Via Codos",
               "How Via Codos collects, uses, and protects your information.", "Legal", PRIVACY)
    legal_page("terms-of-service", "Terms of Service", "Terms of Service | Via Codos",
               "The terms governing use of the Via Codos website and services.", "Legal", TERMS)
    legal_page("nda-security", "Our Confidentiality & Security Commitment", "NDA & Security Commitment | Via Codos",
               "The confidentiality and security standard Via Codos holds itself to on every engagement.", "Legal & Security", NDA)

# ----------------------------------------------------------------- assets note
def build_assets_note():
    note = """VIA CODOS — MEDIA CHECKLIST  (see IMAGE-GUIDE.md in project root for full specs + AI prompts)

IMAGES
hero-image.jpg                  Home hero      Team/office image, portrait-ish 4:5, ~1200x1400
beltkit-poster.jpg              Case studies   BeltKit video poster frame, 16:9, ~1600x900
qalam-poster.jpg                Case studies   Qalam MMS video poster frame, 16:9
realtor-grow-poster.jpg         Case studies   Realtor Grow video poster frame, 16:9
ai-call-colleague-poster.jpg    Case studies   AI Call Colleague video poster frame, 16:9

VIDEOS (MP4, H.264, 16:9, ideally < 25 MB each)
beltkit.mp4                     portfolio/beltkit.html
qalam.mp4                       portfolio/qalam-mms.html
realtor-grow.mp4                portfolio/realtor-grow.html
ai-call-colleague.mp4           portfolio/ai-call-colleague.html

Already in place: logo.png (transparent, generated from your logo.jpeg).
No team photos needed — the team page uses monogram medallions by design.
"""
    full = os.path.join(OUT, "assets", "IMAGES-README.txt")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(note)
    print("  + assets/IMAGES-README.txt")

# ----------------------------------------------------------------- run
if __name__ == "__main__":
    print("Building Via Codos site →", OUT)
    build_home()
    build_services()
    build_industries()
    build_why()
    build_company()
    build_portfolio()
    build_insights()
    build_contact()
    build_legal()
    build_assets_note()
    print("Done.")
