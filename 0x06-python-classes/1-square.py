#!/usr/bin/python3

"""Square class
No modules were imported
Square = __import__('1-square').Square
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)
"""

class Square:
	"""Defines the square.
	private instance size:
		An integer indicating the size of the square object.
"""

	def __init__(self, size):
		"""An object constructor method
		Arg: size: an integer representing object size
		"""
		self.__size = size
