def array123(nums):
  i = 0
  if len(nums) < 3:
    return False
  elif len(nums) == 3:
    if nums[0] == 1 and nums[1] == 2 and nums[2] == 3:
      return True
    else:
      return False
  else:
    for i in range(len(nums)):
      if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
        return True
      elif i < len(nums) - 3:
        i += 1
      else:
        return False