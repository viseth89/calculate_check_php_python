class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()



class AddSubtract:
  def __init__(self, first, second):
    self.first = first
    self.second = second

  def sumof(self):
    return int(self.first) + int(self.second)

  def productof(self):
    return int(self.first) * int(self.second)

    # product = int(first) + int(second)




# name = input('Please enter your name : ')
rate = input('Please enter your hourly rate: ')
hours = input('Please enter how many hours you worked')
base = AddSubtract(rate, hours)

print(base.sumof())
print('The product is ' + str(base.productof()) + ' test')
