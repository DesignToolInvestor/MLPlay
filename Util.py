#
# U t i l . p y
#

import numpy as np


# Note on the order of the coefficients:  coef[i] is the coefficient of the term x^i.
def PolyVal1(coef, x):
  ord = len(coef) - 1
  result = x * coef[ord]

  for i in range(ord - 1, 0, -1):
    result = x * (coef[i] + result)
  result += coef[0]

  return result

def PolyVal(coef, xL):
  if isinstance(xL, np.number) or isinstance(xL, (int, float, complex)):
    return PolyVal1(coef, xL)
  else:
    result = [PolyVal1(coef, x) for x in xL]
    return result