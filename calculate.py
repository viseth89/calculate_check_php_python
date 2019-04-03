# def calculateCheck(rate, hours):
#   tax80 = int(rate)*int(hours)*.80
#   basePay = int(rate)*int(hours)

#   return basePay, tax80

# Here we create a basic function to do multiplication
# It takes 2 parameters and multiplies them to give us 'Base Pay'

class ReturnValue(object):
  def __init__(self, basePay, tax80):
     self.basePay = basePay
     self.tax80 = tax80


def calculateCheck(x, y):
  basePay = x * y
  tax80 = x * y * .8

  return ReturnValue(basePay, tax80)