"""

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping
the adjacent elements
O(n)

"""



def Bubble(arr):
    n = len(arr)

    for i in range(n):
        #total iteration

        for j in range(n-i-1):
            # last element is already sorted so "-1 "

            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

                # arr[j], arr[j+1] = arr[j+1], arr[j]   Direct swap

def display(arr):
    for ir in arr:
        print(ir)


arr = [2, 4, 3,76,45,78,98,34,2,1,56,43,0,11,22,33,54,9]
Bubble(arr)
display(arr)


