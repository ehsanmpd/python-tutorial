# Performance analysis of list functions

## Sum of elements
Consider the following ```list```:
```python
list_ones = [1]*10000
```
We study two methods of implementation to sum the elements in the list:

1. Using built-in python ```sum()``` function:
   ```python
   list_sum= sum(list_ones)
   ```
2. Using for-loop and iterate among the numbers in the list:
    ```python
   sum=0
    for i in list_ones:
        sum += i
    ```

The file [list-add-performance.py](list-add-performance.py) implements the two ways. The performace measurement shows 
that the first method is faster than the second one:
```
Built-in method -> result of sum: 10000,  Elapsed time: 82000 ns
For-loop method -> result of sum: 10000,  Elapsed time: 705000 ns
```