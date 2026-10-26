
import time

# 1. Epoch: Unix 时间戳的起点
print("Epoch:", time.ctime(0))

# 2. 获取当前 Unix 时间戳
timestamp = time.time()
print("Timestamp:", timestamp)

# 3. 获取本地时间对象
local_time = time.localtime()
print("Local time object:", local_time)

# 4. 格式化时间对象 -> 字符串
formatted_time = time.strftime(
    "%Y-%m-%d %H:%M:%S",
    local_time
)
print("Formatted time:", formatted_time)

# 5. 时间字符串 -> 时间对象
time_string = "1999-09-06 12:12:12"

time_object = time.strptime(
    time_string,
    "%Y-%m-%d %H:%M:%S"
)
print("Parsed time object:", time_object)

# 6. 把指定时间对象转换成字符串
print(
    "Original date:",
    time.strftime("%d/%m/%Y", time_object)
)
