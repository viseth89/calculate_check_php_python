# Python Refresher

# name = ''

from calculate import calculateCheck

print('hi')

# name = input('Please enter your name : ')
rate = input('Please enter your hourly rate: ')
hours = input('Please enter how many hours you worked')
base = ReturnValue(rate, hours)


# print('Your name is ' + name)
print('Your hourly rate is ' + rate)
print('You worked ' + hours + ' hours')
print('Your base pay is ' + str(base) )
print(base['tax80'] )

def calculateCheck(rate, hours):
  return int(rate)*int(hours)

