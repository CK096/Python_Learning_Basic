# ==============================
# String Methods
# ==============================

# .upper()        全部转大写
# .lower()        全部转小写
# .capitalize()   第一个字串换成大写
# .title()        每个单字首字母大写，其余小写
# .strip()        去除前后空白
# .replace()      替换指定文字
# .split()        切割字串，回传 List
# .count()        计算指定字串出现次数

text = "    Banana,Apple,Orange,Apple    "

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.strip())
print(text.replace("Apple","Grape"))
print(text.count("Apple"))
print(text.split(","))
print(text.upper().lower().strip().replace("apple","Grape").split(","))
#可以同时使用多个字符串处理功能(左到右)

# ==============================
# Built-in Function
# ==============================

# len()           计算长度（字元数）

# ==============================
# Boolean Methods
# ==============================

# .startswith()   是否以指定文字开头
# .endswith()     是否以指定文字结尾

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
  
# 常用来检查网址、文件格式、文件副档名等。
