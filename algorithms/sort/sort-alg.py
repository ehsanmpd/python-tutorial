import time
import random


# Merge sort script
def merge(leftList,rightList):
    sorted_list = []
    leftPivot = 0
    rightPivot = 0
    # do the while-loop until one fo the lists become empty
    while leftPivot <= len(leftList) - 1 and rightPivot <= len(rightList) - 1:
        if leftList[leftPivot] <= rightList[rightPivot]:
            sorted_list.append(leftList[leftPivot])
            leftPivot += 1
        else:
            sorted_list.append(rightList[rightPivot])
            rightPivot += 1
    # add the remaining of non empty list to the sorted_list
    while leftPivot <= len(leftList) - 1:
        sorted_list.append(leftList[leftPivot])
        leftPivot += 1
    while rightPivot <= len(rightList) - 1:
        sorted_list.append(rightList[rightPivot])
        rightPivot += 1
    return sorted_list


def merge_sort(in_list):
    sorted_list=[]
    if len(in_list) > 1:
        # find the middle index of the list
        mid = int(len(in_list)/2)
        # divide the list into two and run merge_sort recursively for each
        leftList = merge_sort(in_list[:mid])
        rightList = merge_sort(in_list[mid:])
        # merge the two sorted lists
        sorted_list = merge(leftList,rightList)
        return sorted_list
    # the following only occurs when in_list has only one element. A list with single element is sorted
    sorted_list.append(in_list[0])
    return sorted_list


# Quick sort script
def quick_sort(in_list):
    sorted_list=[]
    return sorted_list


random_list = random.sample(population=range(0,1000),k=1000)
sorted_list = random_list.copy()

start = time.time_ns()
sorted_merge=merge_sort(random_list)
end=time.time_ns()
merge_time = (end-start)/1000
print("Elapsed time for merge sort: %d us"%(merge_time))

# python sort() uses Timsort algorithm
start = time.time_ns()
sorted_list.sort(key=None,reverse=False)
end=time.time_ns()
sort_time = (end-start)/1000
print("Elapsed time for python Timsort: %d us"%(sort_time))

print(merge_time/sort_time)
