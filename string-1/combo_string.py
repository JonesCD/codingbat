def combo_string(a, b):
  short = min(len(a), len(b))
  if short == len(a):
    return a + b + a
  else:
    return b + a + b