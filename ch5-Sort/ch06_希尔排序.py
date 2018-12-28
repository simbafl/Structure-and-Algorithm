"""
希尔排序，也称递减增量排序，是插入排序的一种高效的改进版本。但希尔排序是非稳定排序算法。
对于插入排序：1. 在几乎排序好的序列中操作时效率高，即可达到线性排序的效率。2. 但插入排序一次只能移动一位，所以很低效。
对于希尔排序：先将整个待排序的记录序列分割成若干子序列分别进行直接插入排序，待整个序列中的记录基本有序时，再对全体记录进行依次直接插入排序。
步骤：
1. 选择一个增量序列t1,t2,..., tk, 其中t1 > tj, tk = 1
2. 按增量序列个数k，对序列进行k趟排序
3. 每趟排序，根据对应的增量ti，将待排序序列分割成若干长度为m的子序列，分别对各各子表进行直接插入排序。仅增量因子为1时，整个序列作为一个表来处理，表长度即为整个序列的长度。
"""
def shellSort(arr):
    import math
    gap = 1
    while (gap < len(arr)/3):
        gap = gap*3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr

