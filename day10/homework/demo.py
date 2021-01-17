#继承  被继承的类，父类， 继承的类：子类
class Animal:
    name = None
    age = None
# 让猫和狗来继承这些
class Dog(Animal):
    def lookGate(self):
        print(self.name,"看大门，看了",self.age)

class Cat(Animal):
    def catchMouse(self):
        print(self.name,"在抓老鼠")

dog=Dog()
dog.name="哈士奇"
dog.age=15
dog.lookGate()




