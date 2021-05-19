import re
import requests

A = input().strip()
B = input().strip()

# A = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
# B = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
#
# A = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
# B = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
#
# A = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
# B = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
res = requests.get(A)
text_A = res.text
# print(text_A)

url_list = []
pattern_from_A_to_C = r'<a'
small_pattern = r'href="([\w\.:/\\ ]+)"'
pattern_from_C_to_B = r'href="{}"'.format(B)

# print(text_A.split(sep='\n'))
for line in text_A.split(sep='\n'):
    # print(line)
    match = re.match(pattern_from_A_to_C, line)
    # print(match)

    if match != None:
        res = re.search(small_pattern, line)
        if res != None:
            # print(r'\1')
            url_list.append(line[res.span()[0]+6:res.span()[1]-1])

ans = 'No'
for url in url_list:
    try:
        text_C = requests.get(url).text
        if pattern_from_C_to_B in text_C:
            ans = 'Yes'
    except:
        pass

print(ans)


