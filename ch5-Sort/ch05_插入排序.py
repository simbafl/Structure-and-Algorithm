"""
插入排序思想类似于打扑克，插入相应位置
步骤：
1. 将第一待排序序列第一个元素看作一个有序序列，把第二个元素到末尾看作未排序序列
2. 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置(如果待插入元素与有序序列中某一元素相等，则将其插入相等元素后面).
"""
def insertSort(arr):
    for i in range(len(arr)):
        perIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current
    return arr
