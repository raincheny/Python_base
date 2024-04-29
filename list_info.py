my_list = [1, 2, 3, 4, 5]
names = ['rain', 'cyclouds', 'chenyun']
mix_list = [1, 'rain', 3.4, [1, 2, 3]]
print(names[0])  # 访问元素
names[1] = 'cycloud'  # 修改元素
print(names[1])
names.append('david')  # 在列表尾部添加
print(names)
names.insert(2, 'cy')  # 在指定位置添加
print(names)
names.remove('cy')  # 删除指定值
print(names)
del names[3]  # 删除指定位置的值
print(names)
name_popped = names.pop()  # 删除最后一个值并返回它
print(names)
print(name_popped)
print(len(names))  # 获取列表长度
names.sort()  # 排序列表
print(names)
names.reverse()  # 反转列表
print(names)
