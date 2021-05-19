'''
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b

scope = {'global':{'parent':None, 'variables':['a']},
         'foo':{'parent':'global', 'variables':['b'],
         'bar':{'parent':'foo', 'variables':['a']}}}
'''

def add(scope, namespace, variable):
    scope[namespace]['variables'] = scope[namespace]['variables'] + [variable]

def create(scope, namespace, parent_namespace):
    scope[namespace] = {}
    scope[namespace]['parent'] = parent_namespace
    scope[namespace]['variables'] = []

def get(scope, namespace, variable):

    if variable in scope[namespace]['variables']:
        return namespace
    else:
        if namespace == 'global':
            return None
        else:
            return get(scope, scope[namespace]['parent'], variable)

scope = {'global':{'parent':None, 'variables':[]}}
command_num = int(input())

for i in range(command_num):
    # print(i)
    # print(scope)
    part1, part2, part3 = input().split()
    if part1 == 'add':
        add(scope, part2, part3)
    elif part1 == 'create':
        create(scope, part2, part3)
    elif part1 == 'get':
        print(get(scope, part2, part3))