"""三数之和与目标值最接近, 假设只有一个答案"""
def threeSumCloset(nums, target):
    nums.sort()
    midiff = 10000  # 初始化一个diff值，当然这样有点low
    res = 0
    for i in range(len(nums)):
        left = i+1
        right = len(nums)-1
        while left < right:
            sum = nums[left] + nums[i] + nums[right]
            diff = abs(target-sum)
            if diff < middiff:
                middiff = diff
                res = sum
            if sum == target:
                return sum
            elif sum < target:
                left += 1
            else:
                right -= 1
    return res
