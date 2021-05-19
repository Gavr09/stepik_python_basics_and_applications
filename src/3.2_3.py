# вывести строки, содержащие две буквы z, между которыми ровно три символа
'''
Input:
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz

Output:
zabcz
zzxzz
'''

import sys
import re

pattern = r'z(\S){3}z'
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) > 0:
        # print(re.match(pattern, line))
        print(line)
