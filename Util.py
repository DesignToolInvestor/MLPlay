#
# U t i l . p y
#

import numpy as np
import random


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

def PolyStr(coefL, varStr):
  ord = len(coefL) - 1

  result = ''
  for i in range(ord, -1, -1):
    coef = coefL[i]

    if (coef != 0):
      if (i < ord):
        if (0 < coef):
          result += ' + '
        elif (coef < 0):
          result += ' - '

      if (abs(coef) != 1) or (i == 0):
        if (i == ord):
          result += f'{coef}'
        else:
          result += f'{abs(coef)}'

      if 1 < i:
        result += f'{varStr}^{i}'
      elif i == 1:
        result += f'{varStr}'

  return result

def SetSeed(seed, dig=5):
  if seed is None:
    random.seed()
    seed = random.randint(0, 10 ** dig - 1)

  random.seed(seed)

  return seed