def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints)==0:
        return 0,0
    else:
        Max=ints[0]
        Min=ints[0]
        temp=0
        for value in ints:
            if value >Max:
                Max=value
            if value<Min:
                Min=value
            
        return(Min,Max)

def test_function(test_case):
    if len(test_case)>0:
        print ("Pass" if ((min(test_case), max(test_case)) == get_min_max(test_case)) else "Fail")
    else:
        print("Pass" if ((0,0)==get_min_max(test_case)) else "Fail")
#egde case 1: large list     
test_function([i for i in range(20000)])

#egde case 2: large list   with large negative numbers 
# your solution failed on this test case  
test_function([i for i in range(-200000,-20000)])

#egde case 3: large list   with large positive numbers  randomized
import random
test_function([random.randint(1000000,99029002002) for i in range(-200000,20000)])
#edge case 4:list with single positive number
test_function([1])
#edge case 5:empty list
test_function([])
