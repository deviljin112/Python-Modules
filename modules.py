# Task
# get user input of a float number
# check if the number is lower than .50 then round the figure to lower end
# check if the number is greater than .51 then round the figure to higher end
# example - num_float = 23.66 - round it to 24, num_float = 23.50 - round it to lower end

import math
import random

try:
    number = float(input("Input a Float Number.\n=> "))
except:
    print("That is not a float value!")
else:
    print(f"Starting number: {number}")

    if number % 1 < .5:
        output = math.floor(number)
    else:
        output = math.ceil(number)

    print(f"Formatted number: {output}")
