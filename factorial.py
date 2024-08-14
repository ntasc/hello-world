def factorial(x):
  if x == 1:
    return 1
  else if x < 1:
    return 0
  else:
    return x * factorial(x-1)
