import time
from functools import reduce


list_ones = [1] * 10000

t_start = time.time_ns()
# start of method 1
builtin_sum = sum(list_ones)
# end of method 1
t_end = time.time_ns()
time_elapsed = t_end-t_start
print('Built-in method -> result of sum: %d,  Elapsed time: %d ns'%(builtin_sum,time_elapsed))

t_start = time.time_ns()
# start of method 2
iter_sum=0
for i in list_ones:
    iter_sum += i
# end of method 2
t_end = time.time_ns()
time_elapsed = t_end-t_start
print('For-loop method -> result of sum: %d,  Elapsed time: %d ns'%(iter_sum,time_elapsed))

t_start = time.time_ns()
# start of method 3
reduce_sum = reduce(lambda x,y: x+y,list_ones)
# end of method 3
t_end = time.time_ns()
time_elapsed = t_end-t_start
print('Reduce method -> result of sum: %d,  Elapsed time: %d ns'%(reduce_sum,time_elapsed))