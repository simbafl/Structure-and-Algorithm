"""
归并排序：建立在归并操作上的一种有效的排序算法，是采用分治法的一个非常典型的应用
步骤：
1. 使用分治法，先拆分成小序列
2. 然后递归解决每个小序列，解决完再合并
3. 最后合并得到结果。
"""
def merge(S1, S2, S):
    # 把两个有序序列S1, S2合并成一个有序序列S
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1
 
def merge_sort(S):
    # 结合merge方法, 对S进行排序
    n = len(S)
    if n < 2:
        return
    mid = n // 2  # 根据mid将S一分为二
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)  # 对每个子序列递归调用
    merge_sort(S2)
    merge(S1, S2, s)  # 从树的最底层开始，由下往上, 由小往大合并子序列。最后得到总序列
 
A = [1, 2, 4, 6, 3, 0, 2]
merge_sort(A)

