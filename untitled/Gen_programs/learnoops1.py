class Animal:
    def __init__(self, name):
        self.name = name
        #print(self.name)
    def move(self):
        print("New Objects born are moving")


a = Animal('noobs')

#print(a.name)

class Dog(Animal):
    def __init__(self):
        print("idle state")

    def woof(self):
        print("New Dog objects will woof")

    def run(self):
        print("New Dog objects will run")

d = Dog()
d.move()
a.move()
d.woof()






