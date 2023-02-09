from functools import total_ordering


def get_missing_number(arr):
    '''
    first by using the 'n'we get the arrays length
    by 'm'we get the total numbers list since one number is missing from the list
    the we caluculate the sum of the numbers between 1 and 'n+1'
    since the missing number is the difference between actual sum and expected sum.
    '''
    n=len(arr)
    m=n+1
    total=m*(m+1)//2
    return total-sum(arr)

arr=[1,2,3,5]
print('the missing number is',get_missing_number(arr))