class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError


lst = PositiveList([])
lst.append(-1)
lst.append(0)
lst.append(2)
print(lst)

