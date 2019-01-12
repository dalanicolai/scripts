#!/usr/bin/env python3
"""
Usage: djvu_page_extract.py

djvu_page_extract.py filename pagesize(wxh, use list_page_sizes.py)
"""
import subprocess
import sys
import re

result = subprocess.check_output(['djvudump',sys.argv[1]]).decode("utf-8").split('FORM')

page_select = []
for i in range(len(result)):
    page = re.search(r'\[P\w+\]',result[i])
    size = re.search(r'\b\w+x\w+\b',result[i])
    if page is not None and str(size.group(0)) != sys.argv[2]:
        page_select.append(str(page.group(0))[2:-1])
print(page_select)

# write pages to file
f = open('pages.txt', 'w')
f.writelines([num + '\n' for num in page_select])
f.close()

pages = ",".join(page_select)
subprocess.run(['ddjvu','-format=pbm','-page='+pages,'-eachpage','-size='+sys.argv[2],sys.argv[1],'out%d.pbm'])

# convert .pbm files to .djvu
for i in page_select:
    subprocess.run(['cjb2','out'+i+'.pbm','out'+i+'.djvu'])

for i in page_select[::-1]:
    subprocess.run(['djvm','-d',sys.argv[1],i])

for i in page_select:
    subprocess.run(['djvm','-i',sys.argv[1],'out'+i+'.djvu',i])


