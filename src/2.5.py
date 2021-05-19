from functools import partial

def mod_checker(x, mod=0):
    return lambda y: y%x==mod
    # if mod == 0:
    #     return lambda mod: x%mod == 0
    # else:
    #     return lambda *args: x%mod==0

mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True