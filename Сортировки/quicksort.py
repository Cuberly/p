nums = [4, 1, 6, 3, 2, 7, 8]
n = 1
while n < len(nums):
   for i in range(len(nums) - n):
       if nums[i] > nums[i + 1]:
           nums[i], nums[i + 1] = nums[i + 1], nums[i]
   n += 1