import numpy as np
import matplotlib.pyplot as plt

class Ultra:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self):
        return self.a,self.b,self.c

    def __str__(self):
        return ('(%g, %g, %g)')%(self.a, self.b, self.c)

    def __repr__(self):
        return (('%s(%g,%g,%g)')%(self.__class__.__name__,self.a, self.b, self.c))

    def __add__(self, other):
        x = self.a + other.a
        y = self.b + other.b
        z = self.c + other.c
        return Ultra(x,y,z)

    def __sub__(self, other):
        x = self.a - other.a
        y = self.b - other.b
        z = self.c - other.c
        return Ultra(x,y,z)

    def __neq__(self):
        return Ultra(-self.a,-self.b,self.c)

    def __mul__(self, other): # * || dot product
        x = self.a * other.a
        y = self.b * other.b
        z = self.c * other.c
        return (x+y+z)

    def __matmul__(self, other): # @ || cross product
        g = self.a *other.b - self.b *other.a
        h = self.b *other.c - self.c *other.b
        i = self.c*other.a - self.a *other.a
        return Ultra(g,h,i)

    def __rmul__(self, other): # int*
        return self*other

u = Ultra(1,-1,0)
print(u)
print(repr(u))

v = Ultra(-1,1,0)
print(v)
print(repr(v))

print(u-v)
print(-v)
