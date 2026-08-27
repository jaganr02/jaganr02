import base64
import os

with open('e:/github-portfolio/assets/dithered-portrait-hd.png', 'rb') as f:
    dither_b64 = base64.b64encode(f.read()).decode('utf-8')

svg_content = f'''<svg width="100%" height="auto" viewBox="0 0 920 540" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" />
      <stop offset="100%" stop-color="#f1f5f9" />
    </linearGradient>

    <!-- Card Surface Gradient -->
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="100%" stop-color="#ffffff" />
    </linearGradient>

    <!-- Drop Shadows -->
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="14" stdDeviation="22" flood-color="#64748b" flood-opacity="0.14" />
    </filter>

    <filter id="searchShadow" x="-5%" y="-10%" width="110%" height="130%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#94a3b8" flood-opacity="0.18" />
    </filter>

    <!-- Blueprint Grid -->
    <pattern id="subtleGrid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#e2e8f0" stroke-width="1" />
    </pattern>

    <style>
      @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}
      @keyframes flowH {{
        0% {{ stroke-dashoffset: 40; }}
        100% {{ stroke-dashoffset: 0; }}
      }}
      @keyframes flowV {{
        0% {{ stroke-dashoffset: 20; }}
        100% {{ stroke-dashoffset: 0; }}
      }}
      @keyframes pulseDot {{
        0%, 100% {{ transform: scale(1); opacity: 1; }}
        50% {{ transform: scale(1.3); opacity: 0.6; }}
      }}
      /* Smooth Looping Title Alternations */
      @keyframes roleCycle1 {{
        0%, 28% {{ opacity: 1; transform: translateY(0px); }}
        33%, 95% {{ opacity: 0; transform: translateY(8px); }}
        100% {{ opacity: 1; transform: translateY(0px); }}
      }}
      @keyframes roleCycle2 {{
        0%, 28% {{ opacity: 0; transform: translateY(-8px); }}
        33%, 61% {{ opacity: 1; transform: translateY(0px); }}
        66%, 100% {{ opacity: 0; transform: translateY(8px); }}
      }}
      @keyframes roleCycle3 {{
        0%, 61% {{ opacity: 0; transform: translateY(-8px); }}
        66%, 95% {{ opacity: 1; transform: translateY(0px); }}
        100% {{ opacity: 0; transform: translateY(8px); }}
      }}

      .cursor {{
        animation: blink 1s infinite;
      }}
      .flow-line-h {{
        stroke-dasharray: 4, 4;
        animation: flowH 1.4s linear infinite;
      }}
      .flow-line-v {{
        stroke-dasharray: 4, 4;
        animation: flowV 1.4s linear infinite;
      }}
      .status-pulse {{
        transform-origin: center;
        animation: pulseDot 2s ease-in-out infinite;
      }}
      .role-1 {{ animation: roleCycle1 9s ease-in-out infinite; }}
      .role-2 {{ animation: roleCycle2 9s ease-in-out infinite; }}
      .role-3 {{ animation: roleCycle3 9s ease-in-out infinite; }}

      .text-title {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-weight: 800;
        font-size: 32px;
        fill: #7c3aed;
        letter-spacing: -0.5px;
      }}
      .text-sub {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-weight: 600;
        font-size: 14.5px;
        fill: #0284c7;
      }}
      .text-meta {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-weight: 500;
        font-size: 12px;
        fill: #475569;
      }}
      .text-quote {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-style: italic;
        font-weight: 500;
        font-size: 12.5px;
        fill: #6366f1;
      }}
      .text-contact {{
        font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace;
        font-size: 11px;
        fill: #64748b;
      }}
      .text-diag {{
        font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace;
        font-size: 9px;
        font-weight: 600;
        fill: #64748b;
      }}
    </style>
  </defs>

  <!-- Outer Canvas Frame -->
  <rect width="920" height="540" rx="24" fill="url(#bgGradient)" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="8 8" />
  <rect width="920" height="540" rx="24" fill="url(#subtleGrid)" opacity="0.75" />

  <!-- ================= TOP QUERY INPUT ================= -->
  <g transform="translate(80, 26)">
    <rect width="360" height="44" rx="22" fill="#ffffff" filter="url(#searchShadow)" stroke="#e2e8f0" stroke-width="1" />
    <text x="24" y="27" font-family="'SF Mono', Consolas, monospace" font-size="14" font-weight="600" fill="#0284c7">&gt;</text>
    <text x="42" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="14" font-weight="500" fill="#1e293b">&quot;who is Jagan R?&quot;</text>
    <rect x="186" y="14" width="9" height="17" fill="#0284c7" class="cursor" />
  </g>

  <!-- Vertical Connecting Line from Query Search Bar Down to Node 1 -->
  <path d="M 235 70 L 235 110" stroke="#0284c7" stroke-width="1.5" class="flow-line-v" opacity="0.7" />

  <!-- Pipeline Header & Status -->
  <text x="480" y="52" font-family="'SF Mono', Consolas, monospace" font-size="11" font-weight="600" fill="#64748b" letter-spacing="1.5">RAG PIPELINE / PROFILE v2.0</text>
  <text x="780" y="52" font-family="'SF Mono', Consolas, monospace" font-size="11" font-weight="600" fill="#64748b">online</text>
  <circle cx="832" cy="48" r="4" fill="#22c55e" class="status-pulse" />

  <!-- ================= PIPELINE HORIZONTAL NODES ================= -->
  <g transform="translate(40, 95)">
    <!-- Main horizontal flow path -->
    <path d="M 195 38 L 735 38" stroke="#0284c7" stroke-width="1.5" class="flow-line-h" opacity="0.6" />

    <!-- Node 1: Query Embedding -->
    <g transform="translate(170, 14)">
      <circle cx="25" cy="24" r="23" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" />
      <circle cx="25" cy="24" r="5" fill="#0284c7" />
      <text x="25" y="60" text-anchor="middle" class="text-diag">1 · QUERY</text>
      <text x="25" y="70" text-anchor="middle" class="text-diag">EMBEDDING</text>
    </g>

    <!-- Node 2: Qdrant Vector Store -->
    <g transform="translate(280, 10)">
      <!-- 3D Vector DB cylinder -->
      <ellipse cx="40" cy="12" rx="34" ry="10" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5" />
      <path d="M 6 12 v 12 a 34 10 0 0 0 68 0 v -12" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5" />
      <path d="M 6 24 v 12 a 34 10 0 0 0 68 0 v -12" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5" />
      <text x="40" y="16" text-anchor="middle" font-family="'SF Mono', Consolas, monospace" font-size="9.5" font-weight="700" fill="#7c3aed">Qdrant</text>
      <text x="40" y="64" text-anchor="middle" class="text-diag">2 · SIMILARITY</text>
      <text x="40" y="74" text-anchor="middle" class="text-diag">SEARCH</text>
    </g>

    <!-- Node 3: Top-K Chunks -->
    <g transform="translate(395, 12)">
      <rect x="0" y="0" width="50" height="13" rx="3" fill="#ffffff" stroke="#38bdf8" stroke-width="1" />
      <text x="25" y="9" text-anchor="middle" font-family="'SF Mono', monospace" font-size="7" font-weight="600" fill="#0284c7">chunk 1</text>
      
      <rect x="0" y="16" width="50" height="13" rx="3" fill="#ffffff" stroke="#38bdf8" stroke-width="1" />
      <text x="25" y="25" text-anchor="middle" font-family="'SF Mono', monospace" font-size="7" font-weight="600" fill="#0284c7">chunk 2</text>

      <rect x="0" y="32" width="50" height="13" rx="3" fill="#ffffff" stroke="#38bdf8" stroke-width="1" />
      <text x="25" y="41" text-anchor="middle" font-family="'SF Mono', monospace" font-size="7" font-weight="600" fill="#0284c7">chunk 3</text>
      
      <text x="25" y="62" text-anchor="middle" class="text-diag">3 · TOP-K</text>
      <text x="25" y="72" text-anchor="middle" class="text-diag">CHUNKS</text>
    </g>

    <!-- Node 4: Prompt Construction -->
    <g transform="translate(485, 12)">
      <rect x="0" y="0" width="84" height="48" rx="8" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5" />
      <text x="42" y="28" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9.5" font-weight="700" fill="#7c3aed">PROMPT</text>
      <text x="42" y="62" text-anchor="middle" class="text-diag">4 · PROMPT CONSTRUCT</text>
      <text x="42" y="72" text-anchor="middle" class="text-diag">(query + context)</text>
    </g>

    <!-- Node 5: LLM Generation -->
    <g transform="translate(605, 12)">
      <rect x="0" y="0" width="84" height="48" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" />
      <text x="42" y="28" text-anchor="middle" font-family="'SF Mono', monospace" font-size="10" font-weight="700" fill="#0284c7">LLM</text>
      <text x="42" y="62" text-anchor="middle" class="text-diag">5 · GENERATION</text>
    </g>

    <!-- Node 6: Final Answer -->
    <g transform="translate(725, 14)">
      <circle cx="25" cy="24" r="23" fill="#ffffff" stroke="#22c55e" stroke-width="1.8" />
      <text x="25" y="60" text-anchor="middle" class="text-diag">FINAL</text>
      <text x="25" y="70" text-anchor="middle" class="text-diag">ANSWER</text>
    </g>
  </g>

  <!-- Vertical Connecting Line from Final Answer Down to Profile Card -->
  <path d="M 790 178 L 790 236" stroke="#22c55e" stroke-width="1.5" class="flow-line-v" opacity="0.8" />

  <!-- ================= STREAMING TERMINAL PROFILE CARD ================= -->
  <g transform="translate(80, 235)">
    <!-- Card Frame -->
    <rect width="760" height="255" rx="18" fill="url(#cardBg)" filter="url(#cardShadow)" stroke="#e2e8f0" stroke-width="1" />

    <!-- Terminal Window Top Control Dots -->
    <circle cx="24" cy="22" r="5" fill="#ef4444" />
    <circle cx="38" cy="22" r="5" fill="#f59e0b" />
    <circle cx="52" cy="22" r="5" fill="#10b981" />
    <text x="72" y="26" font-family="'SF Mono', Consolas, monospace" font-size="11" fill="#64748b">generated_profile.md · streaming...</text>

    <!-- Candidate Name -->
    <text x="24" y="65" class="text-title">R JAGAN</text>

    <!-- Cycling Animated Roles -->
    <g transform="translate(24, 88)">
      <text x="0" y="0" class="text-sub role-1">AI Engineer • Generative AI &amp; Multi-Agent Systems</text>
      <text x="0" y="0" class="text-sub role-2">Machine Learning Engineer • RAG &amp; Vector Search</text>
      <text x="0" y="0" class="text-sub role-3">Intelligent Systems Developer • FastAPI &amp; Python</text>
    </g>

    <!-- Meta Details Row -->
    <g transform="translate(24, 110)">
      <text x="0" y="0" class="text-meta">🎓 B.Tech - AI &amp; DS</text>
      <text x="170" y="0" class="text-meta">📍 India</text>
      <text x="245" y="0" class="text-meta">🛠️ building Multi-Agent &amp; RAG systems</text>
    </g>

    <!-- Tech Skill Pills Row 1 -->
    <g transform="translate(24, 124)">
      <!-- Python -->
      <rect x="0" y="0" width="66" height="22" rx="11" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1" />
      <circle cx="9" cy="11" r="3" fill="#16a34a" />
      <text x="18" y="15" font-family="'SF Mono', monospace" font-size="10" font-weight="600" fill="#166534">Python</text>

      <!-- FastAPI -->
      <rect x="74" y="0" width="70" height="22" rx="11" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1" />
      <circle cx="83" cy="11" r="3" fill="#0d9488" />
      <text x="92" y="15" font-family="'SF Mono', monospace" font-size="10" font-weight="600" fill="#115e59">FastAPI</text>

      <!-- LangGraph -->
      <rect x="152" y="0" width="86" height="22" rx="11" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1" />
      <circle cx="161" cy="11" r="3" fill="#9333ea" />
      <text x="170" y="15" font-family="'SF Mono', monospace" font-size="10" font-weight="600" fill="#6b21a8">LangGraph</text>

      <!-- RAG -->
      <rect x="246" y="0" width="56" height="22" rx="11" fill="#f5f3ff" stroke="#ddd6fe" stroke-width="1" />
      <circle cx="255" cy="11" r="3" fill="#7c3aed" />
      <text x="264" y="15" font-family="'SF Mono', monospace" font-size="10" font-weight="600" fill="#5b21b6">RAG</text>

      <!-- Qdrant -->
      <rect x="310" y="0" width="70" height="22" rx="11" fill="#fef2f2" stroke="#fecaca" stroke-width="1" />
      <circle cx="319" cy="11" r="3" fill="#dc2626" />
      <text x="328" y="15" font-family="'SF Mono', monospace" font-size="10" font-weight="600" fill="#991b1b">Qdrant</text>

      <!-- Scikit-Learn -->
      <rect x="388" y="0" width="94" height="22" rx="11" fill="#fffbeb" stroke="#fde68a" stroke-width="1" />
      <circle cx="397" cy="11" r="3" fill="#d97706" />
      <text x="406" y="15" font-family="'SF Mono', monospace" font-size="10" font-weight="600" fill="#92400e">scikit-learn</text>
    </g>

    <!-- Tech Skill Pills Row 2 -->
    <g transform="translate(24, 152)">
      <!-- MCP -->
      <rect x="0" y="0" width="56" height="22" rx="11" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1" />
      <circle cx="9" cy="11" r="3" fill="#16a34a" />
      <text x="18" y="15" font-family="'SF Mono', monospace" font-size="10" font-weight="600" fill="#166534">MCP</text>

      <!-- LangChain -->
      <rect x="64" y="0" width="86" height="22" rx="11" fill="#f5f3ff" stroke="#ddd6fe" stroke-width="1" />
      <circle cx="73" cy="11" r="3" fill="#7c3aed" />
      <text x="82" y="15" font-family="'SF Mono', monospace" font-size="10" font-weight="600" fill="#5b21b6">LangChain</text>

      <!-- Docker -->
      <rect x="158" y="0" width="70" height="22" rx="11" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1" />
      <circle cx="167" cy="11" r="3" fill="#0284c7" />
      <text x="176" y="15" font-family="'SF Mono', monospace" font-size="10" font-weight="600" fill="#0369a1">Docker</text>

      <!-- MySQL -->
      <rect x="236" y="0" width="66" height="22" rx="11" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1" />
      <circle cx="245" cy="11" r="3" fill="#2563eb" />
      <text x="254" y="15" font-family="'SF Mono', monospace" font-size="10" font-weight="600" fill="#1e40af">MySQL</text>
    </g>

    <!-- Motto Quote -->
    <text x="24" y="196" class="text-quote">&quot;Learn relentlessly. Build fearlessly. Ship something that matters.&quot;</text>

    <!-- Contact Line with Blinking Cursor -->
    <text x="24" y="224" class="text-contact">in/r-jagan-52bb94289 · rajajagan697@gmail.com</text>
    <rect x="375" y="213" width="6" height="13" fill="#0284c7" class="cursor" />

    <!-- Right Side: High-Definition Stylized Subject Rendering -->
    <g transform="translate(545, 12)">
      <text x="65" y="14" text-anchor="middle" font-family="'SF Mono', monospace" font-size="9" fill="#94a3b8">⚡ rendering subject...</text>
      
      <!-- Portrait Card Surface -->
      <g transform="translate(0, 20)">
        <rect x="0" y="0" width="130" height="165" rx="12" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
        <clipPath id="portraitClip">
          <rect x="2" y="2" width="126" height="161" rx="10" />
        </clipPath>
        
        <!-- HD Base64 Embedded Stylized Portrait -->
        <image href="data:image/png;base64,{dither_b64}" x="0" y="0" width="130" height="165" clip-path="url(#portraitClip)" preserveAspectRatio="xMidYMid slice" />
        
        <!-- Status Pill -->
        <g transform="translate(18, 172)">
          <rect x="0" y="0" width="94" height="18" rx="9" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
          <circle cx="10" cy="9" r="3" fill="#22c55e" />
          <text x="18" y="13" font-family="'SF Mono', monospace" font-size="9" font-weight="600" fill="#334155">jaganr02</text>
        </g>
      </g>
    </g>
  </g>

  <!-- Bottom Telemetry Status Line -->
  <g transform="translate(80, 510)">
    <text x="0" y="0" font-family="'SF Mono', Consolas, monospace" font-size="10" fill="#64748b">
      retrieved: <tspan fill="#0284c7" font-weight="600">top-k chunks</tspan>  ·  latency: <tspan fill="#334155" font-weight="600">38 ms</tspan>  ·  throughput: <tspan fill="#334155" font-weight="600">94 tok/s</tspan>  ·  context: <tspan fill="#16a34a" font-weight="600">grounded ✓</tspan>
    </text>
    <text x="760" y="0" text-anchor="end" font-family="'SF Mono', Consolas, monospace" font-size="10" font-weight="600" fill="#64748b">
      github.com/jaganr02
    </text>
  </g>
</svg>'''

with open('e:/github-portfolio/assets/hero.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print('Updated hero.svg generated with RAG & MCP pills (MongoDB removed)!')
