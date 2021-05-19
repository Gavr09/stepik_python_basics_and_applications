import itertools

def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev+cur

def primes():
    a = 2
    while True:
        pr_prime_number = True
        for b in range(a):
            if b > 1 and a%b == 0:
                pr_prime_number = False
        if pr_prime_number == True:
            yield a
            a += 1
        else:
            a += 1


# for i in fibonacci():
#     print(i)
#     if i > 100:
#         break
#
# for i in primes():
#     print(i)
#     if i > 50:
#         break
# gen = primes()
# print(next(gen))
# print(next(gen))
# print(next(gen))
print(list(itertools.takewhile(lambda x: x <= 31, primes())))