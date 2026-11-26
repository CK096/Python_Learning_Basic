#Local Variable(局部变量)
def test():
    message = "Hello Python" #这里的 message 是在 Function 内部创建的，所以外面用不到
    print(message)
test()


#Global Variable（全局变量）
number = 100 # 因为 number 是在外面， Function外面，所以Function 可以读取它

def calculate():
    print(number)

calculate()

# Big Example
number = 50

def calculate():
    number = 100 #这里创建了一个新的 Local Variable (number),它不会改变外面的 (number)
    print(number)

calculate()
print(number) #这里读取的是 Global Variable，所以仍然是 50

# Global Keyword
number = 50

def calculate():
    global number #这是告诉pthon,我不是要创建新的 Local Variable，而是要使用外面的 Global Variable
    number = 100

calculate()
print(number)
#输出是 100

# example
score = 80

def update_score():
    global score
    score += 10
    print(score)

update_score() #输出是90
print(score) #输出也是90，因为使用了global

#没有 global：修改的是局部变量（如果在函数内赋值）。
#有 global：可以修改外面的全局变量


#=========================================================
# Python 中的作用域

# 变数范围与作用域
# LEGB 作用域顺序

# L - local 区域
# E - Enclosed
# G - Global 全域
# B - Build in


# 变数范围
c = 10 #这个属于 G-global全域 (全部范围都可用)
a = 6 #这个不会显示在function_one 里面，因为function_one 是一个（local-区域）
def function_one():
    a = 1 #function_one 的 local 区域
    print("a: ",a)
    def function_two():
        b = 2 #function_two 的 local 区域
        print("a: ",a) # 放在function_two的时候原本的function_one 的 (a)是 E-enclosed
        print("b: ",b)
        print("c: ", c)
    function_two()

function_one()
print("global A:", a) #这个不是调用function_one(local-区域)，所以a是最开始那个

from math import e # B - Build in (调用模组来使用)
print(e)
print(round(e))

def function_three():
    print(e)
function_three()
