#!/usr/bin/python3

class Grand:
    def hello_g(self):
        print("grand")

class Father(Grand):
    id = 4
    def hello_f(self):
        print("father")



obj1 = Grand()
obj2 = Father()

print(obj1.__class__)
print(obj1.__class__.__name__)

print(obj2.__class__.__name__)
print(obj2.__dict__)
