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


#exp enumarate
students = ["Alex", "Ben", "Chris", "David", "Amy"]
scores = [80, 45, 90, 35, 55]

for index, (x, y) in enumerate(zip(students,scores),start=1): #代表索引从1开始
    if y < 60:
        print(index, x, y)

############################################################################################
#any()，all() 判断True/False

#any() 用来判断一组资料中，是否至少有一个元素为 True
#all() 用来判断一组资料中，是否所有元素都满足条件

#exp List()
scores = [45, 55, 80, 30]

result1 = any(score >= 60 for score in scores)
result2 = all(score >= 60 for score in scores)
print(result1) #输出结果是True （其中一个达成条件）
print(result2) #输出结果是False (不是全部达成条件)

#dictionary 版本，使用.value() 只取值
scores = {
    "Bob": 80,
    "Sam": 55,
    "Lee": 90,
    "Amy": 65
}

has_fail = any(score < 60 for score in scores.values())
everyone_pass = all(score >= 60 for score in scores.values())

print(has_fail)
print(everyone_pass)


