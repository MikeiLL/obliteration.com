import os
import sys
import pathlib
import re
import datetime

date = datetime.datetime.now()
dateFormatted = date.strftime('%Y-%m-%d')
title = sys.argv[1] or 'x-x-x-x-x-x-x-x'

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
        with open('_posts/' + dateFormatted + '-x.md', 'w') as new:
          new.write(template.format(
            title=soup.title.get_text().strip() if soup.title else 'x-x-x-x-x-x-x-x',
            date=dateFormatted if dateFormatted else 'No Date',
            dateFormatted=dateFormatted.replace('-','/') if dateFormatted else 'No Date',
            description=description['content'] if description else 'No Description',
            keywords=keywords['content'] if keywords else 'No Keywords',
            bgcolor=bgcolor,
            textColor=textColor,
            links=links,
            alinks=links,
            vlinks=links,
            mdd=mdd
          ))
      except AttributeError:
        print('No body attributes for ' + f)
  except UnicodeDecodeError:
    print(f + " is not UTF-8")
