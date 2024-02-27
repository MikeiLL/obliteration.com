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

most_recent_date = ''

day_strings = {
  'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10',
  'eleven': '11', 'twelve': '12', 'thirteen': '13', 'fourteen': '14', 'fifteen': '15', 'sixteen': '16', 'seventeen': '17', 'eighteen': '18', 'nineteen': '19', 'twenty': '20',
  'twentyone': '21', 'twentytwo': '22', 'twentythree': '23', 'twentyfour': '24', 'twentyfive': '25', 'twentysix': '26', 'twentyseven': '27', 'twentyeight': '28', 'twentynine': '29', 'thirty': '30',
  'thirtyone': '31'
}

month_names = {
  'january': '01', 'february': '02', 'march': '03', 'april': '04', 'may': '05', 'june': '06', 'july': '07', 'august': '08', 'september': '09', 'sept': '09', 'october': '10', 'november': '11', 'december': '12'
}
list_of_files = os.listdir('older')
sorted_files = sorted(list_of_files, key=lambda x: int(x.split('mikeb')[1].split('.')[0]))

for f in sorted_files:
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
        """ if date:
          print("WE HAVE A DATE ALREADY: ", date) # 9/9/1969
          if date == '9/9/1969':
            print("WE HAVE A DATE ALREADY: ", date) """
        date = re.search(r"^(\d{1,2})/(\d{1,2})/(\d{2,4})$", string)
        word_date = re.search(r"^([a-z,A-Z]+)/([a-z,A-Z]+)/([a-z,A-Z]+)$", string)
        if date:
          print("Date: ", date.group(1) + '/' + date.group(2)  + '/' + date.group(3))
          try:
            dateFormatted=datetime.datetime.strptime(
              date.group(1) + '/' + date.group(2)  + '/' + date.group(3), '%m/%d/%y'
              ).strftime('%Y-%m-%d')
          except AttributeError:
            '''try looking for a different date format eg Fourteen/January/Ten or 14/January/2010'''
        if word_date:
          print("Word Date: ", word_date.group(1) + '/' + word_date.group(2)  + '/' + word_date.group(3))
          date = [day_strings[word_date.group(1).lower()], str("{:02d}".format(int(month_names[word_date.group(2).lower()]))), day_strings[word_date.group(3).lower()]]
          try:
            dateFormatted=datetime.datetime.strptime(
              str("{:02d}".format(int(month_names[word_date.group(2).lower()]))) + '/' + day_strings[word_date.group(1).lower()] + '/' + "{:02d}".format(int(day_strings[word_date.group(3).lower()])), '%m/%d/%y'
              ).strftime('%Y-%m-%d')
          except AttributeError:
            pass
          if dateFormatted:
            print('dateFormatted: ', dateFormatted)
          most_recent_date = dateFormatted
        else:
          if not dateFormatted and most_recent_date:
            # if no date, let's increment the most recent date
            print('most_recent_date: ', most_recent_date)
            date_parts = most_recent_date.split('-')
            print('date_parts: ', date_parts)
            date = datetime.datetime(int(date_parts[0]), int(date_parts[1]), int(date_parts[2])) + datetime.timedelta(days=1)
            dateFormatted = date.strftime('%Y-%m-%d')
            print('incremented dateFormatted: ', dateFormatted)
            most_recent_date = dateFormatted
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
