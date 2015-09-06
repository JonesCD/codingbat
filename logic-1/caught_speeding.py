def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    speed -= 5
  
  if speed - 81 > 0:
    return 2
  elif speed - 61 > 0:
    return 1
  else:
    return 0