# в каждой строке заменить все вхождения подстроки human на подстроку computer и вывести полученные строки
'''
Input:
I need to understand the human mind
humanity

Output:
I need to understand the computer mind
computerity
'''

import sys
import re

pattern = r'human'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, 'computer', line))
