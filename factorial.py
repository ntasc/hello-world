def factorial(x):
  if x == 0:
    return 1
  elif x < 0:
    return 0
  else:
    return x * factorial(x-1)
