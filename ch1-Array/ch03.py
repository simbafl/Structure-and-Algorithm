"""
对于四数之和问题
遍历一次，记录所有两数之和的可能
再遍历一次，即可转化为两数之和的问题
"""
def fourSum(nums, target):
    res = set()
    dic = {}
    numLen = len(nums)
    nums.sort()
    for i in range(numLen):
        for j in range(i+1, numLen):
            key = nums[i]+nums[j]
            if key not in dic.keys():
                dic[key] = [(i, j)]
            else:
                dic[key].append((i,j))
    for i in range(numLen):
        for j in range(i+1, numLen-2):
            exp = target - nums[i] - nums[j]
            if exp in dic.keys():
                for tmp in dic[exp]:
                    if tmp[0] > j:
                        res.add((nums[i], nums[j], nums[tmp[0]], nums[tmp[1]]))

    return [list(i) for i in res]

"""
[-1, 0, 0, -2, 2, 1]

[out]: 
[[-1,0,0,1], [-2,-1,1,2], [-2,0,0,2]]

"""
