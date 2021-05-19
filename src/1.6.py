'''
Sample Input:

4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A

Sample Output:

Yes
Yes
Yes
No

parents_names_dict = {'A':[],
                      'B':['A'],
                      'C':['A'],
                      'D':['B', 'C']}
'''

def add_one_class(parents_names_dict, class_name):
    parents_names_dict[class_name] = []

def add_parents(parents_names_dict, son_name, parents_names):
    parents_names_dict[son_name] = parents_names

def is_parent(parents_names_dict, class1_name, class2_name):
    if class1_name == class2_name:
        return True
    else:
        if class1_name in parents_names_dict[class2_name]:
            return True
        else:
            for parent_name in parents_names_dict[class2_name]:
                if is_parent(parents_names_dict, class1_name, parent_name) == True:
                    return True
    return False

parents_names_dict = {}

descriptions_num = int(input())

for i in range(descriptions_num):
    str = input()
    if ':' not in str:
        class_name = str.split()[0]
        add_one_class(parents_names_dict, class_name)
    else:
        idx = str.index(':')
        son_name = str[:idx].split()[0]
        parents_names = str[idx+1:].split()
        add_parents(parents_names_dict, son_name, parents_names)

requests_num = int(input())

for i in range(requests_num):
    class1_name, class2_name = input().split()
    if is_parent(parents_names_dict, class1_name, class2_name) == True:
        print('Yes')
    else:
        print('No')
