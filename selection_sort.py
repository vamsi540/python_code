#--swapping would done at once only and only one
#--like it will select the min value among all the elements in the list
#--then it will swap that value with the where the min value is present

def sort(nums):
    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

nums = [5, 3, 8, 6, 7, 2]
sort(nums)
print(nums)