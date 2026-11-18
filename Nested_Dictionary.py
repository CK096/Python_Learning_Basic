# Dictionary 里面再放Dictionary
students = {"student1": {"name": "Tom","age": 20,"score": 85},"student2": { "name": "John", "age": 21, "score": 90 }}

# 如果我想获取 Tom 的成绩 (连续访问两层Dictionary)
print(students["student1"]["score"]

# 取得所有学生资料
for key, value in students.items():
    print(key，value)

# 如果想直接取得每位学生的名字和成绩
for key, value in students.items():
    print(value["name"], value["score"])
