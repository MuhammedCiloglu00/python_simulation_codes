"""
Muhammed Çiloğlu
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

# the specified function is defined as
def f(x):
    return np.sqrt(x)
# Determine a rectangular area inside the function and put points in the x and y coordinates of this area.
counting = 0.0
sub_area = 0.0
sub_area_list=[]
upper_area_list=[]
sampling= int(input("How many dots do you want? "))
# I named the total thrown points as the counting, and the area under the curve as the subArea.
while counting < sampling:
    x_coordinate = np.random.uniform(1,4)
    y_coordinate = np.random.uniform(0,2)
    # If the point thrown to the y coordinate is less than the value of the same point in the function, 1 is added to sub_area
    if  y_coordinate< f(x_coordinate):
        sub_area += 1
        sub_area_list.append((x_coordinate, y_coordinate))
    else:
        upper_area_list.append((x_coordinate, y_coordinate))
    counting += 1
    
    # When the loop is complete, 1 is added to counting
box_area= 6
# box field is entered
# If the ratio of the points under the curve to the total points is multiplied by the box area, we find the area below  
area=(sub_area/ counting) * box_area
tolerance= abs(((14/3)-area)/(14/3)*100)
# we calculate the margin of error as an absolute value
print("area =" ,area)
print("Your tolerance: %", tolerance )

plt.figure(figsize=(6,6))
plt.scatter([x_coordinate[0] for x_coordinate in sub_area_list], [x_coordinate[1] for x_coordinate in sub_area_list], marker=".",alpha=0.5,color='darkblue');
plt.scatter([x_coordinate[0] for x_coordinate in upper_area_list], [x_coordinate[1] for x_coordinate in upper_area_list], marker=".",alpha=0.5,color='red');

