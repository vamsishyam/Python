import threading as t
from time import sleep
from calc import add

print(add(26,12))

#function
def display_range(*lst):
    """ display a list received """
    for i in lst:
        print(i)
        sleep(1)


thread = t.Thread(target=display_range, args=(['a','b','c']))
thread.start()

#try except
try:
    f = open("sample.txt","w")
    f.write("Hello World")
except FileNotFoundError:
    print("File not found")
finally:
    f.close()

#class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)

person1 = Person("Vamsi", 34)
person2 = Person("Shyam", 26)

person1.display()
person2.display()

thread.join()

#entry point
if __name__ == '__main__':
    print('PyCharm')

