import requests
import json
import time

my_dict = {}

client_id = '834a280698b8492c12ce'
client_secret = '645db9559310d24002c2d85cd42c9c47'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

template_url = "https://api.artsy.net/api/artists/{}"

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

with open('test_3.5.2/dataset_24476_4.txt', 'r') as f:
    for sortable_name in f:
        res = requests.get(template_url.format(sortable_name.strip()), headers=headers)
        j = res.json()
        my_dict[j['sortable_name']] = j['birthday']
        time.sleep(1)

res_list = sorted(my_dict.items(), key=lambda x: (x[1], x[0])) # На выходе имеем list из кортежей

output_str = ''
for elem in res_list:
    output_str += elem[0] + '\n'

with open('test_3.5.2/output.txt', 'w', encoding='utf-8') as f:
    f.write(output_str)
