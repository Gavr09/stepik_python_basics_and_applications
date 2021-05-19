'''
Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x
и возвращающую самое маленькое целое число y, такое что:

    y больше или равно x
    y делится нацело на 5
'''

def closest_mod_5(x):
    for y in range(x, x+5):
        if y % 5 == 0:
            return y
    return "I don't know :("

def run1():
    print(closest_mod_5(39))

def calc_c_n_k(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return calc_c_n_k(n-1, k) + calc_c_n_k(n-1, k-1)

def run2():
    n, k = map(int, input().split())
    print(calc_c_n_k(n, k))

# run1()
run2()