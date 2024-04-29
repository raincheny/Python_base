# 迭代列表
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# 迭代字符串
for letter in 'apple':
    print(letter)

# 使用range迭代数字序列
for i in range(5):
    print(i)

# 同时迭代多个序列
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f'{name} is {age} years old.')

# 迭代字典
dict_data = {'a': 1, 'b': 2, 'c': 3}
for key, value in dict_data.items():
    print(f'Key: {key}, Value: {value}')

# 下标
names = ['Alice', 'Bob', 'Charlie']
for i, name in enumerate(names):
    print(i+1, name)

