'''
Sample Input:

4
class1
class2
class3 : class1
class4 : class3 class2
4
class2
class3
class1
class4

Sample Output:

class4

parents_names_dict = {'class1':[],
                      'class2':[],
                      'class3':['class1'],
                      'class4':['class3', 'class2']}

----------------------------------
Sample Input:

4
BaseException
Exception : BaseException
LookupError : Exception
KeyError : LookupError
2
BaseException
KeyError

Sample Output:

KeyError

parents_names_dict = {'BaseException':[],
                      'Exception':['BaseException'],
                      'LookupError':['Exception'],
                      'KeyError':['LookupError']}
'''

def add_one_class(classes_info_dict, class_name):
    classes_info_dict[class_name] = {}
    classes_info_dict[class_name]['parents'] = []
    classes_info_dict[class_name]['class_was_checked'] = False

def add_class_with_parents(classes_info_dict, class_name, parent_classes_names):
    classes_info_dict[class_name] = {}
    classes_info_dict[class_name]['parents'] = parent_classes_names
    classes_info_dict[class_name]['class_was_checked'] = False

def check_may_be_deleted(classes_info_dict, class_name):
    if len(classes_info_dict[class_name]['parents']) == 0 and classes_info_dict[class_name]['class_was_checked'] == False:
        return False
    else:
        if classes_info_dict[class_name]['class_was_checked'] == True:
            return True
        else:
            for parent_name in classes_info_dict[class_name]['parents']:
                if check_may_be_deleted(classes_info_dict, parent_name) == True:
                    return True

classes_info_dict = {}

classes_num = int(input())

for i in range(classes_num):
    str = input()
    if ':' not in str:
        class_name = str.split()[0]
        add_one_class(classes_info_dict, class_name)
    else:
        idx = str.index(':')
        class_name = str[:idx].split()[0]
        parent_classes_names = str[idx+1:].split()
        add_class_with_parents(classes_info_dict, class_name, parent_classes_names)

checks_num = int(input())

for i in range(checks_num):
    class_name = input().split()[0]
    if check_may_be_deleted(classes_info_dict, class_name) == True:
        print(class_name)
    else:
        classes_info_dict[class_name]['class_was_checked'] = True
