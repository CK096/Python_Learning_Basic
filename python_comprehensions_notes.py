# -*- coding: utf-8 -*-
"""
Python 推导式笔记（Comprehensions）
适合初学者复习，可保存到 GitHub。

内容：
1. List Comprehension（列表推导式）
2. 使用 if 筛选元素
3. 使用 if-else 转换元素
4. 处理字符串与 Dictionary
5. Set Comprehension（集合推导式）
6. Dictionary Comprehension（字典推导式）
7. 常见错误与练习
"""


# ============================================================
# 1. List Comprehension（列表推导式）
# ============================================================
# 列表推导式可以用更简洁的语法创建新的 List。
#
# 基本语法：
# [表达式 for 变量 in 可迭代对象]
#
# 表达式：决定放入新 List 的内容
# for：逐个取出元素
# in：指定数据来源


# 普通写法：把 1 到 10 的数字平方
def square(x):
    return x * x


squares_loop = []
for number in range(1, 11):
    squares_loop.append(square(number))

print("普通写法的平方结果：")
print(squares_loop)


# 列表推导式写法
squares = [number * number for number in range(1, 11)]

print("列表推导式的平方结果：")
print(squares)


# ============================================================
# 2. List Comprehension + if：筛选元素
# ============================================================
# 语法：
# [表达式 for 变量 in 可迭代对象 if 条件]
#
# if 在这里负责筛选。
# 只有符合条件的元素才会加入新 List。

numbers = [3, 8, 11, 14, 17, 20]

# 只保留偶数
even_numbers = [number for number in numbers if number % 2 == 0]
print("偶数：", even_numbers)  # [8, 14, 20]

# 只保留大于 10 的数字
large_numbers = [number for number in numbers if number > 10]
print("大于 10 的数字：", large_numbers)  # [11, 14, 17, 20]


# ============================================================
# 3. 同时筛选和转换
# ============================================================
# 表达式放在最前面，if 条件放在 for 后面。
# 先判断条件；符合条件时，再把表达式的结果放入新 List。

numbers = [2, 3, 4, 5, 6, 7]

# 只筛选偶数，并计算平方
even_squares = [number ** 2 for number in numbers if number % 2 == 0]
print("偶数的平方：", even_squares)  # [4, 16, 36]

# 筛选大于 5 的数字，再乘以 3
tripled_large_numbers = [number * 3 for number in numbers if number > 5]
print("大于 5 的数字乘以 3：", tripled_large_numbers)  # [18, 21]


# ============================================================
# 4. List Comprehension + if-else：根据条件转换
# ============================================================
# 语法：
# [结果A if 条件 else 结果B for 变量 in 可迭代对象]
#
# 注意：这里的 if-else 负责决定每个元素变成什么，
# 并不是筛选元素。每个元素都会产生一个结果。

numbers = [1, 2, 3, 4, 5]

size_labels = ["Big" if number >= 3 else "Small" for number in numbers]
print("数字大小标签：", size_labels)
# ['Small', 'Small', 'Big', 'Big', 'Big']


# ============================================================
# 5. 处理字符串
# ============================================================
names = ["alice", "BOB", "Alexander", "tom", "AMANDA"]

# 只保留长度大于 4 的名字，并转换成大写
long_names_upper = [name.upper() for name in names if len(name) > 4]
print("长度大于 4 的大写名字：", long_names_upper)
# ['ALICE', 'ALEXANDER', 'AMANDA']

# 常用字符串方法：
# name.upper()  -> 转换成大写
# name.lower()  -> 转换成小写
# len(name)     -> 取得字符串长度


# ============================================================
# 6. 处理由 Dictionary 组成的 List
# ============================================================
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 55},
    {"name": "Charlie", "score": 92},
    {"name": "David", "score": 48},
]

# 筛选成绩大于等于 60 的学生，只提取姓名
passed_students = [
    student["name"]
    for student in students
    if student["score"] >= 60
]
print("及格学生：", passed_students)  # ['Alice', 'Charlie']


products = [
    {"name": "Keyboard", "price": 150},
    {"name": "Mouse", "price": 80},
    {"name": "Monitor", "price": 600},
    {"name": "Headset", "price": 120},
    {"name": "USB Cable", "price": 20},
]

# 筛选价格小于 200 的商品，只提取名称
cheap_product_names = [
    product["name"]
    for product in products
    if product["price"] < 200
]
print("价格低于 200 的商品：", cheap_product_names)


# ============================================================
# 7. Set Comprehension（集合推导式）
# ============================================================
# 语法：
# {表达式 for 变量 in 可迭代对象 if 条件}
#
# Set 会自动去除重复值，而且不保证元素显示顺序。

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_large_numbers = {number for number in numbers if number > 2}
print("大于 2 且不重复的数字：", unique_large_numbers)  # {3, 4, 5}


# ============================================================
# 8. Dictionary Comprehension（字典推导式）
# ============================================================
# 基本语法：
# {key: value for 变量 in 可迭代对象}
#
# 加入筛选条件：
# {key: value for 变量 in 可迭代对象 if 条件}
#
# key 和 value 之间必须使用冒号 : 分隔。

products = [
    {"name": "Keyboard", "stock": 10},
    {"name": "Mouse", "stock": 25},
    {"name": "Monitor", "stock": 5},
]

# 商品名称作为 key，库存作为 value
stock_dictionary = {
    product["name"]: product["stock"]
    for product in products
}
print("商品库存：", stock_dictionary)
# {'Keyboard': 10, 'Mouse': 25, 'Monitor': 5}

# 只保留库存大于等于 5 的商品
available_stock = {
    product["name"]: product["stock"]
    for product in products
    if product["stock"] >= 5
}
print("库存至少为 5 的商品：", available_stock)

# 商品名称作为 key，折后价格作为 value；
# 只保留原价小于 200 的商品。
products_with_prices = [
    {"name": "Keyboard", "price": 150},
    {"name": "Mouse", "price": 80},
    {"name": "Monitor", "price": 600},
    {"name": "Headset", "price": 120},
    {"name": "USB Cable", "price": 20},
]

discount_prices = {
    product["name"]: product["price"] * 0.9
    for product in products_with_prices
    if product["price"] < 200
}
print("折后价格：", discount_prices)
# {'Keyboard': 135.0, 'Mouse': 72.0, 'Headset': 108.0, 'USB Cable': 18.0}


# ============================================================
# 9. 三种推导式的区别
# ============================================================
# List Comprehension：
# [表达式 for item in data]
# 结果是 List；保留顺序和重复值。
#
# Set Comprehension：
# {表达式 for item in data}
# 结果是 Set；自动去除重复值，不保证显示顺序。
#
# Dictionary Comprehension：
# {key: value for item in data}
# 结果是 Dictionary；建立 key 和 value 的对应关系。
#
# 额外注意：
# (表达式 for item in data) 是 Generator Expression，
# 它不是 List Comprehension，也不会立即生成完整的 List。


# ============================================================
# 10. 常见错误
# ============================================================
# 错误 1：把 < 和 <= 混淆
# price < 100   -> 小于 100，不包含 100
# price <= 100  -> 小于或等于 100，包含 100
#
# 错误 2：把筛选 if 和 if-else 混淆
# [x for x in numbers if x > 5]
# -> 只保留大于 5 的元素
#
# ["Big" if x >= 3 else "Small" for x in numbers]
# -> 每个元素都会变成 "Big" 或 "Small"
#
# 错误 3：想建立 Dictionary，却只写一个表达式
# {product["price"] * 0.9 for product in products}
# -> 这是 Set Comprehension，不是 Dictionary Comprehension
#
# Dictionary 必须写 key: value：
# {product["name"]: product["price"] * 0.9 for product in products}
#
# 错误 4：不要把变量命名为 list、dict、set 等内置类型名称。
# 建议使用 numbers、items、result 等名称。


# ============================================================
# 11. 练习题（先自己完成，不要急着看答案）
# ============================================================
# 练习 1：
# numbers = [1, 2, 3, 4, 5, 6]
# 使用 List Comprehension，创建每个数字的平方。
#
# 练习 2：
# numbers = [3, 8, 11, 14, 17, 20]
# 使用 List Comprehension，只保留偶数。
#
# 练习 3：
# names = ["Amy", "Alexander", "Bob", "Amanda"]
# 筛选长度大于 4 的名字，并全部转换成大写。
#
# 练习 4：
# students = [
#     {"name": "Amy", "score": 90},
#     {"name": "Bob", "score": 55},
#     {"name": "Chris", "score": 72},
# ]
# 使用 List Comprehension，提取成绩大于等于 60 的学生姓名。
#
# 练习 5：
# products = [
#     {"name": "Pen", "price": 5},
#     {"name": "Bag", "price": 80},
#     {"name": "Laptop", "price": 2500},
# ]
# 使用 Dictionary Comprehension，只保留价格小于 100 的商品，
# 商品名称作为 key，价格乘以 0.9 作为 value。


print("\nPython 推导式笔记示例运行完毕。")
