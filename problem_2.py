def pivotedBinarySearch(arr, n, key): 
    pivot = findPivot(arr, 0, n-1); 
    if pivot == -1: 
        return binarySearch(arr, 0, n-1, key); 
    if arr[pivot] == key: 
        return pivot 
    if arr[0] <= key: 
        return binarySearch(arr, 0, pivot-1, key); 
    return binarySearch(arr, pivot+1, n-1, key); 
def findPivot(arr, low, high): 
    if high < low: 
        return -1
    if high == low: 
        return low 
    mid = int((low + high)/2) 
    if mid < high and arr[mid] > arr[mid + 1]: 
        return mid 
    if mid > low and arr[mid] < arr[mid - 1]: 
        return (mid-1) 
    if arr[low] >= arr[mid]: 
        return findPivot(arr, low, mid-1) 
    return findPivot(arr, mid + 1, high) 
def binarySearch(arr, low, high, key): 
  
    if high < low: 
        return -1
    mid = int((low + high)/2) 
    if key == arr[mid]: 
        return mid 
    if key > arr[mid]: 
        return binarySearch(arr, (mid + 1), high, 
                                            key); 
    return binarySearch(arr, low, (mid -1), key); 

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return(pivotedBinarySearch(input_list,len(input_list),number))

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

#egde test 1  empyt string
test_function([[], 1])
#egde test 2  large list
test_list=[i for i in range (1011,10000)]+[i for i in range (0,1011)]
test_function([test_list, 6])
#egde test 3  large list with negative numbers
test_list=[i for i in range (1011,10000)]+[i for i in range (-1000,1011)]
test_function([test_list, -60])
#edge test 4 for single input
test_function([[1],0])
