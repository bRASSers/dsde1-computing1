import math

def period(L, g=9.8):
    T = 2*math.pi*((L/g)**0.5)
    return T

testvalues = period(1.2, )
print(testvalues)
