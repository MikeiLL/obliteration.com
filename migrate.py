import os
import sys
import pathlib
import re
import datetime


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
  try:
    with open (str(location) + '/older/' + f, 'r', encoding="UTF-8") as old:
      for line in old:
        date = date if date else re.search(r"(\d{1,2})/(\d{1,2})/(\d{2,4})", line)
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
  '''.format(
    body=body.group(1) if body else 'none',
    bgcolor=bgcolor.group(1) if bgcolor else 'None',
    date=date.group(1) + '/' + date.group(2)  + '/' + date.group(3) if date else 'none',
    title=title.group(1) if title else 'untitled',
    dateFormatted=dateFormatted if dateFormatted else 'none')
    print(s)
  except UnicodeDecodeError:
    print(f + " is not UTF-8")
