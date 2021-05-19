import re
import requests

test_url_1 = ''
test_url_2 = 'http://pastebin.com/raw/hfMThaGb'
test_url_3 = 'http://pastebin.com/raw/7543p0ns'

res = requests.get(test_url_2)
content = res.text
# with open('test_3.3.2/example.txt', 'r') as f:
#     for line in f:
#         content+=line

prot_pattern = r'''((http://)|(https://)|(ftp://)|())'''
end_pattern = r'''((\.org)|(\.ru)|(\.com)|(\.ua)|(\.ge))'''
# body_pattern = r''''''

url_list = []

# content = '<li><a href="http://adworker.ru/">Adworker.ru</a></li>'
# content = '</script><a target="_top" href="http://banner.rbc.ru/banredir.cgi?lid=firstpage_bot" empty="true"'
# content = '''<b>20:28&nbsp;30/03/2009</b>\n\n<a href="http://data.rbc.ru/cgi-bin/mk_custom_table.cgi">Ваши&nbsp;настройки</a><br>'''
# content = ''';\n<a href="http://www.rbcinfosystems.com/">Инвесторам</a>&nbsp; &middot; &nbsp;'''
# content = '''ou are currently not logged in, this means you can not edit or delete anything you paste.
# Sign Up or Login<a href="http://steeeeeeepic.org/courses"\n
# ou are currently not logged in, this means you can not edit or delete anything you paste. Sign Up or Login'''

content = r'''k href='http://neerc.ifmo-2.ru:1345'\n\n<a title=test download="http://test.com"; href="test.com" class="my test" style='''

# for line in re.split(r'''[>\n]''', content):
#     try:
#         # print(line)
#         # big_pattern = r'<a([\w.:/\s"\'=]+?)href=["\']((http://)|(https://)|(ftp://)|())([\w\.:/\-]+?)((\.org)|(\.ru)|(\.com))'
#         big_pattern = r'''([\w\.:;/\s"\'=]+?)<a([\w\.:/\s"\'=]+?)href=[\'"]{}([\w\.:/\-]+?){}'''.format(prot_pattern, end_pattern)
#         match = re.match(big_pattern, line)
#         cut_string = match.group()
#
#         small_pattern = r'''([\w\.:/\s"\'=]+?)<a([\w\.:/\s"\'=]+?)href=[\'"]{}'''.format(prot_pattern)
#
#         match = re.match(small_pattern, line)
#         url = cut_string[match.span()[1]:]
#
#         if url not in url_list:
#             url_list.append(url)
#     except BaseException:
#         pass

try:
    # print(line)
    # big_pattern = r'<a([\w.:/\s"\'=]+?)href=["\']((http://)|(https://)|(ftp://)|())([\w\.:/\-]+?)((\.org)|(\.ru)|(\.com))'
    big_pattern = r'''([\w\.:;/\s"\'=\\n]+?)?(<a([\w\.:;/\s"\'=]+?)href=[\'"]{}([\w\.:/\-]+?){})'''.format(prot_pattern, end_pattern)
    matches_list = re.findall(big_pattern, content)

    for i in range(len(matches_list[0])):
        cut_string = matches_list[0][i]

        small_pattern = r'''([\w\.:;/\s"\'=\\n]+?)<a([\w\.:;/\s"\'=]+?)href=[\'"]{}'''.format(prot_pattern)

        try:
            match = re.match(small_pattern, cut_string)
            url = cut_string[match.span()[1]:]

            if url not in url_list:
                url_list.append(url)
        except BaseException:
            pass
except BaseException:
    pass

url_list.sort()

for url in url_list:
    print(url)
