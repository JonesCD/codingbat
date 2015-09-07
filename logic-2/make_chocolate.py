def make_chocolate(small, big, goal):
  most_big = goal / 5
  
  if big >= most_big:
    if small >= goal - most_big * 5:
      return goal - most_big * 5
    else:
      return -1
  
  elif big < most_big:
    if small >= goal - big * 5:
      return goal - big * 5
    else:
      return -1
      
  else:
    return -1