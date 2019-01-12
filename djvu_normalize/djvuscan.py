#!/usr/bin/env python3

import subprocess
import sys
import re

# first we obtain output from the djvudump bash command, convert byte to string (decode), and split the output string in multiple sections 
result = subprocess.check_output(['djvudump',sys.argv[1]]).decode("utf-8").split('FORM')

nums = {}
for i in range(len(result)):
    page = re.search(r'\[P\w+\]',result[i])
    size = re.search(r'\b\w+x\w+\b',result[i])
    if page is not None:
        if str(size.group(0)) in nums:
            nums[str(size.group(0))]+=1
        else:
            nums[str(size.group(0))] = 0
        print(page.group(0),size.group(0))
print(nums)
