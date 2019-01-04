"""
数组中三数之和等于定值
初始化头尾指针，随i遍历共同向中间移动`
"""
def threeSum(nums):
    array = []
    nums.sort()
    for i in range(len(nums)-2):
        if i==0 or nums[i] > nums[i-1]:
            left = i+1
            right = len(nums)-1
            while left<right:
                ident = nums[left] + nums[i] + nums[right]
                if ident == 0:
                    array.append([nums[left], nums[i], nums[right]])
                    left += 1
                    right -= 1
                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
                elif ident < 0:
                    left += 1
                else:
                    right -= 1
    return array
