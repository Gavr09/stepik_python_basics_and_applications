import requests

template_url = 'http://numbersapi.com/{}/math?json=true'

output_str = ''

with open('test_3.5.1/dataset_24476_3.txt', 'r') as f:
    for string in f:
        cur_num = int(string)
        res = requests.get(template_url.format(cur_num))
        if res.json()['found'] == True:
            output_str += 'Interesting\n'
        else:
            output_str += 'Boring\n'

with open('test_3.5.1/output.txt', 'w') as f:
    f.write(output_str)
