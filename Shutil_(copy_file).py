import shutil

# ===========================
# Python 复制档案（shutil）
# ===========================

path_file = r"C:\Users\user\Desktop\workshop"

# 原始档案
source_file = f"{path_file}/source.txt"

# 复制后的档案
copy_file = f"{path_file}/next.txt"


# ---------------------------
# copyfile()
# ---------------------------
# 只复制文件内容
# 不复制权限、修改时间等资料
# destination 必须是完整的文件名称
#
# 语法：
# shutil.copyfile(source, destination)

shutil.copyfile(source_file, copy_file)



# ---------------------------
# copy()
# ---------------------------
# 复制文件内容
# 会复制文件权限（Permission）
# destination 可以是文件，也可以是资料夹
#
# 语法：
# shutil.copy(source, destination)

# 复制成另一个档案
shutil.copy(source_file, copy_file)

# 或复制到资料夹
# shutil.copy(source_file, path_file)



# ---------------------------
# copy2()
# ---------------------------
# 功能最完整
# 会复制：
# - 文件内容
# - 文件权限（Permission）
# - 修改时间（Modified Time）
# - 存取时间（Access Time）
# - 其他 Metadata（依作业系统而定）
#
# 适合用来备份档案
#
# 语法：
# shutil.copy2(source, destination)

shutil.copy2(source_file, copy_file)



# ===========================
# 三个函数比较
# ===========================
#
# copyfile()
# ✔ 复制内容
# ✘ 不复制权限
# ✘ 不复制修改时间
# ✘ 不能直接复制到资料夹
#
# copy()
# ✔ 复制内容
# ✔ 复制权限
# ✘ 不复制修改时间
# ✔ 可以复制到资料夹
#
# copy2()
# ✔ 复制内容
# ✔ 复制权限
# ✔ 复制修改时间
# ✔ 可以复制到资料夹
# ✔ 最适合备份
#
# 小口诀（快速记住）
# copyfile() → 只复制内容（最快）
# copy()     → 内容 + 权限
# copy2()    → 内容 + 权限 + 时间（最完整，备份最常用）
