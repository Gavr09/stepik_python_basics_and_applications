class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина функций pos >= neg
        if pos>=neg:
            return True
        else:
            return False

    def judge_any(pos, neg):
        # допускат элемент, если его допускает хотя бы одна функция pos >= 1
        if pos >= 1:
            return True
        else:
            return False

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции neg == 0
        if neg == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge


    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for elem in self.iterable:
            pos = 0
            neg = 0
            for f in self.funcs:
                if f(elem) == True:
                    pos+=1
                else:
                    neg+=1
            if self.judge(pos, neg) == True:
                yield elem


def mul2(x):
    return x%2==0

def mul3(x):
    return x%3==0

def mul5(x):
    return x%5==0

a = [i for i in range(31)]

print(list(multifilter(a, mul2, mul3, mul5)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))