def floorSqrt(x) : 
    if (x == 0 or x == 1) : 
        return x 
    start = 1
    end = x    
    while (start <= end) : 
        mid = (start + end) // 2
        if (mid*mid == x) : 
            return mid 
        if (mid * mid < x) : 
            start = mid + 1
            ans = mid 
        else : 
            end = mid-1
    return ans 
def Square_root(x):
    if x>=0:
     return floorSqrt(x)
    else:
     return "Error"
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if Square_root(input_list) ==number:
        print("Pass")
    else:
        print("Fail")
#test_case 0 :empty list
test_function([0, 0])
#test_case 1:list with large positive value
test_function([23432432432432432432444,153076557422])
#test_case2:list with negative value
test_function([-213213231213,"Error"])
