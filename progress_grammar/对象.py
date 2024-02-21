class Student:
    name = None
    gender = None
    age = None
    country = None
    native_place = None


stu1 = Student()
stu1.name = "张三"
stu1.gender = "男"
stu1.age = 10
stu1.country = "中国"
stu1.native_place = "山东"


class Student1:

    def __init__(self, name, gender, age, country, native_place):
        self.name = name
        self.gender = gender
        self.age = age
        self.country = country
        self.native_place = native_place


stu1 = Student1("hoking", "男", 18, "china", "银河")
print(stu1.name, stu1.gender)
