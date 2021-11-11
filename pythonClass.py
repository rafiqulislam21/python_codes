class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def another_fun(a, b):
        c = a + b
        return c

    def my_fun(self):
        print("Hello world")


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1.another_fun(2, 3))
p1.my_fun()
