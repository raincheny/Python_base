# 基本的while 循环
count = 0
while count < 5:
    print(count)
    count += 1

# 使用break退出循环
count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1

# 使用continue 跳过当前迭代
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:  # 如果是偶数，则跳过
        continue
    print(count)

# 结合else,当while循环正常结束时（即不是break导致的）,将执行else块中的代码
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('loop ended normally.')
