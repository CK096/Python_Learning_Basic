# .upper()     # 全部大写
# .lower()     # 全部小写
# .strip()     # 去除前后空格
# .count()     # 计算有多少一样的字符串
# .replace()   # 替换文字
# .split()     # 切割字符串成列表

text = "    Banana,Apple,Orange,Apple    "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Apple","Grape"))
print(text.split(","))
print(text.count("Apple"))
print(text.upper().lower().strip().replace("apple","Grape").split(","))
#可以同时使用多个字符串处理功能(左到右)

#####################################################################################

#.len()#计算有多少字
#.startswith()#开头带有什么字
#.endswith()#结尾带有什么字

new = "Python"
print(len(new))
print(new.startswith("Py"))
print(new.endswith("thon"))
print(new.startswith("Py") and new.endswith("thon"))
#输出回答是Bool(True,False)

file = "cat.jpg"
files = "main.py"
url = "https://google.com"

if file.endswith(".jpg"):
    print("Image File")

if file.endswith(".py"):
    print("Python File")

if url.startswith("https://"):
    print("Secure Website")
  
#检查是不是网址或者哪个格式的文件也可以用得到
