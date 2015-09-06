def make_bricks(small, big, goal):
  if small + big * 5 < goal:
    return False
  elif goal % 5 == 0:
    if big * 5 < goal:
      return goal - big * 5 <= small
    else: 
      return True
  else:
    return goal % 5 <= small