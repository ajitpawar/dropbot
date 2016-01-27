import matplotlib.pyplot as plt
from math import sqrt
import numpy as np


def dy(distance, m):
    return m*dx(distance, m)

def dx(distance, m):
    return sqrt(distance/(m**2+1))

# Returns co-ordinates of the arrow
def get_arrow_head(p1, p2, length=1, width=0.50):

	lst = [p1,p2]
	x = [i[0] for i in lst]
	y = [i[1] for i in lst]
	slope, y_intercept = np.polyfit(x, y, 1)

	# check if slope is infinite (vertical line)
	if int(slope) == int(y_intercept):
		slope = 25.5

	# calculate intercept point
	delta_x = dx(length,slope)
	delta_y = dy(length,slope)
	if p2[0] < 0:	# if point is in left half
		delta_x = -1*delta_x
		delta_y = -1*delta_y
	intercept = (p2[0]-delta_x, p2[1]-delta_y)

	# slope of perpendicular line
	r_slope = -1*(1/slope)

	# calculate the adjacent points
	left = (intercept[0]-dx((width/2),r_slope), intercept[1]-dy((width/2),r_slope))
	right = (intercept[0]+dx((width/2),r_slope), intercept[1]+dy((width/2),r_slope))
	top = p2

	return left, right, top, intercept


####################
#
# 	Test
# ##################
p1 = [1,1]
p2 = [1,10]
length=1
width=0.50

left,right,top,intercept = get_arrow_head(p1,p2,length,width)


####################
#
# 	Draw stuff
# ##################

# draw line
lst = [p1,p2]
x = [i[0] for i in lst]
y = [i[1] for i in lst]
plt.plot(x, y, '--')

# draw intercept point
plt.plot(intercept[0], intercept[1], '*')

# draw the arrow
ls = [left,right,top,left]
x1 = [i[0] for i in ls]
y1 = [i[1] for i in ls]
plt.plot(x1, y1, 'b')

# draw the 3 points
plt.plot(left[0], left[1], '*')
plt.plot(right[0], right[1], '*')
plt.plot(top[0], top[1], '*')

# draw grid
plt.xticks(np.arange(-10,10,1))
plt.yticks(np.arange(-10,10,1))
plt.grid()
plt.show()