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
