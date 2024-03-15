#
# D e c i s i o n T r e e . p y
#

# This code group contains functions reformulate the information in the decision tree
# created by sklearn.

###############################################################
# This function converts a 1D tree into a sequence of values interspersed by knot locations,
# i.e., v[0], k[0], v[1], k[1], ... k[n-1], v[n].  The implied piecewise functions is:
#
#         / v[0]    if x < k[0]
#  f(x) = | v[i]    if (k[i + 1] < x) and (x < k[i])
#         \ v[n]    if k[n - 1] < x
#
# The function is recursive, because the code is compat.  Of course, a while loop and a stack
# structure would be faster, but the extra complexity seems gratuitous for the size of the
# problems being considered.

def SplineOrd0(tree, index=0):
  leftIndex = tree.children_left[index]
  rightIndex = tree.children_right[index]

  if leftIndex == rightIndex:    # is a leaf
    return [float(tree.value[index])]

  else:
    result = SplineOrd0(tree, leftIndex)
    rightResult = SplineOrd0(tree, rightIndex)

    result.append(tree.threshold[index])
    result.extend(rightResult)

    return result


def Curve(spline, lim):
  lowLim,highLim = lim
  nSeg = (len(spline) + 1) // 2

  result = [(lowLim,spline[0])]
  for segNum in range(nSeg - 1):
    segVal = spline[2*segNum]
    knot = spline[2*segNum + 1]
    nextVal = spline[2*segNum + 2]

    result.append((knot,segVal))
    result.append((knot,nextVal))

  result.append((highLim, spline[len(spline)- 1]))

  return result