scores = {"Alice": 85,"Bob": 55,"Charlie": 92,"David": 48,"Emma": 70}
result = {"Pass": [],"Fail": []}

for key, value in scores.items():
    if value >= 60:
        result["Pass"].append(value)
    else:
        result["Fail"].append(value)

print(result)
