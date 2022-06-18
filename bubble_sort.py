#--in bubble sort we will use the concept of swapping
#--while swapping if 1st value is greater than 2nd value it will sawp

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

nums = [5, 3, 8, 6, 7, 2]
sort(nums)
print(nums)