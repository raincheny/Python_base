import random
from math import ceil, floor, pi, e

# 科学计数表示法表示浮点数
print(1.23e9)
print(1.2e-3)
print(pi)  # 圆周率
print(e)
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

# 数字运算
print(5 ** 3)  # 幂运算
print(pow(5, 3))
print(17 // 3)  # 整除
print(floor(4.9))  # 返回数字的下舍整数
print(ceil(4.1))  # 返回数字的上入整数
print(round(4.4))  # 返回数字的四舍五入值

# 三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
para_str = r"""这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)

# 字符串内建函数
print("hello World".capitalize())  # 将字符串的第一个字母变成大写，其他字母变小写
print("hello".center(20, "*"))  # 生成20个长度的字符串，hello居中，左右*补齐
print("hello".count("l", 0, 4))  # 从位置0开始到位置4结束，l出现的次数
print("hello".encode('GBK', 'strict'))  # 以指定的编码格式编码字符串, 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError
print("hello China".startswith("he", 0, 10))  # 从位置0到10，是否以he开头
print("hello China".endswith("he", 0, 10))
print("hello China".find("l", 1, 4))  # 从位置1到4，从左到右，l出现的位置，返回索引值，不存在的话返回-1,rfind方法是从右到左
print("hello world".isalnum())  # 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
print("hello中国".isalpha())  # 如果字符串至少有一个字符并且所有字符都是字母或文字则返回 True，否则返回 False。
print("aaa".isdigit())  # 检测字符串是否只由数字组成
print("hello中国".islower())  # islower() 方法检测字符串是否由小写字母组成
print("hello中国".isupper())  # 检测字符串中所有的字母是否都为大写
s1 = "hello"
print(s1.join("world"))  # 连接
print(len("hello"))  # 获取长度
print("hello".ljust(20, "*"))  # 获取20长度字符串，hello在左边，其余部分*补齐
print("Hello".lower())  # 转小写
print("hello".upper())  # 转大写
print("   hello".lstrip())  # 结果"hello"
print("888hello".lstrip("8"))  # 结果hello
print(max("hello"))  # 获取最大字母
print(min("hello"))  # 获取最小字母
print("hello hello hello world".replace("hello", "china"))
print("hello hello hello world".replace("hello", "china", 2))  # 替换不超过 2 次
print("hello world   ".rstrip())  # 删除末尾空格
print("hello world....".rstrip("."))  # 删除末尾.
print("hello world   ".lstrip())  # 删除末尾空格
print(" hello world ".strip())  # 执行lstrip rstrip
print("hello world china".split(" "))  # ["hello","world","china"]
print("hello,world,china".split(","))
print("abChina".swapcase())  # 大写转小写，小写转大写
print("this is string".title())  # 所有单词首字母大写
