# вывести строки, содержащие cat в качестве слова
'''
Input:
cat
catapult and cat
catcat
concat
Cat
'cat'
!cat?

Output:
cat
catapult and cat
'cat'
!cat?

\b - граница слова
\B
'''

import sys
import re

pattern = r'\bcat\b'
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) > 0:
        print(line)
