class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.count = 0
        self.capacity = capacity

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.count <= (self.capacity-v):
            return True
        else:
            return False

    def add(self, v):
        # положить v монет в копилку
        self.count += v

def test_MoneyBox():
    x = MoneyBox(20)
    print(x.count)
    print(x.can_add(10))
    x.add(10)
    print(x.count)
    print(x.can_add(15))

# test_MoneyBox()

class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.count = 0 # текущее значение обработанных элементов
        self.values = []

    def add(self, *a):
        # добавить следующую часть последовательности
        b = self.values + list(a)
        l = len(b)
        i = 0
        while l >=5:
            self.values = b[i*5:i*5+5]
            print(sum(self.values))
            self.values = []
            i += 1
            l -= 5
        if l != 0:
            self.values = b[-l:]

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
        # print(self.values)
        return self.values

def test_Buffer():
    buf = Buffer()
    buf.add(1, 2, 3)
    buf.get_current_part()  # вернуть [1, 2, 3]
    buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
    buf.get_current_part()  # вернуть [6]
    buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
    buf.get_current_part()  # вернуть []
    buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
    buf.get_current_part()  # вернуть [1]

test_Buffer()