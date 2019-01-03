"""给定一个字符串，寻找最长无重复字串长度，当然必须连续

1. 初始一个头指针，字典，最大长度l，当前指针。
2. 遍历同时，记录每个字符当前位置
     如果该元素出现在字典中，并且在start位置后面
         那就让start在出现位置后移动一位，因为此时start和i之间没有重复元素
     把当前元素位置重新赋值

     计算此时i和start位置之间长度，和l比较

"""

def SubString(s):
    l = 0
    start = 0
    dic = {}
    for i in range(len(s)):
        cur = s[i]
        if cur not in dic.keys():
            dic[cur] = i
        else:
            if dic[cur] >= start:
                start = dic[cur] + 1
            dic[cur] = i
        if i-start+1 > l:
            l = i-start+1
     return l
