# set working directory
import os
path = r'C:\Users\nicka\OneDrive\Desktop\1 Modern Data Structures - GR5072\QMSS-GR5072_Spring2024\Week 7\Class Activity'
os.chdir(path)
os.getcwd()

# Import rocket and shuttle class
from Rocket_class import Rocket

# Initalize rocket at (0, 0)
rocket_0 = Rocket()
rocket_0.x
rocket_0.y

# Initalize rocket at (10, 5)
rocket_1 = Rocket(10,5)
rocket_1.x
rocket_1.y

# Move rocket_1 to (3, 4)
rocket_1.move_rocket(-7, -1)
rocket_1.x
rocket_1.y

# Show the distance between the two rockets
distance = rocket_0.get_distance(rocket_1)
print("The rockets are {} units apart.".format(distance))


