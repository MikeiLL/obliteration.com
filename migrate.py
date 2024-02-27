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

day_strings = {
  '01': 'One',
  '02': 'Two',
  '03': 'Three',
  '04': 'Four',
  '05': 'Five',
  '06': 'Six',
  '07': 'Seven',
  '08': 'Eight',
  '09': 'Nine',
  '10': 'Ten',
  '11': 'Eleven',
  '12': 'Twelve',
  '13': 'Thirteen',
  '14': 'Fourteen',
  '15': 'Fifteen',
  '16': 'Sixteen',
  '17': 'Seventeen',
  '18': 'Eighteen',
  '19': 'Nineteen',
  '20': 'Twenty',
  '21': 'Twenty-One',
  '22': 'Twenty-Two',
  '23': 'Twenty-Three',
  '24': 'Twenty-Four',
  '25': 'Twenty-Five',
  '26': 'Twenty-Six',
  '27': 'Twenty-Seven',
  '28': 'Twenty-Eight',
  '29': 'Twenty-Nine',
  '30': 'Thirty',
  '31': 'Thirty-One'
}

for f in os.listdir('older'):
  """ print('''
  ##### Details for %s
  ''' % f) """
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
      description = soup.find('meta', attrs={'name': 'description'})
      try:
        print('Description ', description)
      except AttributeError:
        print('No description')
      keywords = soup.find('meta', attrs={'name': 'keywords'})
      try:
        print('Keywords ', keywords)
      except AttributeError:
        print('No keywords')
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
      if not date:
        print('''
  ##### No date for %s
  ''' % f)
      mdd = md(soup)
      # print(mdd)
      template = '''\
---
title: {title}
date: {date}
author: 'Mike iLL'
layout: post
permalink: /{dateFormatted}/{title}
categories:
    - 'Diaper Entries'
og_description: {description}
og_keywords: {keywords}
---
<style>
body {{
  background-color: {bgcolor};
  color: {textColor};
}}
a {{
  color: {links};
}}
a:active {{
  color: {alinks};
}}
a:visited {{
  color: {vlinks};
}}
</style>
{mdd}
'''
      try:
        False and print(template.format(
          title=soup.title.get_text() if soup.title else 'Untitled',
          date=dateFormatted if dateFormatted else 'none',
          dateFormatted=dateFormatted if dateFormatted else 'none',
          description=description['content'] if description else 'none',
          keywords=keywords['content'] if keywords else 'none',
          mdd=mdd,
          bgcolor=body.attrs['bgcolor'] if body.attrs.get('bgcolor') else 'white',
          textColor=body.attrs['text'] if body.attrs.get('text') else 'black',
          links=body.attrs['links'] if body.attrs.get('links') else 'blue',
          vlinks=body.attrs['vlink'] if body.attrs.get('vlink') else 'purple',
          alinks=body.attrs['alink'] if body.attrs.get('alink') else 'red'
        ))
      except AttributeError:
        print('No body attributes')
  except UnicodeDecodeError:
    print(f + " is not UTF-8")
