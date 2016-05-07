# -*- coding: utf-8 -*-
from time import *

t0 = time()
count = 10**5

nums = []

for i in range(count):
    nums.append(i)   # append() 常数时间

nums.reverse()

t1 = time() - t0

t0 = time()
nums = []
for i in range(count):
    nums.insert(0, i)
t2 = time()-t0

print("t1: {}\nt2: {}".format(t1, t2))
