# 基本的'if'语句
x = 10
if x > 5:
    print('x is greater than 5')

# if else 语句
x = 3
if x > 5:
    print('x is greater than 5')
else:
    print('x is not greater than 5')

# if-elif-else 语句
x = 5
if x > 10:
    print('x is greater than 10')
elif x == 5:
    print('x is 5')
else:
    print('x is not greater than 10 and x is not 5')

# 三元表达式,简短的if-else表达式
x = 5
message = 'x is even' if x % 2 == 0 else 'x is odd'
print(message)
print('x is greater than 5') if x > 5 else print('x is not greater than 5')

#
x = None
print('True') if x else print('False')

#
weight = float(input('请输入体重：(kg)'))
high = float(input('请输入身高：(m)'))
BMI = weight / (high ** 2)
print(f'您的肥胖指数为{BMI}')

if BMI < 18.5:
    print('您的体重过轻')
elif 18.5 <= BMI < 25:
    print('您的体重正常')
elif 25 <= BMI < 28:
    print('您的体重过重')
elif 28 <= BMI < 32:
    print('您的体重肥胖')
else:
    print("您的体重严重肥胖")
