def last2(str):
  if len(str) < 2:
    return 0
    
  end = str[len(str) - 2:]
  count = 0
  
  for i in range(len(str) - 2):
    newstr = str[i : i + 2]
    if newstr == end:
      count += 1
      
  return count