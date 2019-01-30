# 192.  Word Frequency

**<font color=red>难度: Medium</font>**

## 刷题内容

> 原题连接

* https://leetcode.com/problems/word-frequency/

> 内容描述

```
Write a bash script to calculate the frequency of each word in a text file words.txt.

For simplicity sake, you may assume:

words.txt contains only lowercase characters and space ' ' characters.
Each word must consist of lowercase characters only.
Words are separated by one or more whitespace characters.
Example:

Assume that words.txt has the following content:

the day is sunny the the
the sunny is is
Your script should output the following, sorted by descending frequency:

the 4
is 3
sunny 2
day 1
Note:

Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.
Could you write it in one-line using Unix pipes?
```

## 解题方案

> 思路 1

beats 50.99%
```bash
cat words.txt | egrep -o "[a-z]{1,}?" |sort|uniq -c|sort -r|awk '{print $2,$1}'
```

> 思路 2

beats 98.99%
```bash
cat words.txt | grep -P -o '\w+'|sort|uniq -c|sort -nr -k1|awk '{print $2,$1}'
```

> 思路 3

beats 99.29%
```bash
awk '{for(i=1;i<=NF;i++){words[$i]++}} END{for(i in words){print i, words[i]}}' words.txt | sort -k2 -r -n
```
总结：
1. 多练吧，几天不用
[shell基础](https://github.com/fenglei110/Linux-Tools/tree/master/shell)