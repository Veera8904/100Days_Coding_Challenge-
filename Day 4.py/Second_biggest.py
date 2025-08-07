#Second biggest number in a list with one loop
def second_biggest(nums):
    max_num = secondmax_num = float('-inf')
    for num in nums:
        if num > max_num:
            secondmax_num = max_num
            max_num = num
        elif num > secondmax_num and num != max_num:
            secondmax_num = num
    return secondmax_num

nums = [10,30,20,15,40,25,35]
print("Second bigest number is",second_biggest(nums))
