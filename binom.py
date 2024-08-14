from factorial import *

def binom(n, k):
  if k > n or k == 0:
    return 0
  return factorial(n) / (factorial(k) * factorial(n-k))
