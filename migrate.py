import os
import sys
import pathlib
import re
import datetime
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
"""
Hmmm maybe checkout https://pypi.org/project/markdownify/ and beautiful soup
"""

"""
date = date if date else re.search(r"(\d{1,2})/(\d{1,2})/(\d{2,4})", line)
        description = description if description else re.search(r"NAME=\"DESCRIPTION\" CONTENT=\"(.*)\">", line, re.IGNORECASE)
        keywords = keywords if keywords else re.search(r"NAME=\"KEYWORDS\" CONTENT=\"(.*)\">", line, re.IGNORECASE)
        #if date: print(date.group(1) + '/' + date.group(2)  + '/' + date.group(3))
        title = title if title else re.search(r"<TITLE>(.*)</TITLE>", line, re.IGNORECASE)
        #if title: print(title.group(1))
        bgcolor = bgcolor if bgcolor else re.search(r"Bgcolor=[\",\'](#(?:[0-9a-fA-F]{3}){1,2})", line, re.IGNORECASE)
        body = body if body else re.search(r"<body (.*) ", line, re.IGNORECASE)
        links = links if links else re.search(r"links=(.*) ", line, re.IGNORECASE)
        textColor = textColor if textColor else re.search(r"text=[\",\'](#(?:[0-9a-fA-F]{3}){1,2})", line, re.IGNORECASE)
        #if body: print(body.group(1))
        try:
          dateFormatted=datetime.datetime.strptime(
            date.group(1) + '/' + date.group(2)  + '/' + date.group(3), '%m/%d/%y'
            ).strftime('%Y-%m-%d')
        except:
          dateFormatted = ''
    s = '''\
  Body: {body}
  Bgcolor: {bgcolor}
  Title {title}
  Date {date}
  DateFormatted {dateFormatted}
  Keywords {keywords}
  Description {description}
  Paragraphs {paragraphs}
  '''.format(
    body=body.group(1) if body else 'none',
    bgcolor=bgcolor.group(1) if bgcolor else 'None',
    date=date.group(1) + '/' + date.group(2)  + '/' + date.group(3) if date else 'none',
    title=title.group(1) if title else 'untitled',
    dateFormatted=dateFormatted if dateFormatted else 'none',
    keywords=keywords.group(1) if keywords else 'none',
    description=description.group(1) if description else 'none',
    paragraphs=paragraphs)
    print(s)
    """
def md(soup, **options):
    return MarkdownConverter(**options).convert_soup(soup)

location = pathlib.Path().resolve()

for f in os.listdir('older'):
  print('''
  ##### Details for %s
  ''' % f)
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
      print(soup.title.get_text() if soup.title else 'No Title')
      body = soup.find('body')
      try:
        print(body.attrs)
      except AttributeError:
        print('No body attributes')
      date = None
      for string in soup.stripped_strings:
        if date:
          print("WE HAVE A DATE ALREADY: ", date) # 9/9/1969
          if date == '9/9/1969':
            date = None
        date = re.search(r"(\d{1,2})/(\d{1,2})/(\d{2,4})", string)
        try:
          dateFormatted=datetime.datetime.strptime(
            date.group(1) + '/' + date.group(2)  + '/' + date.group(3), '%m/%d/%y'
            ).strftime('%Y-%m-%d')
          date = None
        except:
          '''try looking for a different date format eg Fourteen/January/Ten or 14/January/2010'''
          dateFormatted = None
        if dateFormatted:
          print(dateFormatted)
        else:
          if date:
            print(date.group(1) + '/' + date.group(2)  + '/' + date.group(3))

      mdd = md(soup)
      # print(mdd)
  except UnicodeDecodeError:
    print(f + " is not UTF-8")
