'''
geometry.py
Contains analytical geometry functions to compute line slope, 
distance between points, line intercepts, and line intersections.
'''

from math import sqrt, fabs

#  Python 3.5 has math.inf, but 3.4 does not
from sys import version_info
if version_info.major == 3 and version_info.minor == 5:
    from math import inf
else:
    inf = float("inf")


def floatequals(a, b):
    '''
    Returns True if the floating-point values a and b are
    close enough in value to be considered equal; otherwise,
    the function returns False.  The parameters are considered
    equal when they are within 0.001 of each other.
    '''
    return a == b or fabs(a - b) < 0.001


def distance(x1, y1, x2, y2):
    '''
    Computes the distance between the points (x1,y1) and (x2,y2),
    where x1, y1, x2, and y2 are numbers.
    '''
    return sqrt(((x2-x1)**2)+((y2-y1)**2))


def slope(x1, y1, x2, y2):
    '''
    Computes the slope of the line that passes between the points 
    (x1,y1) and (x2,y2).  The function returns inf if a vertical 
    line passes throught the two points.  The funnction's behavior is 
    undefined if the two points are identical.  
    x1, y1, x2, and y2 are numbers.
    '''
    if (x2-x1) != 0:
        return (y2-y1)/(x2-x1)
    else:
        return inf

def intercept(x1, y1, x2, y2):
    '''
    Computes the y-intercept of the non-vertical line that 
    passes through the points (x1,y1) and (x2,y2).  The 
    function returns the x-intercept if the line is vertical.  
    Two identical points are interpreted to be on a 
    vertical line.
    '''
    if (x2-x1) != 0:
        return y1-((y2-y1)/(x2-x1))*(x1)
    else:
        return x1

def lineequation(x1, y1, x2, y2):
    '''
    Returns a string representation of a line passing through the points
    (x1,y1) and (x2,y2).  The result is in the form y = mx + b for 
    non-vertical lines and x = b for vertical lines.  The representation
    is as simple as possible; e.g., 
         y = 3x - 2      not y = 3x + -2
         y = x + 3       not y = 1x + 3
         y = 5           not y = 0x + 5
         x = 4           a vertical line
    '''
    
    if (x2-x1) != 0:
        m = (y2-y1)/(x2-x1)
        b = y1-((y2-y1)/(x2-x1))*(x1)        
        if m == 1.0 and b == 0.0:
            return "y = x"
        elif m == -1.0 and b == 0.0:
            return "y = -x"
        elif m == 1.0:
            if b < 0.0:
                return "y = x - " + str(b*(-1))
            return "y = x + " + str(b)
        elif m == -1.0: 
            if b < 0.0:
                return "y = -x - " + str(b*(-1)) 
            return "y = -x + " + str(b)
        elif m == 0.0:
            if b == 0.0:
                return "y = 0"
            elif b < 0.0:
                return "y = -" + str(b)
            return "y = " + str(b)
        elif b == 0.0:
            return "y = " + str(m) + "x"      
        elif b < 0.0:
            return "y = " + str(m) + "x - " + str(b*(-1))
        return "y = " + str(m) + "x + " + str(b)
    else:
        return "x = " + str(x1)

def intersection(m1, b1, m2, b2):
    '''
    Computes the (i_x, i_x) intersection point of the lines 
    y = m1x + b1 and y = m2x + b1.  Returns None if the lines 
    do not intersect in a single point.
    '''
    return None   # Replace with your implementation


if __name__ == '__main__':
    pass 