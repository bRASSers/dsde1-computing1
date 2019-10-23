import math


def period(L, g):
    T = 2*math.pi*((L/g)**0.5)
    return T

isinstance('L', (float, int))
while False:
    print(TypeError)

isinstance('g', (float, int))
while False:
    print(TypeError)

if 'g' == 0:
    print(ValueError)
