# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 20:26:13 2018

@author: Administrator
"""
#HTML parser with Beautiful Soup

#Use HTML and scrap data, then sum up


from urllib import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(str(url), context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
soup = BeautifulSoup(html, "html.parser")
print soup
# Retrieve all of the anchor tags
tags = soup('span')
sums = []
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('span', None))
    print('Contents:', tag.contents)
    print('Attrs:', tag.attrs)
    for i in tag.contents:
        sums.append(int(i))

print sums

Total = sum(sums)
print(Total)
'''Scraping from:
   http://py4e-data.dr-chuck.net/comments_9854.html'''