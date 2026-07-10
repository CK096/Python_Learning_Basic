# ==========================
# File Handling（文件读写）
# ==========================

# 文件路径
file_path = r"C:\Users\user\Desktop\workshop\test.txt"

# --------------------------
# 写入（Write）
# --------------------------

# "w"
# 建立新文件，如果文件已经存在，会覆盖旧内容
with open(file_path, "w") as file:
    file.write("Apple\nBanana\nOrange")

# --------------------------
# 追加（Append）
# --------------------------

# "a"
# 建立新文件，如果文件已经存在，会把内容加到最后面
with open(file_path, "a") as file:
    file.write("\nWatermelon")

# --------------------------
# 读取（Read）
# --------------------------

# read() -> 一次读取全部内容（String）
with open(file_path, "r") as file:
    data = file.read()

print(type(data))      # <class 'str'>

# readlines() -> 一次读取全部内容（List）
with open(file_path, "r") as file:
    data2 = file.readlines()

print(type(data2))     # <class 'list'>

# --------------------------
# read()
# --------------------------

# String，所以 for 会一个字一个字读取
for char in data:
    print(char)

# --------------------------
# readlines()
# --------------------------

# List，所以 for 会一行一行读取
for line in data2:
    print(line)

# --------------------------
# ⭐ 推荐写法（Modern Python）
# --------------------------

# 不需要 readlines()
# Python 会自动一行一行读取文件
with open(file_path, "r") as file:
    for line in file:
        print(line.strip())
