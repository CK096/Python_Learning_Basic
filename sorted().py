# sorted () 排序

products = [
    {"name": "Apple", "price": 5},
    {"name": "Orange", "price": 3},
    {"name": "Banana", "price": 8}
]

names = ["John", "Amy", "Bob", "David"]

result = sorted(products, key=lambda x: x["price"]) #key = sorted() 规定好的参数
result2 = sorted(products, key=lambda x: x["price"],reverse =True) #revere 也是，不过它的用途是倒转顺序
result3 = sorted(products, key=lambda x: x["name"]) #按字母来排也是可以哦
result4 = sorted(names) #如果没用到Dictionary,这是普通用法

print(result)
print(result2)
print(result3)
print(result4)
