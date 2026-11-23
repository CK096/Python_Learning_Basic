# Dictionary 里面再放Dictionary
students = {"student1": {"name": "Tom","age": 20,"score": 85},"student2": { "name": "John", "age": 21, "score": 90 }}

# 如果我想获取 Tom 的成绩 (连续访问两层Dictionary)
print(students["student1"]["score"])

# 取得所有学生资料
for key, value in students.items():
    print(key, value)

# 如果想直接取得每位学生的名字和成绩
for key, value in students.items():
    print(value["name"], value["score"])

# 修改资料
students["student1"]["score"] = 70

# 新增资料
students["student1"]["Class"] = "1A"

#===================================================

# Dictionary 里面再放List
students = {
    "John": [80, 75, 90],
    "Mary": [95, 88, 92],
    "Tom": [60, 70, 65],
    "Lisa": [85, 90, 95]
}

high_average = 0

for key, value in students.items():
    average = sum(value)/len(value) #拿list的值来用
    print(f"Student: {key}, Average Score: {average:.2f}")
    if average >= 80:
        high_average += 1
print("Average Score Students More Then 80 Have",high_average,"People")
