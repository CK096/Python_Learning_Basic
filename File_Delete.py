import os
import shutil
import send2trash

# ===========================
# Python 删除档案、资料夹（安全版）
# ===========================

path = r"C:\Users\user\Desktop\workshop"

file_path = f"{path}/test.txt"
empty_folder = f"{path}/empty_folder"
folder = f"{path}/project_folder"


# ---------------------------
# 删除文件（先检查是否存在）
# ---------------------------

if os.path.exists(file_path):
    os.remove(file_path)
    print("文件已删除")
else:
    print("找不到文件")


# ---------------------------
# 删除空资料夹（先检查是否存在）
# ---------------------------

if os.path.exists(empty_folder):
    os.rmdir(empty_folder)
    print("资料夹已删除")
else:
    print("找不到资料夹")


# ---------------------------
# 删除整个资料夹（先检查是否存在）
# ---------------------------

if os.path.exists(folder):
    shutil.rmtree(folder)
    print("资料夹及所有内容已删除")
else:
    print("找不到资料夹")


# ---------------------------
# 丢到资源回收桶（最安全）
# ---------------------------

if os.path.exists(file_path):
    send2trash.send2trash(file_path)
    print("已移动到资源回收桶")
else:
    print("找不到文件")
