#timeit>>>identify the excution  in 1000000 time

import timeit

#print(dir(timeit))

#print(timeit.timeit("'elzero' * 1000"))



import random

#print(random.randint(0, 50))
print(timeit.timeit(stmt="random.randint(0, 50)",setup="import random"))
