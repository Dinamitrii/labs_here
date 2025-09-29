import math
from os import WCONTINUED

lighthouse_height = 100.0 # meters

angle_of_view = 30.0 # degrees

if math.tan(angle_of_view) == math.sqrt(3):
    lighthouse_height = lighthouse_height / 2.0

print("lighthouse_height", lighthouse_height)



equation = lighthouse_height * math.sqrt(3)

print(equation)
