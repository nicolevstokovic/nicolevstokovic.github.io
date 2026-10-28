#!/usr/bin/env python3
"""Gradi statičnu stranicu Nicole Vojak Štoković iz _izvor/tekstovi.py.

Pokretanje (iz korijena spremišta):
    python3 _izvor/build.py              # gradi pravu stranicu u korijen spremišta
    python3 _izvor/build.py --pregled DIR  # gradi privatni pregled (noindex) u DIR
"""
import html
import json
import os
import shutil
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tekstovi import TEKSTOVI  # noqa: E402

SITE = "https://nicolevstokovic.github.io"
IME = "Nicole Vojak Štoković"
EMAIL = "nicolevojak@gmail.com"
MREZE = [
    ("Instagram", "https://www.instagram.com/nicolevstokovic/", "@nicolevstokovic"),
    ("Facebook", "https://www.facebook.com/nicolevstokovic", "nicolevstokovic"),
    ("TikTok", "https://www.tiktok.com/@nicolevstokovic", "@nicolevstokovic"),
    ("LinkedIn", "https://www.linkedin.com/in/nicolevstokovic", "nicolevstokovic"),
]
JEZICI = ["hr", "en", "it"]
POCETNA = {"hr": "/", "en": "/en/", "it": "/it/"}
TEKST_DIO = {"hr": "/tekstovi/", "en": "/en/writing/", "it": "/it/testi/"}
FOTO = "img/nicole-za-mikserom.jpg"

MJESECI = {
    "hr": ["siječnja", "veljače", "ožujka", "travnja", "svibnja", "lipnja", "srpnja", "kolovoza", "rujna", "listopada", "studenoga", "prosinca"],
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "it": ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"],
}

L = {
    "hr": {
        "locale": "hr_HR",
        "nav": [("Tekstovi", "#tekstovi"), ("O meni", "#o-meni"), ("Kontakt", "#kontakt")],
        "onair": "U eteru · Istra",
        "lede": "Radijska voditeljica i novinarka. Ovdje pišem ono što ne stane u prilog.",
        "btn": "Čitaj kolumne",
        "caption": "Šešir glavu čuva, slušalice priču.",
        "foto_alt": "Nicole Vojak Štoković za radijskim mikserom, u crnom šeširu",
        "portret_alt": "Nicole Vojak Štoković sa slušalicama i naočalama, smiješi se",
        "najnovija": "Najnovija kolumna",
        "cijela": "Čitaj cijelu kolumnu",
        "biljeznica": "Iz bilježnice",
        "sve": "Sve",
        "vrste": {"kolumna": ("Kolumna", "Kolumne"), "pjesma": ("Pjesma", "Pjesme"), "crtica": ("Crtica", "Crtice")},
        "o_meni": "O meni",
        "o_naslov": "Glas koji ste možda već čuli",
        "bio": [
            "Šest godina govorim u eter. Prije toga bila sam prevoditeljica, plesačica i moderatorica, a radio me pronašao gotovo slučajno: kroz talijanski jezik i jedan turistički prilog kojemu je trebao glas. Ostala sam.",
            "Kao voditeljica i novinarka bavim se temama za koje se rijetko nađe dovoljno vremena. Zdravljem, majčinstvom, odgojem, mentalnim zdravljem. Zanima me ono što ostaje izvan vijesti: kako se živi, kako se priča, što nas dira.",
            "Najradije slušam ljude kojima se rijetko daje riječ. U njihovim pričama naš kraj izgleda drugačije nego na razglednicama.",
            "Ovdje zapisujem ono što ne stane u radijski prilog.",
        ],
        "kontakt": "Kontakt",
        "kontakt_naslov": "Pišite mi",
        "kontakt_tekst": "Za suradnju na tekstovima, prijedloge tema i priče koje bi trebalo ispričati.",
        "kopiraj": "Kopiraj", "kopirano": "Kopirano",
        "natrag": "Svi tekstovi",
        "jos": "Još iz bilježnice",
        "autor_kratko": "radijska voditeljica i novinarka iz Istre.",
        "regija": "Istra, Hrvatska",
        "home_title": "Nicole Vojak Štoković – kolumne, pjesme i crtice",
        "home_desc": "Nicole Vojak Štoković, radijska voditeljica i novinarka iz Istre. Kolumne, pjesme i crtice o zdravlju, majčinstvu, mentalnom zdravlju i ljudima čije priče rijetko čujemo.",
        "job": ["Radijska voditeljica", "Novinarka"],
        "pregled": "Pregled u izradi. Stranica još nije javna.",
        "jezik_naziv": "Hrvatski",
        "nije_pronadeno": "Ova stranica ne postoji.",
        "na_pocetnu": "Na početnu",
    },
    "en": {
        "locale": "en_GB",
        "nav": [("Writing", "#tekstovi"), ("About", "#o-meni"), ("Contact", "#kontakt")],
        "onair": "On air · Istria",
        "lede": "Radio host and journalist. Here I write what doesn’t fit into a radio segment.",
        "btn": "Read the columns",
        "caption": "The hat guards the head, the headphones guard the story.",
        "foto_alt": "Nicole Vojak Štoković at the radio mixing desk, wearing a black hat",
        "portret_alt": "Nicole Vojak Štoković smiling, wearing headphones and glasses",
        "najnovija": "Latest column",
        "cijela": "Read the full column",
        "biljeznica": "From the notebook",
        "sve": "All",
        "vrste": {"kolumna": ("Column", "Columns"), "pjesma": ("Poem", "Poems"), "crtica": ("Sketch", "Sketches")},
        "o_meni": "About",
        "o_naslov": "A voice you may already know",
        "bio": [
            "I have been on air for six years. Before that I was a translator, a dancer and an event host, and radio found me almost by chance: through the Italian language and a tourism segment that needed a voice. I stayed.",
            "As a host and journalist I cover subjects that rarely get enough time. Health, motherhood, parenting, mental health. I am interested in what stays outside the news: how we live, how we tell our stories, what moves us.",
            "Most of all I like listening to people who are rarely given the floor. In their stories, our region looks different from the postcards.",
            "Here I write down what doesn’t fit into a radio segment.",
        ],
        "kontakt": "Contact",
        "kontakt_naslov": "Write to me",
        "kontakt_tekst": "For writing collaborations, topic suggestions and stories that deserve to be told.",
        "kopiraj": "Copy", "kopirano": "Copied",
        "natrag": "All writing",
        "jos": "More from the notebook",
        "autor_kratko": "radio host and journalist from Istria, Croatia.",
        "regija": "Istria, Croatia",
        "home_title": "Nicole Vojak Štoković – columns, poems and sketches",
        "home_desc": "Nicole Vojak Štoković, radio host and journalist from Istria, Croatia. Columns, poems and sketches about health, motherhood, mental health and people whose stories we rarely hear.",
        "job": ["Radio host", "Journalist"],
        "pregled": "Preview in progress. The site is not public yet.",
        "jezik_naziv": "English",
        "nije_pronadeno": "This page does not exist.",
        "na_pocetnu": "Go to the home page",
    },
    "it": {
        "locale": "it_IT",
        "nav": [("Testi", "#tekstovi"), ("Chi sono", "#o-meni"), ("Contatti", "#kontakt")],
        "onair": "In onda · Istria",
        "lede": "Conduttrice radiofonica e giornalista. Qui scrivo quello che non entra in un servizio.",
        "btn": "Leggi le rubriche",
        "caption": "Il cappello protegge la testa, le cuffie la storia.",
        "foto_alt": "Nicole Vojak Štoković al mixer radiofonico, con un cappello nero",
        "portret_alt": "Nicole Vojak Štoković sorridente, con cuffie e occhiali",
        "najnovija": "Ultima rubrica",
        "cijela": "Leggi tutta la rubrica",
        "biljeznica": "Dal taccuino",
        "sve": "Tutti",
        "vrste": {"kolumna": ("Rubrica", "Rubriche"), "pjesma": ("Poesia", "Poesie"), "crtica": ("Bozzetto", "Bozzetti")},
        "o_meni": "Chi sono",
        "o_naslov": "Una voce che forse avete già sentito",
        "bio": [
            "Sono in onda da sei anni. Prima ero traduttrice, ballerina e presentatrice, e la radio mi ha trovata quasi per caso: attraverso la lingua italiana e una rubrica turistica che aveva bisogno di una voce. Sono rimasta.",
            "Come conduttrice e giornalista mi occupo di temi a cui raramente si dedica abbastanza tempo. Salute, maternità, educazione, salute mentale. Mi interessa ciò che resta fuori dalle notizie: come si vive, come si racconta, cosa ci tocca.",
            "Più di tutto mi piace ascoltare le persone a cui raramente si dà la parola. Nelle loro storie la nostra terra appare diversa da come la mostrano le cartoline.",
            "Qui annoto ciò che non entra in un servizio radiofonico.",
        ],
        "kontakt": "Contatti",
        "kontakt_naslov": "Scrivetemi",
        "kontakt_tekst": "Per collaborazioni sui testi, proposte di temi e storie che meritano di essere raccontate.",
        "kopiraj": "Copia", "kopirano": "Copiato",
        "natrag": "Tutti i testi",
        "jos": "Altro dal taccuino",
        "autor_kratko": "conduttrice radiofonica e giornalista dall’Istria, Croazia.",
        "regija": "Istria, Croazia",
        "home_title": "Nicole Vojak Štoković – rubriche, poesie e bozzetti",
        "home_desc": "Nicole Vojak Štoković, conduttrice radiofonica e giornalista dall’Istria. Rubriche, poesie e bozzetti su salute, maternità, salute mentale e persone le cui storie ascoltiamo di rado.",
        "job": ["Conduttrice radiofonica", "Giornalista"],
        "pregled": "Anteprima in lavorazione. Il sito non è ancora pubblico.",
        "jezik_naziv": "Italiano",
        "nije_pronadeno": "Questa pagina non esiste.",
        "na_pocetnu": "Alla pagina iniziale",
    },
}

E = html.escape


def datum_txt(iso, lang):
    d = date.fromisoformat(iso)
    m = MJESECI[lang][d.month - 1]
    if lang == "hr":
        return f"{d.day}. {m} {d.year}."
    if lang == "en":
        return f"{d.day} {m} {d.year}"
    return f"{d.day} {m} {d.year}"


def tekst_url(t, lang):
    return TEKST_DIO[lang] + t[lang]["slug"] + "/"


class Gradnja:
    def __init__(self, out, pregled):
        self.out = out
        self.pregled = pregled
        self.urls = []  # (lang->url dict) for sitemap

    # --- linkovi ---
    def rel(self, od, do):
        """Relativni link sa stranice `od` (url putanja direktorija) na `do` (putanja; direktorij završava s /)."""
        anchor = ""
        if "#" in do:
            do, anchor = do.split("#", 1)
            anchor = "#" + anchor
        od_dir = od if od.endswith("/") else os.path.dirname(od) + "/"
        if do.endswith("/"):
            r = os.path.relpath(do, od_dir)
            r = "" if r == "." else r + "/"
            if self.pregled:
                r += "index.html"
            elif r == "":
                r = "./"
        else:
            r = os.path.relpath(do, od_dir)
        return r + anchor

    # --- dijelovi ---
    def head(self, lang, path, title, desc, alternates, og_type, jsonld, og_image=FOTO):
        url = SITE + path
        alt = "".join(
            f'<link rel="alternate" hreflang="{lg}" href="{SITE + alternates[lg]}">' for lg in JEZICI
        ) + f'<link rel="alternate" hreflang="x-default" href="{SITE + alternates["hr"]}">'
        robots = '<meta name="robots" content="noindex, nofollow">' if self.pregled else ""
        return f"""<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
{robots}<link rel="canonical" href="{url}">
{alt}
<meta property="og:site_name" content="{E(IME)}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/{og_image}">
<meta property="og:locale" content="{L[lang]['locale']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="{self.rel(path, '/img/ikona.png')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300..600;1,6..72,300..500&family=Hanken+Grotesk:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{self.rel(path, '/css/stil.css')}">
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>"""

    def header(self, lang, path, alternates, home=False):
        h = POCETNA[lang]
        nav = "".join(
            f'<li><a href="{self.rel(path, h + a)}">{E(n)}</a></li>' for n, a in L[lang]["nav"]
        )
        langs = "".join(
            (f'<a href="{self.rel(path, alternates[lg])}" lang="{lg}" hreflang="{lg}"'
             + (' aria-current="true"' if lg == lang else "")
             + f' title="{L[lg]["jezik_naziv"]}">{lg.upper()}</a>')
            for lg in JEZICI
        )
        note = f'<div class="preview-note" role="note"><div class="wrap">{E(L[lang]["pregled"])}</div></div>' if self.pregled else ""
        return f"""{note}<header class="top">
  <div class="wrap">
    <a class="mark" href="{self.rel(path, h)}">Nicole <em>Vojak</em> Štoković</a>
    <div class="nav-side">
      <nav aria-label="{E(L[lang]['nav'][0][0])}"><ul>{nav}</ul></nav>
      <div class="langs">{langs}</div>
    </div>
  </div>
</header>"""

    def footer(self, lang):
        return f'<footer><div class="wrap"><span>© {date.today().year} {E(IME)}</span><span>{E(L[lang]["regija"])}</span></div></footer>'

    def tijelo_teksta(self, t, lang):
        poem = t["vrsta"] == "pjesma"
        out = []
        for blok in t[lang]["tekst"].strip().split("\n\n"):
            b = blok.strip()
            if b == ". . .":
                out.append('<p class="pauza" aria-label="tri sekunde tišine">. . .</p>')
            elif poem:
                out.append("<p>" + "".join(f'<span class="v">{E(r)}</span>' for r in b.split("\n")) + "</p>")
            else:
                out.append("<p>" + E(" ".join(b.split("\n"))) + "</p>")
        return "\n".join(out)

    def isjecak(self, t, lang, n=1):
        blokovi = [b for b in t[lang]["tekst"].strip().split("\n\n") if b.strip() != ". . ."]
        return blokovi[:n]

    def osoba(self, lang):
        return {
            "@type": "Person",
            "@id": SITE + "/#nicole",
            "name": IME,
            "alternateName": ["Nicole Vojak Stokovic", "Nicole V. Štoković"],
            "jobTitle": L[lang]["job"],
            "url": SITE + POCETNA[lang],
            "image": SITE + "/" + FOTO,
            "email": "mailto:" + EMAIL,
            "address": {"@type": "PostalAddress", "addressRegion": "Istarska županija", "addressCountry": "HR"},
            "knowsLanguage": ["hr", "it", "en"],
            "knowsAbout": ["zdravlje", "majčinstvo", "roditeljstvo", "mentalno zdravlje", "lokalne priče", "radio"],
            "sameAs": [u for _, u, _ in MREZE],
        }

    def stranica(self, path, lang, head, body, ulazna=False):
        """Zapisuje stranicu. Ulazna stranica pregleda piše se bez <html>/<head> omota (Artifact ga dodaje)."""
        script = f"""<script>
document.querySelectorAll('.tabs button').forEach(function(t){{t.addEventListener('click',function(){{
document.querySelectorAll('.tabs button').forEach(function(x){{x.setAttribute('aria-pressed',x===t?'true':'false')}});
document.querySelectorAll('.lista li').forEach(function(p){{p.hidden=!(t.dataset.f==='sve'||p.dataset.kind===t.dataset.f)}});}})}});
var c=document.getElementById('copy');if(c){{c.addEventListener('click',function(){{var el=document.getElementById('email');
try{{navigator.clipboard.writeText(el.textContent).then(function(){{c.textContent='{L[lang]['kopirano']}';setTimeout(function(){{c.textContent='{L[lang]['kopiraj']}'}},1800)}},function(){{getSelection().selectAllChildren(el)}})}}catch(e){{getSelection().selectAllChildren(el)}}}})}}
</script>"""
        if ulazna:
            doc = f'<meta name="claude:viewport-fit-sides" content="cover">\n{head}\n<div lang="{lang}">\n{body}\n</div>\n{script}'
        else:
            doc = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}
</head>
<body>
{body}
{script}
</body>
</html>
"""
        rel = path.lstrip("/")
        fname = os.path.join(self.out, rel, "index.html") if path.endswith("/") else os.path.join(self.out, rel)
        if ulazna:
            fname = os.path.join(self.out, "_ulaz.html")
        os.makedirs(os.path.dirname(fname), exist_ok=True)
        with open(fname, "w", encoding="utf-8") as f:
            f.write(doc)

    # --- početna ---
    def pocetna(self, lang):
        path = POCETNA[lang]
        S = L[lang]
        alternates = dict(POCETNA)
        kol = next(t for t in TEKSTOVI if t["vrsta"] == "kolumna")
        isj = "".join(f"<p>{E(' '.join(b.split()))}</p>" for b in self.isjecak(kol, lang, 2))
        tabs = f'<button type="button" id="f-sve" data-f="sve" aria-pressed="true">{E(S["sve"])}</button>' + "".join(
            f'<button type="button" id="f-{v}" data-f="{v}" aria-pressed="false">{E(S["vrste"][v][1])}</button>'
            for v in ["kolumna", "pjesma", "crtica"] if any(t["vrsta"] == v for t in TEKSTOVI)
        )
        items = "".join(
            f"""<li data-kind="{t['vrsta']}"><a href="{self.rel(path, tekst_url(t, lang))}">
<span class="kind">{E(S['vrste'][t['vrsta']][0])} · {datum_txt(t['datum'], lang)}</span>
<span class="ttl">{E(t[lang]['naslov'])}</span>
<span class="excerpt">{E(t[lang]['opis'])}</span></a></li>"""
            for t in TEKSTOVI
        )
        bio = "".join(f"<p>{E(p)}</p>" for p in S["bio"])
        mreze = "".join(
            f'<li><a href="{u}" target="_blank" rel="me noopener">{n} <span class="handle">{E(h)}</span></a></li>'
            for n, u, h in MREZE
        )
        body = f"""{self.header(lang, path, alternates, home=True)}
<main id="vrh">
  <section class="hero" aria-labelledby="ime">
    <div class="wrap">
      <div class="intro">
        <div class="onair label"><i aria-hidden="true"></i>{E(S['onair'])}</div>
        <h1 id="ime">Nicole Vojak<span>Štoković</span></h1>
        <p class="lede">{E(S['lede'])}</p>
        <a class="btn" href="#kolumne">{E(S['btn'])}</a>
      </div>
      <figure class="arch">
        <img src="{self.rel(path, '/' + FOTO)}" alt="{E(S['foto_alt'])}" width="1050" height="1400">
        <figcaption>{E(S['caption'])}</figcaption>
      </figure>
    </div>
  </section>

  <section id="kolumne" class="featured" aria-labelledby="k1">
    <div class="wrap"><div class="col">
      <div class="kicker label"><span class="kind">{E(S['najnovija'])}</span><span>{datum_txt(kol['datum'], lang)}</span></div>
      <h2 id="k1"><a href="{self.rel(path, tekst_url(kol, lang))}">{E(kol[lang]['naslov'])}</a></h2>
      <div class="prose">{isj}</div>
      <a class="more-link" href="{self.rel(path, tekst_url(kol, lang))}">{E(S['cijela'])} →</a>
    </div></div>
  </section>

  <section id="tekstovi" aria-labelledby="a-naslov">
    <div class="wrap"><div class="col">
      <div class="arch-head">
        <h2 id="a-naslov">{E(S['biljeznica'])}</h2>
        <div class="tabs" role="group">{tabs}</div>
      </div>
      <ul class="lista">{items}</ul>
    </div></div>
  </section>

  <section id="o-meni" class="about" aria-labelledby="o-naslov">
    <div class="wrap about-grid">
      <figure class="portret"><img src="{self.rel(path, '/img/nicole-slusalice.jpg')}" alt="{E(S['portret_alt'])}" width="900" height="1200" loading="lazy"></figure>
      <div class="about-text">
        <div class="label">{E(S['o_meni'])}</div>
        <h2 id="o-naslov">{E(S['o_naslov'])}</h2>
        <div class="prose">{bio}</div>
      </div>
    </div>
  </section>

  <section id="kontakt" class="contact" aria-labelledby="c-naslov">
    <div class="wrap"><div class="col">
      <div class="label">{E(S['kontakt'])}</div>
      <h2 id="c-naslov">{E(S['kontakt_naslov'])}</h2>
      <p>{E(S['kontakt_tekst'])}</p>
      <div class="mail"><span id="email">{EMAIL}</span><button type="button" id="copy">{E(S['kopiraj'])}</button></div>
      <ul class="social">{mreze}</ul>
    </div></div>
  </section>
</main>
{self.footer(lang)}"""
        jsonld = {
            "@context": "https://schema.org",
            "@graph": [
                self.osoba(lang),
                {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": IME,
                 "inLanguage": ["hr", "en", "it"], "author": {"@id": SITE + "/#nicole"}},
            ],
        }
        head = self.head(lang, path, S["home_title"], S["home_desc"], alternates, "profile", jsonld)
        self.stranica(path, lang, head, body)
        if self.pregled and lang == "hr":
            self.stranica(path, lang, head, body, ulazna=True)
        self.urls.append(alternates)

    # --- tekst ---
    def tekst(self, t, lang):
        S = L[lang]
        path = tekst_url(t, lang)
        alternates = {lg: tekst_url(t, lg) for lg in JEZICI}
        ostali = [o for o in TEKSTOVI if o is not t][:3]
        jos = "".join(
            f"""<li><a href="{self.rel(path, tekst_url(o, lang))}"><span class="kind">{E(S['vrste'][o['vrsta']][0])}</span>
<span class="ttl">{E(o[lang]['naslov'])}</span></a></li>""" for o in ostali
        )
        klasa = "prose poem" if t["vrsta"] == "pjesma" else "prose"
        body = f"""{self.header(lang, path, alternates)}
<main>
  <article class="clanak">
    <div class="wrap"><div class="col">
      <a class="back" href="{self.rel(path, POCETNA[lang] + '#tekstovi')}">← {E(S['natrag'])}</a>
      <div class="kicker label"><span class="kind">{E(S['vrste'][t['vrsta']][0])}</span><time datetime="{t['datum']}">{datum_txt(t['datum'], lang)}</time></div>
      <h1>{E(t[lang]['naslov'])}</h1>
      <div class="{klasa}">
{self.tijelo_teksta(t, lang)}
      </div>
      <p class="potpis"><a href="{self.rel(path, POCETNA[lang] + '#o-meni')}">{E(IME)}</a>, {E(S['autor_kratko'])}</p>
    </div></div>
  </article>
  <section class="jos" aria-labelledby="jos-naslov">
    <div class="wrap"><div class="col">
      <h2 id="jos-naslov">{E(S['jos'])}</h2>
      <ul class="lista">{jos}</ul>
    </div></div>
  </section>
</main>
{self.footer(lang)}"""
        tip = "CreativeWork" if t["vrsta"] == "pjesma" else "Article"
        jsonld = {
            "@context": "https://schema.org",
            "@type": tip,
            "headline": t[lang]["naslov"],
            "name": t[lang]["naslov"],
            "description": t[lang]["opis"],
            "genre": S["vrste"][t["vrsta"]][0],
            "inLanguage": lang,
            "datePublished": t["datum"],
            "url": SITE + path,
            "mainEntityOfPage": SITE + path,
            "image": SITE + "/" + FOTO,
            "author": self.osoba(lang),
            "publisher": {"@id": SITE + "/#nicole"},
        }
        title = f"{t[lang]['naslov']} – {S['vrste'][t['vrsta']][0].lower()} · {IME}"
        head = self.head(lang, path, title, t[lang]["opis"], alternates, "article", jsonld)
        head += f'\n<meta property="article:published_time" content="{t["datum"]}">\n<meta property="article:author" content="{E(IME)}">'
        self.stranica(path, lang, head, body)
        self.urls.append(alternates)

    def stranica_404(self):
        S = L["hr"]
        path = "/404.html"
        body = f"""{self.header('hr', '/', POCETNA)}
<main><section><div class="wrap"><div class="col">
<h1 style="font-size:2.3rem">{E(S['nije_pronadeno'])}</h1>
<p><a href="/">{E(S['na_pocetnu'])}</a> · <a href="/en/">{E(L['en']['na_pocetnu'])}</a> · <a href="/it/">{E(L['it']['na_pocetnu'])}</a></p>
</div></div></section></main>"""
        head = f"""<title>404 · {E(IME)}</title><meta name="robots" content="noindex">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300..600;1,6..72,300..500&family=Hanken+Grotesk:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/css/stil.css"><link rel="icon" type="image/png" href="/img/ikona.png">"""
        self.stranica(path, "hr", head, body)

    def sitemap(self):
        rows = []
        for alts in self.urls:
            links = "".join(
                f'<xhtml:link rel="alternate" hreflang="{lg}" href="{SITE + alts[lg]}"/>' for lg in JEZICI
            )
            for lg in JEZICI:
                rows.append(f"<url><loc>{SITE + alts[lg]}</loc>{links}</url>")
        xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
               + "\n".join(rows) + "\n</urlset>\n")
        with open(os.path.join(self.out, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write(xml)
        with open(os.path.join(self.out, "robots.txt"), "w", encoding="utf-8") as f:
            if self.pregled:
                f.write("User-agent: *\nDisallow: /\n")
            else:
                f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

    def staticno(self):
        src = os.path.dirname(os.path.abspath(__file__))
        os.makedirs(os.path.join(self.out, "css"), exist_ok=True)
        shutil.copy(os.path.join(src, "stil.css"), os.path.join(self.out, "css", "stil.css"))
        if os.path.abspath(self.out) != ROOT:
            shutil.copytree(os.path.join(ROOT, "img"), os.path.join(self.out, "img"), dirs_exist_ok=True)

    def sve(self):
        self.staticno()
        for lang in JEZICI:
            self.pocetna(lang)
            for t in TEKSTOVI:
                self.tekst(t, lang)
        if not self.pregled:
            self.stranica_404()
        self.sitemap()


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--pregled":
        out = os.path.abspath(sys.argv[2])
        if os.path.exists(out):
            shutil.rmtree(out)
        os.makedirs(out)
        Gradnja(out, pregled=True).sve()
    else:
        # očisti stare generirane stranice prije gradnje
        for d in ["tekstovi", "en", "it"]:
            p = os.path.join(ROOT, d)
            if os.path.isdir(p):
                shutil.rmtree(p)
        Gradnja(ROOT, pregled=False).sve()
    print("Gotovo.")
