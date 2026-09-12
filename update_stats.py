import urllib.request
import json
import os
from datetime import datetime

# --- CONFIGURATION ---
MS_MARKETPLACE_ID = "likhith-adithya.ai-cli-pro"
OPEN_VSX_ID = "likhith-adithya/ai-cli-pro"
STATS_FILE = "stats.json"
SVG_FILE = "downloads_graph.svg"
BADGE_FILE = "download_badge.svg"
MAX_POINTS = 30 

def get_ms_marketplace_downloads():
    url = "https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery"
    headers = {
        "Accept": "application/json; charset=utf-8; api-version=7.2-preview.1",
        "Content-Type": "application/json"
    }
    body = json.dumps({
        "filters": [{"criteria": [{"filterType": 7, "value": MS_MARKETPLACE_ID}]}],
        "flags": 914
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=body, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            stats = data['results'][0]['extensions'][0]['statistics']
            installs = next(s['value'] for s in stats if s['statisticName'] == 'install')
            return int(installs)
    except Exception as e:
        return 0

def get_open_vsx_downloads():
    url = f"https://open-vsx.org/api/{OPEN_VSX_ID}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
            return int(data.get('downloadCount', 0))
    except Exception as e:
        return 0

def generate_svg(history):
    if not history:
        return

    values = [point['count'] for point in history]
    if not values:
        return

    current_count = values[-1]
    min_val, max_val = min(values), max(values)
    graph_min = min_val * 0.9 if min_val > 0 else 0
    graph_max = max_val * 1.12 if max_val > 0 else 1
    range_val = max(graph_max - graph_min, 1)

    width, height = 760, 220
    padding_x = 52
    padding_top = 30
    padding_bottom = 32
    chart_height = height - padding_top - padding_bottom

    points = []
    for i, val in enumerate(values):
        x = padding_x + (i * (width - 2 * padding_x) / (len(values) - 1 if len(values) > 1 else 1))
        y = (height - padding_bottom) - ((val - graph_min) / range_val * chart_height)
        points.append((x, y))

    polyline_points = " ".join(f"{x},{y}" for x, y in points)

    grid_lines = []
    for i in range(5):
        level = padding_top + (chart_height / 4) * i
        grid_lines.append(f'<line x1="{padding_x}" y1="{level}" x2="{width-padding_x}" y2="{level}" stroke="#ffffff" stroke-opacity="0.08" stroke-width="1"/>')

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Global adoption trend">
    <defs>
        <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#f7f9fc"/>
            <stop offset="100%" stop-color="#eef4fb"/>
        </linearGradient>
        <linearGradient id="lineGrad" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#8b5cf6"/>
            <stop offset="50%" stop-color="#3b82f6"/>
            <stop offset="100%" stop-color="#10b981"/>
        </linearGradient>
        <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.14"/>
            <stop offset="50%" stop-color="#3b82f6" stop-opacity="0.08"/>
            <stop offset="100%" stop-color="#3b82f6" stop-opacity="0"/>
        </linearGradient>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="3.5" result="blur"/>
            <feMerge>
                <feMergeNode in="blur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>

    <rect x="0" y="0" width="{width}" height="{height}" rx="22" fill="url(#bg)"/>
    <rect x="8" y="8" width="{width-16}" height="{height-16}" rx="18" fill="#ffffff" fill-opacity="0.38" stroke="#dfe7f3"/>

    <g opacity="0.9">
        {''.join(grid_lines)}
    </g>

    <text x="{padding_x}" y="22" font-family="SF Pro Display, Segoe UI, Arial, sans-serif" font-size="11" font-weight="700" letter-spacing="1.8" fill="#53677c">AI CLI PRO</text>
    <text x="{width-padding_x}" y="38" font-family="SF Pro Display, Segoe UI, Arial, sans-serif" font-size="30" font-weight="700" fill="#0f172a" text-anchor="end">{current_count}</text>
    <text x="{width-padding_x}" y="58" font-family="SF Pro Display, Segoe UI, Arial, sans-serif" font-size="11" font-weight="600" letter-spacing="1.6" fill="#64748b" text-anchor="end">TOTAL INSTALLS</text>

    <path d="M {padding_x} {height-padding_bottom} L {polyline_points} L {width-padding_x} {height-padding_bottom} Z" fill="url(#areaGrad)"/>
    <polyline points="{polyline_points}" fill="none" stroke="url(#lineGrad)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" filter="url(#glow)"/>
    <circle cx="{points[-1][0]}" cy="{points[-1][1]}" r="6" fill="#ffffff" stroke="#4f46e5" stroke-width="3"/>

    <text x="{padding_x}" y="{height-12}" font-family="SF Pro Display, Segoe UI, Arial, sans-serif" font-size="10" fill="#94a3b8">{history[0]['date']}</text>
    <text x="{width-padding_x}" y="{height-12}" font-family="SF Pro Display, Segoe UI, Arial, sans-serif" font-size="10" fill="#94a3b8" text-anchor="end">{history[-1]['date']}</text>
    </svg>'''

    with open(SVG_FILE, "w") as f:
        f.write(svg)

    badge_svg = f'''<svg width="240" height="76" viewBox="0 0 240 76" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="AI CLI PRO downloads badge">
    <defs>
        <linearGradient id="badgeBg" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#0b1020"/>
            <stop offset="100%" stop-color="#111827"/>
        </linearGradient>
        <linearGradient id="badgeLine" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#7dd3fc"/>
            <stop offset="50%" stop-color="#818cf8"/>
            <stop offset="100%" stop-color="#34d399"/>
        </linearGradient>
        <filter id="badgeShadow" x="-10%" y="-10%" width="120%" height="140%">
            <feDropShadow dx="0" dy="10" stdDeviation="10" flood-color="#0f172a" flood-opacity="0.22"/>
        </filter>
    </defs>

    <g filter="url(#badgeShadow)">
        <rect x="1" y="1" width="238" height="74" rx="18" fill="url(#badgeBg)" stroke="#dbeafe" stroke-opacity="0.12"/>
        <rect x="14" y="12" width="212" height="52" rx="13" fill="#0f172a" fill-opacity="0.72"/>
        <text x="28" y="28" font-family="SF Pro Display, Segoe UI, Arial, sans-serif" font-size="9" font-weight="700" letter-spacing="1.8" fill="#7dd3fc">GLOBAL DOWNLOADS</text>
        <text x="28" y="49" font-family="SF Pro Display, Segoe UI, Arial, sans-serif" font-size="26" font-weight="800" fill="#f8fafc">{current_count}</text>
        <rect x="164" y="19" width="48" height="21" rx="10.5" fill="url(#badgeLine)"/>
        <text x="188" y="34" text-anchor="middle" font-family="SF Pro Display, Segoe UI, Arial, sans-serif" font-size="8.5" font-weight="700" fill="#06111d">LIVE</text>
    </g>
    </svg>'''

    with open(BADGE_FILE, "w") as f:
        f.write(badge_svg)

# Main Execution
ms_count = get_ms_marketplace_downloads()
ovsx_count = get_open_vsx_downloads()
total_count = ms_count + ovsx_count

today = datetime.now().strftime("%Y-%m-%d")

if os.path.exists(STATS_FILE):
    with open(STATS_FILE, "r") as f:
        history = json.load(f)
else:
    history = []

if history and history[-1]['date'] == today:
    history[-1]['count'] = total_count
else:
    history.append({"date": today, "count": total_count})
    history = history[-MAX_POINTS:]

with open(STATS_FILE, "w") as f:
    json.dump(history, f)

generate_svg(history)
