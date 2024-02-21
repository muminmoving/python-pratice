class Student:
    """name = None
    age = None
    tel = None
    """

    # 构造方法
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    # 字符串方法
    def __str__(self):
        return f"hoking的姓名为{self.name}, 年龄为{self.age}"

    # 小于比较方法
    def __lt__(self, other):
        return self.age < other.age

    # 小于比较方法
    def __le__(self, other):
        return self.age <= other.age


stu1 = Student("hoking", 10, "12345678")
stu2 = Student("hoer king", 12, "123456789")

print(stu1.name)
print(stu1)
print(stu1 < stu2)
print(stu1 >= stu2)