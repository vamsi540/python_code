#--values in the list which we are taking as input it should be contain sorted ordered elements/items
#--in binary search first we have to metion the lower bound and upper bound
#--then we have to find the mid index value like (lower + upper)/2 (take the round off value)
#--then we have to check that number with searching number
#--if not matched then we have to change the lower/upper bound
#--first we have to check the searching value is smaller/bigger than the mid value
#--if smaller chnage the upper bound i.e; the mid value will become the upper bound.vice versa....
#--repeat the process until you get the value which you are finding.

pos = -1
def search(list, n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u)//2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False
list = [4,7,8,12,45,99]
n = 9
if search(list, n):
    print("found at",pos + 1)
else:
    print("not found")