import time


list_ones = [1] * 10000

t_start = time.time_ns()
# start of the code
builtin_sum = sum(list_ones)
# end of the code
t_end = time.time_ns()
time_elapsed = t_end-t_start
print('Built-in method -> result of sum: %d,  Elapsed time: %d ns'%(builtin_sum,time_elapsed))

t_start = time.time_ns()
# start of the code
iter_sum=0
for i in list_ones:
    iter_sum += i
# end of the code
t_end = time.time_ns()
time_elapsed = t_end-t_start
print('For-loop method -> result of sum: %d,  Elapsed time: %d ns'%(iter_sum,time_elapsed))