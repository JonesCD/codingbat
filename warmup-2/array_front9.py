def array_front9(nums):
  if len(nums) < 4:
    if 9 in nums:
      return True
    else:
      return False
  else:
    nums_four = nums[:4]
    if 9 in nums_four:
      return True
    else: 
      return False