# BDS Homework 1 - Problem 6

# Estimate the value of pi

import random

random_xy_coords = []


number_of_coords = 100000

for coord in range(number_of_coords):
    random_coord = (random.uniform(-1,1), random.uniform(-1,1))
    random_xy_coords.append(random_coord)

# print(random_xy_coords)

count = 0

for x,y in random_xy_coords:
    if x**2 + y**2 <= 1:
        count += 1

# print(count)

pi = 4 * (count/number_of_coords)

print(pi)