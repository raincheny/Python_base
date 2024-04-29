import random

# 科学计数表示法表示浮点数
print(1.23e9)
print(1.2e-3)

# 十六进制数
print(0xff00)
print(0x770)

# 八进制
print(0o12)  # 零加上小写欧再加数字

# 二进制
print(0b1010)

# 随机函数
print(random.choice([2, 3, 4, 33, 22, 66, 5, 7, 4]))  # 从列表（也可以是元组、字符串）中获取一个随机内容
print(random.randrange(1, 100, 2))  # 从 1-100 中选取一个奇数，2表示递增基数
print(random.randrange(100))  # 从 0-99 选取一个随机数
print(random.random())  # 返回随机生成的一个实数，它在[0,1)范围内
lista = [20, 16, 10, 5]
random.shuffle(lista)  # 将序列的所有元素随机排序
print("随机排序列表 : ", lista)
print(random.uniform(5, 10))  # 返回一个浮点数 N，取值范围为如果 x<y 则 x <= N <= y，如果 y<x 则y <= N <= x
