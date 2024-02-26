import os
import sys
import pathlib
import re
import datetime
from bs4 import BeautifulSoup
"""
Hmmm maybe checkout https://pypi.org/project/markdownify/ and beautiful soup
"""


location = pathlib.Path().resolve()
for f in os.listdir('older'):
  print('Details for ' + f)
  bgcolor = ''
  textColor = ''
  date = ''
  title = ''
  links = ''
  body = ''
  dateFormatted = ''
  description = ''
  keywords = ''
  currentParagraph = ''
  partialParagraph = ''
  paragraphClose = ''
  fullParagraph = ''
  paragraphs = []
  try:
    with open (str(location) + '/older/' + f, 'r', encoding="UTF-8") as old:
      soup = BeautifulSoup(old, 'html.parser')
      # Find Title Tag
      print(soup.title)
      for string in soup.strings:
        print(repr(string))

  except UnicodeDecodeError:
    print(f + " is not UTF-8")
