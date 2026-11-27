import os

os.makedirs("assets", exist_ok=True)


def write(filename, content):
    with open(os.path.join("assets", filename), "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")


# 1. Texto animado que escribe y borra (Inglés y Español)
def make_typing_svg(lines):
    paths_and_texts = []
    n = len(lines)
    for i, (text, start_x, length) in enumerate(lines):
        begin = f"0s;d{n-1}.end" if i == 0 else f"d{i-1}.end"
        paths_and_texts.append(f'''
  <path id="p{i}" d="m0,30 h0">
    <animate id="d{i}" attributeName="d"
      begin="{begin}" dur="3.6s" fill="remove"
      values="m{start_x},30 h0 ; m{start_x},30 h{length} ; m{start_x},30 h{length} ; m{start_x},30 h0"
      keyTimes="0;0.45;0.82;1" />
  </path>
  <text class="txt"><textPath href="#p{i}">{text}</textPath></text>''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 46" width="720" height="46">
  <style>
    .txt {{
      font-family: 'Fira Code', 'Cascadia Code', Consolas, 'Courier New', monospace;
      font-size: 20px;
      font-weight: 600;
      fill: #00D8FF;
    }}
  </style>{"".join(paths_and_texts)}
</svg>'''


write("typing-en.svg", make_typing_svg([
    ("> Mobile & Full-Stack Developer", 164, 410),
    ("> AI & Data Science Enthusiast", 170, 400),
    ("> Learning Networking & Ethical Hacking", 112, 510),
    ("> Halo · Spider-Man · Pokémon", 176, 390),
]))

write("typing-es.svg", make_typing_svg([
    ("> Desarrollador Mobile & Full-Stack", 140, 455),
    ("> Entusiasta de IA & Ciencia de Datos", 128, 480),
    ("> Aprendiendo Redes & Hacking Ético", 140, 455),
    ("> Halo · Spider-Man · Pokémon", 176, 390),
]))


# 2. Botones de switch de idioma
def make_lang_btn(label, active):
    bg = "#0d1117" if active else "#161b22"
    border = "#00D8FF" if active else "#30363d"
    color = "#00D8FF" if active else "#8b949e"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 116 30" width="116" height="30">
  <rect x="1" y="1" width="114" height="28" rx="6" fill="{bg}" stroke="{border}" stroke-width="1.5"/>
  <text x="58" y="20" text-anchor="middle" font-family="Segoe UI, Ubuntu, sans-serif" font-size="12" font-weight="700" letter-spacing="1.2" fill="{color}">{label}</text>
</svg>'''


write("lang-en-on.svg", make_lang_btn("ENGLISH", True))
write("lang-en-off.svg", make_lang_btn("ENGLISH", False))
write("lang-es-on.svg", make_lang_btn("ESPAÑOL", True))
write("lang-es-off.svg", make_lang_btn("ESPAÑOL", False))


# 3. Separador visual animado: Halo + Spider-Man + Pokémon
write("showcase.svg", '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 132" width="800" height="132">
  <defs>
    <radialGradient id="gHalo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#F5A623" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="gSpidey" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#E62429" stop-opacity="0.30"/>
      <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="gPoke" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FF6B00" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0d1117"/>
      <stop offset="23%" stop-color="#F5A623"/>
      <stop offset="50%" stop-color="#E62429"/>
      <stop offset="77%" stop-color="#FF6B00"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
  </defs>

  <rect width="800" height="132" rx="12" fill="#0d1117" stroke="#21262d" stroke-width="1"/>

  <!-- Línea de circuito + pulso viajando -->
  <line x1="40" y1="58" x2="760" y2="58" stroke="url(#lineGrad)" stroke-width="1.5" opacity="0.55"/>
  <circle cy="58" r="3" fill="#00D8FF">
    <animate attributeName="cx" values="40;760;40" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.2;1;0.2" dur="6s" repeatCount="indefinite"/>
  </circle>

  <!-- HALO (Izquierda) -->
  <g transform="translate(185, 58)">
    <circle r="44" fill="url(#gHalo)"/>
    <circle r="32" fill="none" stroke="#21262d" stroke-width="1" stroke-dasharray="4 4"/>
    <!-- Anillo Halo -->
    <ellipse rx="30" ry="12" transform="rotate(-24)" fill="none" stroke="#00D8FF" stroke-width="2.5">
      <animate attributeName="opacity" values="0.65;1;0.65" dur="3s" repeatCount="indefinite"/>
    </ellipse>
    <ellipse rx="24" ry="8" transform="rotate(-24)" fill="none" stroke="#F5A623" stroke-width="1.6"/>
    <!-- Silueta visor Spartan minimalista -->
    <polygon points="-14,-8 14,-8 18,0 10,9 -10,9 -18,0" fill="#F5A623" opacity="0.92"/>
    <polygon points="-11,-5 11,-5 14,0 8,6 -8,6 -14,0" fill="#161b22" opacity="0.35"/>
    <text y="55" text-anchor="middle" font-family="Segoe UI, Ubuntu, sans-serif" font-size="10" font-weight="700" letter-spacing="4" fill="#8b949e">HALO</text>
  </g>

  <!-- SPIDER-MAN (Centro) -->
  <g transform="translate(400, 58)">
    <circle r="46" fill="url(#gSpidey)"/>
    <!-- Telaraña geométrica sutil -->
    <circle r="33" fill="none" stroke="#1f6feb" stroke-width="0.9" opacity="0.45"/>
    <circle r="21" fill="none" stroke="#1f6feb" stroke-width="0.8" opacity="0.35"/>
    <line x1="-33" y1="0" x2="33" y2="0" stroke="#1f6feb" stroke-width="0.7" opacity="0.3"/>
    <line x1="0" y1="-33" x2="0" y2="33" stroke="#1f6feb" stroke-width="0.7" opacity="0.3"/>
    <!-- Emblema Spider-Man -->
    <g fill="#E62429" stroke="#E62429" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
      <ellipse cx="0" cy="-7" rx="3.5" ry="4.5"/>
      <polygon points="0,-1 6,8 0,18 -6,8"/>
      <!-- Patas izquierdas -->
      <polyline points="-3,-6 -13,-15 -18,-22" fill="none"/>
      <polyline points="-4,-2 -17,-8 -24,-12" fill="none"/>
      <polyline points="-4,3 -17,6 -23,14" fill="none"/>
      <polyline points="-3,8 -12,17 -15,25" fill="none"/>
      <!-- Patas derechas -->
      <polyline points="3,-6 13,-15 18,-22" fill="none"/>
      <polyline points="4,-2 17,-8 24,-12" fill="none"/>
      <polyline points="4,3 17,6 23,14" fill="none"/>
      <polyline points="3,8 12,17 15,25" fill="none"/>
      <animate attributeName="opacity" values="0.75;1;0.75" dur="2.6s" repeatCount="indefinite"/>
    </g>
    <text y="55" text-anchor="middle" font-family="Segoe UI, Ubuntu, sans-serif" font-size="10" font-weight="700" letter-spacing="4" fill="#8b949e">SPIDER-MAN</text>
  </g>

  <!-- POKÉMON (Derecha) -->
  <g transform="translate(615, 58)">
    <circle r="44" fill="url(#gPoke)"/>
    <circle r="32" fill="none" stroke="#21262d" stroke-width="1" stroke-dasharray="4 4"/>
    <!-- Pokéball minimalista neón -->
    <path d="M -23,0 A 23,23 0 0,1 23,0 Z" fill="#FF6B00" opacity="0.9"/>
    <path d="M -23,0 A 23,23 0 0,0 23,0 Z" fill="#E6EDF3" opacity="0.9"/>
    <line x1="-24" y1="0" x2="24" y2="0" stroke="#0d1117" stroke-width="4"/>
    <circle r="8.5" fill="#0d1117"/>
    <circle r="4.8" fill="#FFD600">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2.2s" repeatCount="indefinite"/>
    </circle>
    <text y="55" text-anchor="middle" font-family="Segoe UI, Ubuntu, sans-serif" font-size="10" font-weight="700" letter-spacing="4" fill="#8b949e">POKÉMON</text>
  </g>
</svg>''')


# 4. Badges de Stack Tecnológico (estilo for-the-badge local)
rows = [
    [
        ("REACT NATIVE", 136, "#20232A", "#61DAFB"),
        ("EXPO", 78, "#1B1F24", "#FFFFFF"),
        ("TYPESCRIPT", 118, "#3178C6", "#FFFFFF"),
        ("JAVASCRIPT", 118, "#F7DF1E", "#0D1117"),
        ("PYTHON", 92, "#3776AB", "#FFFFFF"),
    ],
    [
        ("POSTGRESQL", 122, "#336791", "#FFFFFF"),
        ("SUPABASE", 108, "#3ECF8E", "#0D1117"),
        ("FIREBASE", 104, "#FFCA28", "#0D1117"),
        ("DOCKER", 94, "#2496ED", "#FFFFFF"),
        ("GCP", 68, "#4285F4", "#FFFFFF"),
        ("AWS", 68, "#FF9900", "#0D1117"),
    ],
    [
        ("GIT", 64, "#F05032", "#FFFFFF"),
        ("GITHUB ACTIONS", 148, "#2088FF", "#FFFFFF"),
        ("JIRA", 72, "#0052CC", "#FFFFFF"),
        ("LINUX", 80, "#FCC624", "#0D1117"),
        ("NETWORKING", 122, "#00B894", "#0D1117"),
        ("ETHICAL HACKING", 154, "#E62429", "#FFFFFF"),
    ],
]

gap = 10
badge_h = 34
svg_badges = []
for r_idx, row in enumerate(rows):
    total_w = sum(item[1] for item in row) + gap * (len(row) - 1)
    x = (800 - total_w) / 2
    y = 8 + r_idx * 44
    for label, w, bg, fg in row:
        border = ' stroke="#30363d" stroke-width="1"' if bg in ("#20232A", "#1B1F24") else ""
        svg_badges.append(
            f'  <rect x="{x:.1f}" y="{y}" width="{w}" height="{badge_h}" rx="4" fill="{bg}"{border}/>\n'
            f'  <text x="{x + w/2:.1f}" y="{y + 21.5}" text-anchor="middle" font-family="Segoe UI, Ubuntu, sans-serif" '
            f'font-size="11.5" font-weight="800" letter-spacing="1" fill="{fg}">{label}</text>'
        )
        x += w + gap

write("stack.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 144" width="800" height="144">
{chr(10).join(svg_badges)}
</svg>''')


# 5. Tarjetas de Contacto mejoradas
def make_contact_card(title, handle, accent, icon_svg):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 246 62" width="246" height="62">
  <rect x="1" y="1" width="244" height="60" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1.2"/>
  <rect x="1" y="1" width="6" height="60" rx="3" fill="{accent}"/>
  <g transform="translate(22, 19)">{icon_svg}</g>
  <text x="58" y="27" font-family="Segoe UI, Ubuntu, sans-serif" font-size="13" font-weight="800" letter-spacing="1" fill="#ffffff">{title}</text>
  <text x="58" y="45" font-family="Consolas, monospace" font-size="11" fill="{accent}">{handle}</text>
</svg>'''


write("contact-gmail.svg", make_contact_card(
    "GMAIL", "alejossalvador@gmail.com", "#EA4335",
    '<rect width="24" height="18" y="3" rx="3" fill="none" stroke="#EA4335" stroke-width="2"/>'
    '<polyline points="2,5 12,13 22,5" fill="none" stroke="#EA4335" stroke-width="2"/>'
))

write("contact-linkedin.svg", make_contact_card(
    "LINKEDIN", "in/salvaalejos", "#0A66C2",
    '<rect width="22" height="22" y="1" rx="4" fill="#0A66C2"/>'
    '<text x="11" y="17" text-anchor="middle" font-family="Segoe UI, sans-serif" font-size="14" font-weight="900" fill="#ffffff">in</text>'
))

write("contact-instagram.svg", make_contact_card(
    "INSTAGRAM", "@saalvaalejos", "#E4405F",
    '<rect width="22" height="22" y="1" rx="6" fill="none" stroke="#E4405F" stroke-width="2"/>'
    '<circle cx="11" cy="12" r="5" fill="none" stroke="#E4405F" stroke-width="2"/>'
    '<circle cx="17" cy="6" r="1.4" fill="#E4405F"/>'
))

print("Listo! Se crearon todos los SVG en la carpeta assets/")
