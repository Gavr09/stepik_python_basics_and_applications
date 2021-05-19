'''
Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
<имя класса> : <количество потомков>

Sample Input:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:
A : 3
B : 1
C : 2

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents": ["B", "C"]}, {"name": "V", "parents": ["D"]}]
A : 5
B : 3
C : 3
D : 2
V : 1

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["B"]}]
A : 3
B : 2
C : 1
'''

import json

def list_with_unique_elems(list1):
    list2 = []
    for elem in list1:
        if elem not in list2:
            list2.append(elem)
    return list2

def calc_parents(parents_num_dict, parents_dict, name):
    parents = parents_dict[name]
    if name not in parents_num_dict.keys():
        parents_num_dict[name] = []

    if len(parents) > 0:
        for parent_name in parents:
            if parent_name not in parents_num_dict.keys():
                parents_num_dict[parent_name] = [name]
                parents_num_dict[parent_name] = parents_num_dict[parent_name] + parents_num_dict[name]
            else:
                parents_num_dict[parent_name] = parents_num_dict[parent_name] + [name]
                parents_num_dict[parent_name] = parents_num_dict[parent_name] + parents_num_dict[name]

            calc_parents(parents_num_dict, parents_dict, parent_name)


data_json = input()
data_python = json.loads(data_json)
parents_num_dict = {}
parents_dict = {}

for elem in data_python:
    parents_dict[elem['name']] = elem['parents']

for name in parents_dict.keys():
    calc_parents(parents_num_dict, parents_dict, name)

output_list = []
# print(parents_num_dict)
for parent_name in parents_num_dict.keys():
    parents_num_dict[parent_name] = list_with_unique_elems(parents_num_dict[parent_name])
    output_list.append('{} : {}'.format(parent_name, len(parents_num_dict[parent_name])+1))
# print(parents_num_dict)
output_list.sort()
for elem in output_list:
    print(elem)






