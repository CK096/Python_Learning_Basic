# .upper()     # 全部大写
# .lower()     # 全部小写
# .strip()     # 去除前后空格
# .replace()   # 替换文字
# .split()     # 切割字符串成列表

text = "    Banana,Apple,Orange,Apple    "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Apple","Grape"))
print(text.split(","))
print(text.upper().lower().strip().replace("apple","Grape").split(","))#可以同时使用多个字符串处理功能(左到右)
