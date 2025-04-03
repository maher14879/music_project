import requests
import json
from bs4 import BeautifulSoup

def get_links(url, depth = 1, max_fail = 1, fails = 0):
    try: payload = requests.get(url=url, headers={})
    except Exception as e: 
        print(f"Unable to get {url}. Error: {e}")
        return []
    
    html = payload.text
    soup = BeautifulSoup(html, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]

    midi_links = [(link if link.startswith("http") else url + "/" + link) for link in links if link.endswith(".mid")]
    if not midi_links: fails += 1

    if depth > 0 and fails <= max_fail:
        for link in links:
            if not link.startswith("http"): link = url + "/" + link
            midi_links += get_links(link, depth - 1, max_fail, fails)
    
    return midi_links

url = "http://www.jsbach.net/midi"

with open("data/midi_files/bach.json", "w") as file:
    json.dump({"midi": get_links(url, 1, 3)}, file, indent=4)