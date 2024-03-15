#
# t e s t _ U t i l . p y
#

# unit test package
from unittest import TestCase

# system packages
import numpy as np

# libraries to be tested
import Util

class Test(TestCase):
  def test_PolyValA(self):
    coef = [1, 0, 0, 1]

    val = Util.PolyVal(coef, 0)
    self.assertEqual(1, val)

    val = Util.PolyVal(coef, 1)
    self.assertEqual(2, val)

    val = Util.PolyVal(coef, -1)
    self.assertEqual(0, val)

  def test_PolyValB(self):
    coef = [-1, -2, -1]

    val = Util.PolyVal(coef, 0)
    self.assertEqual(-1, val)

    val = Util.PolyVal(coef, 1)
    self.assertEqual(-4, val)

    val = Util.PolyVal(coef, -1)
    self.assertEqual(0, val)

  def test_PolyValC(self):
    coef = np.array([-1, -2, -1])
    x = np.array([0,1,-1])
    val = Util.PolyVal(coef, x)
    self.assertEqual([-1, -4, 0], val)

  def test_PolyValD(self):
    coef = [1, 0.2, 0.7, 1, -0.5]
    val = Util.PolyVal(coef, 2)
    self.assertEqual(2.4, val)