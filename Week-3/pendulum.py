# I import math in order to use pi
import math

# Defined the variables
def period(L, g=9.8):

    # If variables are not numbers, the user gets a TypeError with an explanation.
    if isinstance(L, (float, int)) != True:
        print(TypeError + 'Value entered fot L is not a nuber.')
    if isinstance(g, (float, int)) != True:
        print(TypeError + 'Value entered fot g is not a nuber.')  

    #If the variabe for gravity is 0, the user gets a ValueError with an explanation.
    if g == 0:
        print(ValueError + 'Value entered for gravity can not be 0 (The pendulum would not work)')    
      
    # This is the equation
    T = 2*math.pi*((L/g)**0.5)

    # Value for T is returned
    return T

print(period('lol', ))