import urllib.request
import json
import os
from datetime import datetime

# --- CONFIGURATION ---
MS_MARKETPLACE_ID = "likhith-adithya.ai-cli-pro"
OPEN_VSX_ID = "likhith-adithya/ai-cli-pro" # Corrected namespace
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
        print(f"Error fetching Open VSX stats: {e}")
        return 0

def generate_svg(history):
    if not history: return
    
    values = [point['count'] for point in history]
    if not values: return
    
    min_val, max_val = min(values), max(values)
    range_val = max(max_val - min_val, 1)
    
    width, height = 400, 100
    padding = 20
    
    points = []
    if len(values) == 1:
        points.append(f"{padding},{height/2}")
        points.append(f"{width-padding},{height/2}")
    else:
        for i, val in enumerate(values):
            x = padding + (i * (width - 2 * padding) / (len(values) - 1))
            y = (height - padding) - ((val - min_val) / range_val * (height - 2 * padding))
            points.append(f"{x},{y}")
    
    polyline_points = " ".join(points)
    
    svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="transparent"/>
    <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1" />
        </linearGradient>
    </defs>
    <polyline points="{polyline_points}" fill="none" stroke="url(#grad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="{points[-1].split(',')[0]}" cy="{points[-1].split(',')[1]}" r="4" fill="#00f2fe" />
    <text x="{width-padding}" y="{height-2}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="12" font-weight="bold" fill="#4facfe" text-anchor="end">{values[-1]} total installs</text>
    <text x="{padding}" y="{height-2}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="10" fill="#888" text-anchor="start">Global Adoption Trend</text>
    </svg>'''
    
    with open(SVG_FILE, "w") as f:
        f.write(svg)

# Main Execution
ms_count = get_ms_marketplace_downloads()
ovsx_count = get_open_vsx_downloads()
total_count = ms_count + ovsx_count

print(f"MS Marketplace: {ms_count}")
print(f"Open VSX: {ovsx_count}")
print(f"Total: {total_count}")

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
