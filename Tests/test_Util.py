#
# t e s t _ U t i l . p y
#

# unit test package
from unittest import TestCase

# system packages
import numpy as np
from numpy import isclose

# libraries to be tested
import Util

class TestPolyVal(TestCase):
  def test_PolyVal_oa(self):
    coef = [1, 0, 0, 1]

    val = Util.PolyVal(coef, 0)
    self.assertEqual(1, val)

    val = Util.PolyVal(coef, 1)
    self.assertEqual(2, val)

    val = Util.PolyVal(coef, -1)
    self.assertEqual(0, val)

  def test_PolyVal_0b(self):
    coef = [-1, -2, -1]

    val = Util.PolyVal(coef, 0)
    self.assertEqual(-1, val)

    val = Util.PolyVal(coef, 1)
    self.assertEqual(-4, val)

    val = Util.PolyVal(coef, -1)
    self.assertEqual(0, val)

  def test_PolyVal_0c(self):
    coef = np.array([-1, -2, -1])
    x = np.array([0,1,-1])
    val = Util.PolyVal(coef, x)
    self.assertEqual([-1, -4, 0], val)

  def test_PolyVal_0d(self):
    coef = [1, 0.2, 0.7, 1, -0.5]
    val = Util.PolyVal(coef, 2)
    self.assertTrue(isclose(4.2, val))
    
    
class TestPolyStr(TestCase):
  def test_PolyStr_0a(self):
    coefs = [0, 1, 0, 1]
    result = Util.PolyStr(coefs, 'z')
    self.assertEqual('z^3 + z', result)

  def test_PolyStr_0b(self):
    coefs = [-1, 2, -3, 4]
    result = Util.PolyStr(coefs, 'q')
    self.assertEqual('4q^3 - 3q^2 + 2q - 1', result)

  def test_PolyStr_0c(self):
    coefs = [1, 0.2, 0.7, 1, -0.5]
    result = Util.PolyStr(coefs, 'x')
    self.assertEqual('-0.5x^4 + x^3 + 0.7x^2 + 0.2x + 1', result)
