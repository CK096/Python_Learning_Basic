# sorted () 排序

products = [
    {"name": "Apple", "price": 5},
    {"name": "Orange", "price": 3},
    {"name": "Banana", "price": 8}
]

names = ["John", "Amy", "Bob", "David"]

#resorted()是用什么资料来排序,所以资料在前面
result = sorted(products, key=lambda x: x["price"]) #key = sorted() 规定好的参数
result2 = sorted(products, key=lambda x: x["price"],reverse =True) #revere 也是，不过它的用途是倒转顺序
result3 = sorted(products, key=lambda x: x["name"]) #按字母来排也是可以哦
result4 = sorted(names) #如果没用到Dictionary,这是普通用法

print(result)
print(result2)
print(result3)
print(result4)

=================================================================================================

# map() 把一个函数，依次用在 List 的每一个元素上

number = [1,2,3,4]

result = map(lambda x: x*2, number) #map()是用什么函数来改变资料,所以函数在前面

print(list(result)) #list()会吧结果变成list,因为result不算list
