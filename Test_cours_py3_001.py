from math import sqrt

class Point(object):
    "Point Géométrique"

def affiche_point(p):
    print("coord. horizontale =", p.x, "coord. verticale = ", p.y)

def distance(p1,p2):
    a2 = (p2.x - p1.x)**2
    b2 = (p2.y - p1.y)**2
    d = sqrt(a2 + b2)
    return(round(d,4))
 

p1 = Point()
p2 = Point()

p1.x = 3.0
p1.y = 4.0
p2.x = 7.0
p2.y = 8.0

affiche_point(p1)
affiche_point(p2)
print("Distance entre les points = ", distance(p1,p2))
