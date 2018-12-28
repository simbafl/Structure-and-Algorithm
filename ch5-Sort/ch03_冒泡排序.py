"""
冒泡排序简单直接，但是基本没有实用性
步骤：
1. 比较相邻的两个元素，如果第一个比第二个大，就交换两个
2. 对每一对相邻元素做同样的操作，从开始第一对到结尾的最后一对，执行完最后一位是最大的数
3. 针对所有元素重复以上的操作，除了最后一个
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较
"""
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
