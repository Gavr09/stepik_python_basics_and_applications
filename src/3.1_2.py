# s = 'abababa'
# t = 'aba' # 3
# вывести число пересекающихся вхождений t в s

s = input()
t = input()

num = 0
ind = s.find(t, 0)

while ind != -1:
    num += 1
    ind = s.find(t, ind+1)

print(num)
