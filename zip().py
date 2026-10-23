# python Zip 函式

usernames = ["Bob","Steve","Sam"]
passwords = ("123","321","555")


users = zip(usernames, passwords)
print(users) # 会回传 <zip object at 0x0000026DB3DEE040>

#同一个 zip object 被迭代后，已经取出的数据不会自动恢复

#需要用for 迭代出Tuple
for user in users:
    print(user)

#如果没有users的话这样也直接可以用
for a, b in zip(usernames,passwords):
    print(f"name: {a}, password {b}")

#换成List
print(list(users)) #可以得到List (需要先#注解掉之前的迭代出的tuple)

#换成Dict
user_dict =dict(users)
print(user_dict) # key = usernames , value = paswords

for key,value in user_dict.items():
    print(f'name : {key}, Password : {value}')


#如果 usernames 或 passwords 里面少掉其中一组号码或者名字， 显示出来的List,Tuple,Dict 就会少一组
#如果有第三行 List/Tuple exp: zip(usernames, passwords,birthdays), 这样的情况下Dict 会报错
