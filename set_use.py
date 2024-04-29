# 一个无序的，不包含重复元素的集合数据结构
# 创建集合
fruits = {'apple', 'banana', 'cherry'}

# 使用set()函数从其它数据结构转换
fruits_list = ['apple', 'banana', 'cherry', 'apple']
fruits_set = set(fruits_list)
print(fruits_set)

# 添加元素
fruits.add('orange')
print(fruits)

# 删除元素，
# fruits.remove('bananas')  # 如果元素不存在，会引发keyError
fruits.discard('banana')  # 如果元素不存在，不做任何操作
print(fruits)

# 集合操作
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)  # 交集：{3}
print(a | b)  # 并集：{， 2, 3, 4, 5}
print(a - b)  # 差集: {1, 2}
print(a ^ b)  # 对称差集: {1, 2, 4, 5}
