# Performance analysis of list functions

## Sum of elements
Consider the following ```list```:
```python
list_ones = [1]*10000
```
We study the following methods of implementation to sum the elements in the list:

1. Using built-in python ```sum()``` function:
   ```python
   list_sum= sum(list_ones)
   ```
2. Using for-loop and iterate among the numbers in the list:
    ```python
   iter_sum=0
    for i in list_ones:
        iter_sum += i
    ```
3. Using ```reduce()``` function from ```functools``` and inline ```lambda``` function:
```python
reduce_sum = reduce(lambda x,y: x+y,list_ones)
```
The file [list-add-performance.py](list-add-performance.py) implements the two ways. The performace measurement shows 
that the first method is faster than the other ones:
```
Built-in method -> result of sum: 10000,  Elapsed time: 89000 ns
For-loop method -> result of sum: 10000,  Elapsed time: 829000 ns
Reduce method -> result of sum: 10000,  Elapsed time: 821000 ns
```