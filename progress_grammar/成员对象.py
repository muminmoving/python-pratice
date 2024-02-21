class Student:
    name = None

    def say_hi(self):
        print(f"你好，我叫{self.name}")

    def say_hi1(self, msg):
        print(f"你好，我叫{self.name}, {msg}")


stu = Student()
stu.name = "hoking"
stu.say_hi()
stu.say_hi1("你个der")
