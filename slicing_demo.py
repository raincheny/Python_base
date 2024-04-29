# 切片是一种提取序列(如列表、元组、字符串)中的一部分或者多个部分的方法
# 用于从序列中获取一个子序列

lst = [0, 1, 2, 3, 4, 5]

print(lst[1:4])
print(lst[:4])
print(lst[3:])
print(lst[::2])

# 字符串和无组同样可以使用切片
s = "HELLO"
print(s[1:4])

t = (0, 1, 2, 3, 4, 5)
print(t[1:4])

# 负索引：使用负数作为start或stop来从末尾开始计数
lst = [0, 1, 2, 3, 4, 5]
print(lst[-3::-1])

# 浅复制
lst = [0, 1, 2, 3, 4, 5]
copy_lst = lst[:]
print(copy_lst)

# 反转序列
lst = [0, 1, 2, 3, 4, 5]
print(lst[:3:-1])

