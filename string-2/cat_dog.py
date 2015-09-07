def cat_dog(str):
  cat_count = 0
  dog_count = 0
  for i in range(len(str) - 2):
    if str[i] == 'c' and str[i + 1] == 'a' and str[i + 2] == 't':
      cat_count += 1
    if str[i] == 'd' and str[i + 1] == 'o' and str[i + 2] == 'g':
      dog_count += 1
  if cat_count == dog_count:
    return True
  else:
    return False