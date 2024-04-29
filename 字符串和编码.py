#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ASCII编码为1个字节，8比特，最大表示255
# Unicode编码为内存或者是网页服务器里的数据的编码，2字节，最大65535，操作系统和编程语言直接支持Unicode
# utf-8 可变长编码，1-6字节

# 获取字符的整数
print(ord('陈'))

# 获取整数对应的字符
print(chr(38472))
print('\u4e2d\u6587')

# 将unicode编码指定为ASCII
# encode:将字符串转换为字节串
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))

# 从网络或者磁盘上读取字节流，使用decode方法
# decode:将字节串转换为字符串
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 格式化输出
print('hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('rain', 100000000))
print('hi {r}'.format(r='rain'))
name = 'rain'
age = 18
print(f'hello, {name}! you are {age} years old.')
