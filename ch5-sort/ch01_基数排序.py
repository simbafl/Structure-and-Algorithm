"""
就地快速排序
步骤：
1. 从数列中挑出一个元素，成为‘基准’
2. 重新排序数列，排序之后基准值在数列中间位置，把大于基准值放在后面，小于基准值放前面，这就是分区操作
3. 递归把小于基准值元素的子数列和大于基准值的子数列排序
"""
def partition(A, p, r):
    pivot = A[r]  # 把A[r]作为基准值,也就是所有数和末尾数比较大小后，分割成三部分
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
 
def quickSort(A, p, r):
    """
    对数列排序
    p，r 分别为起始终止、索引
    """
    if p < r:
        q = partition(A, p, r)  # q为基准值索引
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)
 

