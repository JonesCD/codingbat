def alarm_clock(day, vacation):
  if day % 6 == 0:
    if vacation == True:
      return "off"
    else:
      return "10:00"
  else:
    if vacation == True:
      return "10:00"
    else: 
      return "7:00"