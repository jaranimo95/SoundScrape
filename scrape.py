import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv)<2:
	print("Usage: python scrape.py <url>")
	sys.exit(0)
else:
	url = sys.argv[1]

#send http request
res = requests.get(url)
res.raise_for_status()

#passing to BS for parsing
soup = BeautifulSoup(res.text, "html.parser")
print(soup.get_text(strip=True))