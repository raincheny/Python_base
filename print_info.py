#!/usr/bin/env python3
import keyword

print('hello, world')
print('The quick brown fox', 'jumps over', 'the lazy dog')
print('300 + 200 =', 300 + 200)

print('1024 * 768 = ', 1024 * 768)
# name = input('please enter your name:')
# print('hello', name)

# python关键字
print(keyword.kwlist)

# 语句长时使用\实现多行
total = "a" + \
        "b" + \
        "c"
print(total)

# 在[]、{}、()中的多行语句，不需要使用反／
total = [
    'item_one', 'item_two', 'item_three'
    , 'item_four', 'item_five'
]
print(total)
