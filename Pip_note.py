# ==========================================
# Python 学习笔记：pip
# ==========================================

"""
一、什么是 pip？

pip 是 Python 的套件管理工具（Package Installer）。

它可以帮助我们：
1. 安装第三方套件
2. 卸载不需要的套件
3. 查看已经安装的套件
4. 更新套件

可以把 pip 想象成手机的 App Store，
而 Package 就像可以安装的 App。
"""


# ==========================================
# 二、pip 的常用命令
# ==========================================

# 注意：
# 以下命令是在 CMD、Terminal 或 VS Code 终端执行，
# 不是直接写在 Python 程序中。

# 1. 安装套件
# pip install pandas

# 2. 卸载套件
# pip uninstall pandas

# 3. 查看已安装的套件
# pip list

# 4. 查看套件的详细信息
# pip show pandas

# 5. 更新套件
# python -m pip install --upgrade pandas


# ==========================================
# 三、pip 和 import 的区别
# ==========================================

"""
pip install：
负责安装套件。

import：
负责在 Python 程序中导入套件。

正确的使用流程：

第一步：在终端安装套件
pip install requests

第二步：在 Python 文件中导入套件
import requests

注意：套件通常只需要安装一次，
之后就可以在相同的 Python 环境中重复使用。
"""


# ==========================================
# 四、安装和使用第三方套件的例子
# ==========================================

# 第一步：在终端执行
# python -m pip install requests

# 第二步：在 Python 文件中编写以下代码

import requests

# 获取一个公开测试 API 的资料
response = requests.get(
    "https://jsonplaceholder.typicode.com/todos/1",
    timeout=10
)

# 检查请求是否成功
response.raise_for_status()

# 将 JSON 资料转换成 Python Dictionary
data = response.json()

print(data)


# ==========================================
# 五、常见的 Python 套件
# ==========================================

"""
1. requests
   用途：发送 HTTP 请求，与 API 交互。

2. pandas
   用途：处理表格、Excel 数据和数据分析。

3. openai
   用途：通过 OpenAI API 开发 AI 应用。

4. python-dotenv
   用途：从 .env 文件读取环境变量。

注意：
这些套件需要根据项目需要安装，
不需要一次全部安装。
"""


# ==========================================
# 六、pip 常见问题
# ==========================================

"""
问题 1：pip 不是内部或外部命令

可以尝试：
python -m pip --version

安装套件时可以使用：
python -m pip install requests

问题 2：ModuleNotFoundError

例如：
ModuleNotFoundError: No module named 'requests'

常见原因：
1. 还没有安装该套件。
2. 安装套件的 Python 环境与运行程序的环境不同。

解决方法：
在正在使用的 Python 环境中安装套件。

问题 3：为什么有时需要 python -m pip？

因为它可以明确使用当前 python 命令所对应的
Python 环境来运行 pip，通常更容易排查环境问题。
"""


# ==========================================
# 七、重要概念总结
# ==========================================

"""
Python：
编程语言。

Package：
别人开发好的代码套件。

pip：
安装和管理第三方套件的工具。

import：
在 Python 程序中导入套件。

记忆方法：

pip install = 安装
import = 使用
pip list = 查看
pip uninstall = 卸载
pip show = 查看详情
"""
