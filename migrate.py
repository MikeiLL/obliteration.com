import os
import sys
import pathlib
import re


location = pathlib.Path().resolve()
for f in os.listdir('older'):
  try:
    with open (str(location) + '/older/' + f, 'r', encoding="UTF-8") as old:
      for line in old:
        m = re.search(r"(\d{1,2})/(\d{1,2})/(\d{2,4})", line)
        if m: print(m.group(1) + '/' + m.group(2)  + '/' + m.group(3))
  except UnicodeDecodeError:
    print(f + " is not UTF-8")
