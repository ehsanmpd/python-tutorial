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
    if len(in_list) > 1:
        # find the middle index of the list
        mid = int(len(in_list)/2)
        # we take the middle value as the quick-sort pivot
        pivot = in_list[mid]
        # remove the middle element
        in_list.pop(mid)
        # create two partition: one for the values less than pivot and one for the values more than pivot
        partition1=[]
        partition2=[]
        for k in in_list:
            if k <= pivot:
                partition1.append(k)
            else:
                partition2.append(k)
        # merge the two sorted list and the pivot value
        sorted_list.extend(quick_sort(partition1))
        sorted_list.append(pivot)
        sorted_list.extend(quick_sort(partition2))
        return sorted_list
    elif in_list:
        # the following only occurs when in_list has only one element. A list with single element is sorted
        sorted_list.append(in_list[0])
    return sorted_list


random_list = random.sample(population=range(0,100000),k=10000)
sorted_list = random_list.copy()
# print(random_list)

# python sort() uses Timsort algorithm
start = time.time_ns()
sorted_list.sort(key=None,reverse=False)
end=time.time_ns()
sort_time = (end-start)/1000
print("Elapsed time for built-in python sort (Timsort): %d us"%(sort_time))


# merge sort script
start = time.time_ns()
sorted_merge=merge_sort(random_list)
end=time.time_ns()
merge_time = (end-start)/1000
# print(sorted_merge)
print("Elapsed time for merge sort: %d us" % merge_time)

# quick sort script
start = time.time_ns()
sorted_quick=quick_sort(random_list)
end=time.time_ns()
quick_time = (end-start)/1000
# print(sorted_quick)
print("Elapsed time for quick sort: %d us" % quick_time)

# print(merge_time/sort_time)
# print(quick_time/sort_time) 
