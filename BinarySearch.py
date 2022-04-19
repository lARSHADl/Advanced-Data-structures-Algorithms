"""
Uses Divide and conquer method
time complexity O(n)

working:

    Compare x with the middle element.
    If x matches with the middle element, we return the mid index.
    Else If x is greater than the mid element, then x can only be in the right half subarray after the mid element. So we recur for the right half.
    Else (x is smaller) recur for the left half.

"""



def  binary(arr, key, low , high ):

    mid = int(low+high/2)
    if arr[mid] == key:
        return mid
    elif arr[mid]>key:
        high = mid-1
        return binary(arr,key,low,high)
    elif arr[mid]>key:
        low = mid+1
        return binary(arr, key, low, high)
    else:
        return -1

array = [1,5,4,3,2,6,7,8,4,2,2]
array.sort()
key = 9

res  = binary(array,key,0,len(array)-1)

if res == -1:
    print("THe element is not fpund")
else:
    print("The eleement ", key , "is found at  location ", a)