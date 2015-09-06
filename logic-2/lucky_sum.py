def lucky_sum(a, b, c):
  lst = [a, b, c]
  if 13 in lst:
    i = lst.index(13)
    return sum(lst[:i])
  else:
    return sum(lst)