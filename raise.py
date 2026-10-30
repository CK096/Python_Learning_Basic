# Python 中的 raise

## 1. 什么是 raise？

`raise` 是 Python 中用来主动抛出异常（Exception）的关键字。

当程序遇到不符合要求的情况时，可以使用 `raise` 主动报告错误。

基本语法：

```python
raise ExceptionType("Error Message")
```

例子：

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")

print("Program continues")
```

输出：

```text
ValueError: Age cannot be negative
```

因为 `raise` 抛出了异常，所以后面的代码不会继续执行。

## 2. 常见的异常类型

| Exception | 用途 |
|---|---|
| ValueError | 值不符合要求 |
| TypeError | 数据类型不符合要求 |
| ZeroDivisionError | 除数为零 |
| IndexError | List 索引超出范围 |
| KeyError | Dictionary 找不到指定 Key |
| FileNotFoundError | 找不到指定文件 |
| Exception | 通用异常类型 |

例子：

```python
# ValueError
age = -1

if age < 0:
    raise ValueError("Invalid age")


# TypeError
raise TypeError("Invalid data type")


# ZeroDivisionError
raise ZeroDivisionError("Cannot divide by zero")
```

## 3. raise 配合 try / except

`raise` 可以和 `try/except` 一起使用。

`raise` 负责抛出异常，`except` 负责捕捉异常。

```python
try:
    age = -5

    if age < 0:
        raise ValueError("Age cannot be negative")

    print(age)

except ValueError as e:
    print(f"Error: {e}")

print("Program continues")
```

输出：

```text
Error: Age cannot be negative
Program continues
```

执行流程：

1. 执行 try。
2. 检查 age 是否小于 0。
3. 条件成立，执行 raise。
4. 跳到 except 捕捉 ValueError。
5. 执行 except 里面的代码。
6. 继续执行后面的程序。

注意：

如果没有合适的 except 捕捉异常，异常会向外传播；如果一直没有被处理，程序会终止当前执行流程。

## 4. raise 在 OOP 中的应用

在 Class 中，可以使用 raise 来保护对象的数据。

例子：

```python
class BankAccount:

    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.balance = balance


account = BankAccount(-100)
```

输出：

```text
ValueError: Balance cannot be negative
```

这里的 raise 可以防止创建余额为负数的账户。

### 在提款功能中的应用

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        return self.balance


account = BankAccount(100)

try:
    account.withdraw(200)

except ValueError as e:
    print(f"Error: {e}")
```

输出：

```text
Error: Insufficient balance
```

## 5. raise 和 continue 的区别

两者用途完全不同。

### continue

`continue` 用来跳过当前这一次循环，直接进入下一次循环。

```python
numbers = [10, -3, 20]

for number in numbers:

    if number < 0:
        continue

    print(number)

print("Program continues")
```

输出：

```text
10
20
Program continues
```

### raise

`raise` 用来主动抛出异常。

```python
numbers = [10, -3, 20]

for number in numbers:

    if number < 0:
        raise ValueError("Number cannot be negative")

    print(number)

print("Program continues")
```

输出：

```text
10
ValueError: Number cannot be negative
```

### 两者比较

| 比较 | continue | raise |
|---|---|---|
| 主要用途 | 跳过当前循环 | 抛出异常 |
| 是否跳过当前循环 | 是 | 不属于循环控制语句 |
| 是否可以继续循环 | 可以 | 没有捕捉异常时不可以 |
| 是否需要 try/except | 不需要 | 可以配合使用 |
| 常见用途 | 跳过无效数据 | 报告违反规则的操作 |

## 6. 什么时候使用 raise？

适合使用 raise 的情况：

- 年龄不能小于 0。
- 商品价格不能小于或等于 0。
- 银行账户余额不能为负数。
- 提款金额不能超过账户余额。
- 用户输入不符合程序规定。

如果只是想跳过某个数据，可以考虑 continue。

如果需要明确报告错误，并阻止不合法的操作，可以使用 raise。

---

## 7. 总结

| Keyword | 用途 |
|---|---|
| try | 尝试执行可能发生异常的代码 |
| except | 捕捉和处理异常 |
| raise | 主动抛出异常 |
| continue | 跳过当前循环 |
| break | 结束整个循环 |
| finally | 无论是否发生异常，通常都会执行 |

**最重要的概念：**

`raise` = 主动抛出异常。

`except` = 捕捉异常。

`continue` = 跳过当前循环。

`break` = 结束整个循环。
