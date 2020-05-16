def sort_012(a):
 low=0
 high=len(a)-1
 mid=0
 while mid<=high :
	    if a[mid]==0:
	        a[low],a[mid]=a[mid],a[low]
	        low=low+1
	        mid=mid+1
	    elif a[mid]==1:
	        mid=mid+1
	    else:
	        a[mid],a[high]=a[high],a[mid]
	        high=high-1
 return a
def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
test_function([0])
