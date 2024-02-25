import os
import sys
import pathlib
import re


location = pathlib.Path().resolve()
for f in os.listdir('older'):
  print('Details for ' + f)
  try:
    with open (str(location) + '/older/' + f, 'r', encoding="UTF-8") as old:
      for line in old:
        date = re.search(r"(\d{1,2})/(\d{1,2})/(\d{2,4})", line)
        if date: print(date.group(1) + '/' + date.group(2)  + '/' + date.group(3))
        title = re.search(r"<TITLE>(.*)</TITLE>", line)
        if title: print(title.group(1))
  except UnicodeDecodeError:
    print(f + " is not UTF-8")
