from factorial import *

def binom(n, k):
  if k > n or if k ==0 or if n ==0:
    return 0
  return factorial(n) / (factorial(k) * factorial(n-k))
