import time


def sum_list_iterative(items):
    sum=0
    for i in items:
        sum += i
    return sum


def sum_list_builtin(items):
    return sum(items)


list_ones = [1] * 10000

t_start = time.time_ns()
builtin_sum = sum_list_builtin(list_ones)
t_end = time.time_ns()
time_elapsed = t_end-t_start
print('Result of sum: %d' %builtin_sum)
print('Elapsed time using built-in function: %d ns'%(time_elapsed))

t_start = time.time_ns()
iter_sum =sum_list_iterative(list_ones)
t_end = time.time_ns()
time_elapsed = t_end-t_start
print('Result of sum: %d' %iter_sum)
print('Elapsed time using for-loop: %d ns'%(time_elapsed))