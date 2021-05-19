# s = 'abab'
# a = 'ab'
# b = 'ba'
# операция: замена всех вхождений строки a в строку s на строку b
# s: abab -> baba -> bbaa
# после какого минимального количества операций в s не останется вхождений a
# вывести число операций либо Impossible, если их больше 1000

s = input()
a = input()
b = input()

num = 0

while True:
    if a not in s:
        print(num)
        break

    if num == 1000:
        print('Impossible')
        break

    s = s.replace(a, b)
    print(s)
    num += 1