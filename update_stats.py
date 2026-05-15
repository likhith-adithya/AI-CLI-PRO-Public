import urllib.request
import json
import os
from datetime import datetime

# --- CONFIGURATION ---
MS_MARKETPLACE_ID = "likhith-adithya.ai-cli-pro"
OPEN_VSX_ID = "likhith-adithya/ai-cli-pro"
STATS_FILE = "stats.json"
SVG_FILE = "downloads_graph.svg"
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
        print(f"Error fetching MS Marketplace stats: {e}")
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
    if not history: return
    
    values = [point['count'] for point in history]
    if not values: return
    
    min_val, max_val = min(values), max(values)
    # Ensure graph has room at top/bottom
    graph_min = min_val * 0.8
    graph_max = max_val * 1.2
    range_val = max(graph_max - graph_min, 1)
    
    width, height = 600, 200
    padding_x = 50
    padding_y = 40
    
    points = []
    for i, val in enumerate(values):
        x = padding_x + (i * (width - 2 * padding_x) / (len(values) - 1 if len(values) > 1 else 1))
        y = (height - padding_y) - ((val - graph_min) / range_val * (height - 2 * padding_y))
        points.append((x, y))
    
    polyline_points = " ".join([f"{x},{y}" for x, y in points])
    
    # Area path (closes the loop at the bottom)
    area_points = f"{padding_x},{height-padding_y} " + polyline_points + f" {width-padding_x},{height-padding_y}"
    
    svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="areaGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#4facfe;stop-opacity:0.3" />
            <stop offset="100%" style="stop-color:#4facfe;stop-opacity:0" />
        </linearGradient>
        <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1" />
        </linearGradient>
        <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur in="SourceAlpha" stdDeviation="3" />
            <feOffset dx="0" dy="2" result="offsetblur" />
            <feComponentTransfer>
                <feFuncA type="linear" slope="0.5" />
            </feComponentTransfer>
            <feMerge>
                <feMergeNode />
                <feMergeNode in="SourceGraphic" />
            </feMerge>
        </filter>
    </defs>
    
    <!-- Background -->
    <rect width="100%" height="100%" fill="transparent"/>
    
    <!-- Grid Lines -->
    <line x1="{padding_x}" y1="{height-padding_y}" x2="{width-padding_x}" y2="{height-padding_y}" stroke="#333" stroke-width="1" />
    <line x1="{padding_x}" y1="{padding_y}" x2="{width-padding_x}" y2="{padding_y}" stroke="#222" stroke-width="1" stroke-dasharray="4" />
    
    <!-- Area Fill -->
    <polygon points="{area_points}" fill="url(#areaGrad)" />
    
    <!-- Line -->
    <polyline points="{polyline_points}" fill="none" stroke="url(#lineGrad)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" filter="url(#shadow)" />
    
    <!-- Data Points -->
    <circle cx="{points[-1][0]}" cy="{points[-1][1]}" r="6" fill="#00f2fe" filter="url(#shadow)" />
    
    <!-- Labels -->
    <text x="{width-padding_x}" y="{padding_y-10}" font-family="Segoe UI, sans-serif" font-size="14" font-weight="bold" fill="#00f2fe" text-anchor="end">{values[-1]} Total Installs</text>
    <text x="{padding_x}" y="{height-10}" font-family="Segoe UI, sans-serif" font-size="12" fill="#888" text-anchor="start">Growth History (Global)</text>
    <text x="{width-padding_x}" y="{height-10}" font-family="Segoe UI, sans-serif" font-size="10" fill="#555" text-anchor="end">Real-time Tracker</text>
    </svg>'''
    
    with open(SVG_FILE, "w") as f:
        f.write(svg)

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

# Only update if today's count changed or it's a new day
if history and history[-1]['date'] == today:
    history[-1]['count'] = total_count
else:
    history.append({"date": today, "count": total_count})
    history = history[-MAX_POINTS:]

with open(STATS_FILE, "w") as f:
    json.dump(history, f)

generate_svg(history)
