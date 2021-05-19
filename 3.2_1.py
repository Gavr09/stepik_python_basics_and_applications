# вывести строки, содержащие cat в качестве подстроки хотя бы два раза
'''
Input:
catcat
cat and cat
catac
cat
ccaatt
cat.cat

Output:
catcat
cat and cat
cat.cat
'''
import sys
import re

double_cat_list = []

pattern = r'cat'
for line in sys.stdin:
    if line == '!':
        break
    line = line.rstrip()
    if len(re.findall(pattern, line)) >= 2:
        print(line)
        double_cat_list.append(line)

# print(double_cat_list)
