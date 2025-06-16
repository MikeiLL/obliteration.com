import requests, sys
import bs4
"""
Get some content from https://colorguide.org
print out to Markdown file
"""

if len(sys.argv) > 1:
  url = sys.argv[1]
else:
  print('Provide a URL from Color Guide.org eg: https://colorguide.org/en/muted-colors')
  sys.exit(1)
response = requests.get(url)
soup = bs4.BeautifulSoup(response.content, 'html.parser')
colors = soup.find_all('div', class_='cP')
print(f'Found {len(colors)} colors')
markdown_content = f'## {soup.find("h1").text}\n\n'
for color in colors:
    style = color.get('style')
    markdown_content += f"<div style='display: flex; align-items: center; {style} markdown=1'>\n"
    markdown_content += f"## {style.split(":")[0]} <br> {style.split(":")[1]}\n"
    markdown_content += "</div>\n\n"

with open('color_org_colors.md', 'w') as file:
    file.write(markdown_content)
print(f"Markdown file 'color_org_colors.md' created successfully.")
