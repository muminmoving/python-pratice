class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪")


class Cat(Animal):
    def speak(self):
        print("miaomiaomiao")


cat = Cat()
dog = Dog()

dog.speak()
cat.speak()
