# 一个无序的、可变的数据结构，存储键值对
# 创建字典
person = {
    'name': 'Alice',
    'age': 30,
    'is_student': False
}

print(person)
print(person['name'])

# 添加/修改项
person['gender'] = 'female'
person['age'] = 31
print(person)

# 删除项
del person['gender']
print(person)

# 使用get方法获取值（更安全）
print(person.get('name'))
print(person.get('hobby', 'rain'))

# 遍历字典
for key, value in person.items():
    print(f'{key}: {value}')

# 合并字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
# merged = {**dict1, **dict2}
merged = dict1 | dict2
print(merged)
