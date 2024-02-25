import os
import sys
import pathlib


location = pathlib.Path().resolve()
for f in os.listdir('older'):
  with open (str(location) + '/older/' + f, 'r') as old:
    for line in old:
      print(line)
