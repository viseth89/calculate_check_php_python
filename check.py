# Python Refresher

# name = ''

from calculate import calculateCheck



rate = ''
hours = ''

print('hi')

name = input('Please enter your name : ')
rate = input('Please enter your hourly rate: ')
hours = input('Please enter how many hours you worked')
base = calculateCheck(rate, hours)


print('Your name is ' + name)
print('Your hourly rate is ' + rate)
print('You worked ' + hours + ' hours')
print('Your base pay is ' + str(base) )

def calculateCheck(rate, hours):
  return int(rate)*int(hours)

