class AddSubtract:
  def __init__(self, first, second):
    self.first = first
    self.second = second

  def sumof(self):
    return int(self.first) + int(self.second)

  def productof(self):
    return int(self.first) * int(self.second)

  def tax80(self):
        return int(self.first) * int(self.second) * .80

  def tax75(self):
        return int(self.first) * int(self.second) * .75

  def tax66(self):
        return int(self.first) * int(self.second) * .66

  def tax60(self):
        return int(self.first) * int(self.second) * .60

  def calculatewOT(self):
    if(int(self.second) > 40):
      base = int(self.first) * int(self.second) * .80
      othours = int(self.second)-40
      otrate = int(self.first)*1.5
      otpay = othours * otrate
      total = base + otpay
      return otpay, total, othours
    else :
      return int(self.first) * int(self.second) * .80


    # product = int(first) + int(second)




# name = input('Please enter your name : ')
rate = input('Please enter your hourly rate: ')
hours = input('Please enter how many hours you worked: ')
base = AddSubtract(rate, hours)

print('The sum is ' + str(base.sumof()) + ' addition')
print('The product is ' + str(base.productof()) + ' multiplication')
print('The total after 20% reduction is ' + str(base.tax80()) + ' after taxes')
print('The total after 25% reduction is ' + str(base.tax75()) + ' after taxes')
print('The total after 33% reduction is ' + str(base.tax66()) + ' after taxes')
print('The total after 40% reduction is ' + str(base.tax60()) + ' after taxes')
print('The total after 40% reduction is ' + str(base.tax60()) + ' after taxes')
print('The total with OT and 20% reduction is ' + str(base.calculatewOT()) + ' after taxes')
print('The total with OT pay is ' + str(base.calculatewOT()[0])  )
print('The total with OT pay is ' + str(base.calculatewOT()[1])  )
print('The total with OT pay is ' + str(base.calculatewOT()[2])  )



# def add_subtract(value1, value2):
#   sumOfValues = value1 + value2
#   productOfValues = value1 * value2
#   return sumOfValues, productOfValues

# b = add_subtract(10,12)
# print(b[0])
# print(b[1])
# Function that returns 2 values, and how to access/retrieve






#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()


