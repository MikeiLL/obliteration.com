"""
Open a set of HTML tables with rows mapping
a color name in a cell to one or more cells with
hex colors in them.
"""
import bs4
import json
import sys
from pprint import pprint
from collections import defaultdict

d = defaultdict(list)

with open ("wernercolortable", "r") as f:
	tables = f.read()
	soup = bs4.BeautifulSoup(tables, "lxml")
	rows = soup.findAll("tr")
	for row in rows:
		try:
			name = row.find('td').get_text()
		except AttributeError:
			continue
		for color in [c.get_text() for c in row.findAll("code")]:
			d[color].append(name)
		#print([c.get_text() for c in row.findAll("code")])

print("printing json file for")
pprint(sorted(d.items()))
print("...")
with open ("color_names_by_hex.json", "wb") as f:
	print(json.dumps(d), file=f)
