"""
选择排序同样简单直接，唯一的好处是不占用额外内存，复杂度O(n^2),对小数据集还算可以
步骤：
1. 在未排序的序列中找到最小的元素，放到未排序序列最起始位置
2. 再从剩余元素中继续寻找最小元素，放到已排序序列末尾
3. 重复第二步，直到所有元素均排序完毕
"""
def selectSort(arr):
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

