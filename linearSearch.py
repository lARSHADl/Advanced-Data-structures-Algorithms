"""
The time complexity of the algorithm is O(n).
Linear Search is rarely used practically

"""

arr = [4, 5, 8, 7, 0, 1, 2, 3, 20, 12, 45, 11]


def linearSearch(array, key):
    n = len(array)
    for i in range(0,n):
        if array[i] == key:
            return i
    return -1

res = linearSearch(arr, 1)

if res == -1:
    print("Element not found ")
else:
    print("Tne elemenet is found at the location " , res)
