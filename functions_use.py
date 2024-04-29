# 一元二次方程求解
import math


def root_value(a, b, c):
    delta = a ** 2 - 4 * a * c
    if delta >= 0:
        x1 = (-b + math.sqrt(a ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(a ** 2 - 4 * a * c)) / (2 * a)
        return x1, x2
    else:
        print('方程式无实根')


value = root_value(5, 4, 1)
print(value)


# 位置参数
# 按照顺序传递
def greet(name, greeting):
    return f"{name}, {greeting}"


print(greet('Rain', 'Hello'))


# 默认参数，如果在调用时没有提供默认值，那么将使用默认值
def greet(name='Rain', greeting='Hello'):
    return f"{name}, {greeting}"


print(greet())
print(greet('Rainbow', 'Hi'))
print(greet(name='cyclouds'))


# 关键字参数，传递参数时使用参数的名字，这样不需要考虑参数的顺序
def describe_pet(animal, name):
    return f"I have a {animal} named {name}"


print(describe_pet(animal="cat", name="Whiskers"))
print(describe_pet(name="Whiskers", animal="cat"))


# 可变位置参数(*args)，收集额外的位置参数为一个元组
def add(*numbers):
    return sum(numbers)


print(add(1, 2, 3, 4))


# 可变关键字参数(**kwargs)
def introduce(**kwargs):
    for key, value1 in kwargs.items():
        print(f"{key}: {value1}")


introduce(name="Alice", age=30, hobby="Reading")


# 参数解包,在调用函数时使用`*`和`**`来解包列表/元组和字典作为参数
def draw_point(x, y):
    # do something
    pass


coords = (3, 4)
draw_point(*coords)  # 解包元组为位置参数

info = {'x': 5, 'y': 7}
draw_point(**info)  # 解包字典为关键字参数


# 函数注解：可以为参数和返回值提供注解，增加代码的可读性(但不强制执行类型)
def greet(name: str, age: int) -> str:
    return f"My name is {name} and I am {age} years old."


# 递归函数： 一个函数在内部调用自身本身，这个函数就是递归函数

def fach(n):
    if n == 1:
        return 1
    return n + fach(n - 1)


print(fach(10))
