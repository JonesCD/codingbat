def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)



def round10(num):
  if num % 10 >= 5:
    return num + 10 - (num % 10)
  else:
    return num - (num % 10)
  
  
"""
My first attempt involved converting to strings to manipulate
the numbers by the indexed digit position, but codingbat
did not allow this method.

def round10(num)
  numstr = str(num)
  if numstr[-1] >= 5:
    numstr[-2] = str(int(numstr[-2]) + 1)
  numstr[-1] = 0
  return int(numstr)

"""