# 列表生成式是Python内置的非常简单却强大的用来创建list的生成式
"""
基本语法
[expression for item in iterable if condition]

场景：
数据转换： 对一组数据进行某种转换生成新的列表
数据过滤： 基于某个条件过滤出列表中的部分元素
快速生成列表： 快速创建满足某种规则的列表
"""

# 创建一个包含0到9的偶数的平方的列表
even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)

# 两层循环，生成全排列
arrange = [m + n for m in 'ABC' for n in 'XYZ']
print(arrange)


def flib(max01):
    n, a, b = 0, 0, 1
    while n < max01:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

