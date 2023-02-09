def find_insert_position(input_list,n,target):
    '''
    we used the BINARY SEARCH method for inserting the given target element.
    it finds the suitable  index position by using this binary searching technique and the 
    returns the suitable index position for the target element.
    '''
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if input_list[mid]==target:
            return mid
        elif input_list[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return end+1
input_list=[1,2,4,5,7,8,19,25,30]
n=len(input_list)
target=27
print(find_insert_position(input_list,n,target))
