# 195. 

**<font color=red>难度: Easy</font>**

## 刷题内容

> 原题连接

* https://leetcode.com/problems/tenth-line/

> 内容描述
```
Given a text file file.txt, print just the 10th line of the file.

Example:

Assume that file.txt has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Your script should output the tenth line, which is:

Line 10
Note:
1. If the file contains less than 10 lines, what should you output?
2. There's at least three different solutions. Try to explore all possibilities.
```
## 解题方案

> 思路 1

beats 25.71%
```bash
tail -n +10 file.txt | head -n 1
```
> 思路 2

```bash
awk 'NR==10' file.txt

awk 'NR==10{print $0}' file.txt

awk 'NR==10' file.txt | more

```
> 思路 3

beats 97.71%
```bash
sed -n 10p file.txt
```

总结：
1. 多练吧，几天不用
[shell基础](https://github.com/fenglei110/Linux-Tools/tree/master/shell)