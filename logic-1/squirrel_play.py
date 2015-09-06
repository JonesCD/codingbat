def squirrel_play(temp, is_summer):
  if temp >= 60:
    return (temp <= 90 and is_summer == False) or (temp <= 100 and is_summer == True) 
  else:
    return False