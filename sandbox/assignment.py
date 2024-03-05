import math

rect_length = 5.0
rect_width = 5.0


def calculate_area(length, width):
	"""
	Calculate the area of a rectangle given the length and width
	Args:
		length(float):	the length of the rectangle
		width(float):the width of the rectangle

	Returns:
		float: the area of the rectangle
	"""

	return length * width


area = calculate_area(rect_length, rect_width)
print(f"The area of a rectangle of length: {rect_length} and width: {rect_width} is {area} ")


# Question 2


def calculate_average():
	"""
	Asks the user for 3 numbers and calculates the average
	Args:
	Returns:
		flaot: the average of the numbers

	"""
	num1 = float(input("Enter the first number: "))
	num2 = float(input("Enter the second number: "))
	num3 = float(input("Enter the third number: "))
	avg = (num1 + num2 + num3) / 3
	print(f"The average of numbers {num1} , {num2} and {num3} is {avg}")
	return avg


calculate_average()

point1 = (5, 8)
point2 = (58, 8)


def calculate_distance(x1, y1, x2, y2):
	"""
	calculates the distance between two points
	Args:
		x1(int): the x coordinate of the first point:
		y1(int): the y coordinate of the first:
		x2(int): the x coordinate of the second point:
		y2(int): the y coordinate of the second point:

	Returns:
		float: the distance between
	"""
	return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


closest_distance = calculate_distance(5, 8, 58, 8)  # ()

print(f"The distance is {closest_distance}")
