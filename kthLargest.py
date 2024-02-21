# Made By Milton
# Processor Information
# - Processor: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
# - System Model: HP Pavilion x360 Convertible 14m-dy0xxx
# - Cores: 4
# - Base speed: 2.42 GHz


# Question: Suppose you have a group of N numbers and 
# would like to determine the kth largest.


# Naive Solution 1
# - Read the N numbers into an array, arr, of size N.
# - Sort arr in decreasing order based on some sorting
# algorithm (e.g., bubblesort).
# - Return the element arr[k].

import time
import random

beg = time.time()

# basic implementation of bubble_sort
def bubble_sort(arr):

  # for(i=0; i<N; i++)
  for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
      if arr[j] < arr[j + 1]:
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp


def solution_1(arr, k):

  # Test case to make sure k number isn't higher 
  # than length of N and N isn't empty
  if k > len(arr) or k < 0:
    return "Doesn't exist -- Error"

  else:
    bubble_sort(arr)

    return arr[k - 1]


# Naive Solution 2
# - Read the first k numbers into an array, arr, of size k.
# - Sort arr in decreasing order based on some sorting algorithm (e.g., bubblesort).
# - Next, read each remaining element one by one. As a new 
# element arrives, it is ignored if it is smaller than the arr[k].
# - Otherwise, it is placed in its correct spot in arr, 
# bumping one element out of the array.
# - When the algorithm ends, arr[k] is returned as the answer.
def solution_2(arr_main, k):

  # Test case to make sure k number isn't higher than length of N and N isn't empty
  if k > len(arr_main) or k < 0:
    return "Doesn't exist -- Error"

  else:
    # create a different array that reads first k numbers
    arr = arr_main[:k]

    for i in range(len(arr), len(arr_main)):

      if arr_main[i] < arr[k - 1]:
        continue
      else:
        arr[k - 1] = arr_main[i]
        bubble_sort(arr)

    return arr[k - 1]

# set value for N
N = random.sample(range(0, 100000000), 1000)
#print(N)

# print("Solution 1 - The kth largest number is: ",
#       solution_1(N, 2))

print("Solution 2 - The kth largest number is: ",
      solution_2(N, 2))

end = time.time()

print("Execution time", end-beg)