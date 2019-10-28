# I import math in order to use pi
import math

# Defined the variables
def period(L, g=9.8):
     try:
        T = 2*math.pi*((L/g)**0.5)
        return T

     except:

        #If the variabe for gravity is 0, the user gets a ValueError with an explanation.
        if g == 0:
            raise ValueError

        #If the variabe for L is not a number, the user gets a TypeError with an explanation.
        elif isinstance(L, (float, int)) != True:
            raise TypeError

        #If the variabe for g is not a number, the user gets a TypeError with an explanation.
        elif isinstance(g, (float, int)) != True:
            raise TypeError