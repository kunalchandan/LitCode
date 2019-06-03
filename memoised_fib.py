import numpy as np


def fib_reg(x: int) -> int:
    if x == 0 or x == 1:
        return 1
    else:
        return fib_reg(x - 1) + fib_reg(x - 2)


fib_val = 10
mem = np.zeros(fib_val, int)


def fib_mem(x: int) -> int:
    if not mem[x-1] == 0:
        return mem[x-1]
    elif x == 0 or x == 1:
        mem[x] = 1
        return mem[x-1]
    else:
        mem[x-1] = fib_mem(x-1) + fib_mem(x-2)
        return mem[x-1]


print(fib_mem(fib_val))
print(fib_reg(fib_val-2))
