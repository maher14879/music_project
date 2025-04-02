import requests
from bs4 import BeautifulSoup

file_name = ""
url = f"http://www.jsbach.net/midi/{file_name}"
headers = {
}

url = "http://www.jsbach.net"

payload = requests.get(url=url, headers=headers)

html = payload.text
soup = BeautifulSoup(html, 'html.parser')
links = [a['href'] for a in soup.find_all('a', href=True)]
print(links)

