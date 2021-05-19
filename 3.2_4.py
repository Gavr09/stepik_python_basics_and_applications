# вывести строки, содержащие \ (обратный слеш)
'''
Input:
\w denotes word character
No slashes here

Output:
\w denotes word character
'''

import sys
import re

pattern = r'\\'
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) > 0:
        print(line)
