def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid]   
        R = arr[mid:] 
  
        mergeSort(L) 
        mergeSort(R)  
  
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
def rearrange_digits(arr):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    n = len(arr) 
    if n==0:
        return 0,0
    elif n==1:
        return arr[0],0
    else:
        mergeSort(arr)
        i=n-1
        j=n-2
        string1=""
        string2=""
        for x in range (i,-1,-2):
          string1=string1+str(arr[x])
        for x in range (j,-1,-2):
          string2=string2+str(arr[x])
        return(int(string1),int(string2))
    
    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0,1,2,3,4,5], [531,420]])
# Empty list
test_function([[], [0, 0]])
test_function([[i for i in range(0,101)], [int("".join(map(str,range(100,-1,-2)))), int("".join(map(str,range(99,-1,-2))))]])
test_function([[1],[1,0]])
