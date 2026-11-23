#Basic

# String 字符串，字母
name = "CK"
print(f'my name is {name}')
print(type(name))

#允许多个变量赋值
a = b = c = 1
a, b, c = 1, 2, "runoob"

# integer 整数
x = 11+7
y = 6
print(x)
print(x+y)
print('My age is',(x+y))
print(type(x+y))

# Float 小数点
gpa = 3.3
print(gpa)
print(f'my gpa is {gpa} mark')
print(type(gpa))

# integer+ Float
print(f'my friend is {x+y + gpa} mark')
print(type(x+y + gpa))
print(f'my friend is {x+y} mark')
print(type(x+y))

# String + Integer + Float
print(f'Student {name} is {x*y + gpa} mark')

#Boolean # True, False
Pass = True
print(f"Student {name} is {x*y + gpa} mark is {Pass}")
print(type(Pass))

# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

#===========================================
#Change Type

#显式型别转换
name = 'Ck'
age = 25
mark = 99.99
gamer = True

ages = float(age)
print("my age is " , (ages))
print(type(ages))

marks = int(mark)
print(f"my age is {mark}")
print(type(marks))

gamers = str(gamer)
print('i was gamer '+ str(gamers))
print(type(gamers))

#隐式型别转换
x = 10
y = 2.0
x = x*y
y = x+x
print(y)
print(type(y))

#====================================================

# input 取得使用者输入
item = input("想要购买的物品： ")
price = float(input("购买物品的价格： ")) #float(input()) 当输入需要小数点的时候
quantity = int(input("购买物品的数量： ")) #int(input()) 当输入需要整数的时候

total = price * quantity

print(f'你购买了{quantity} {item},总价值 RM{total}')
