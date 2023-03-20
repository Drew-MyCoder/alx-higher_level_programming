#!/usr/bin/python3

"""Square Class
No modules were imported
"""


class Square:
	"""Defines the blueprint of square
	Attribute:
		size (int): an integer representing the object size
		position (int, int): the posistion of the new square
	"""

	def __init(self, size=0, psosition=(0, 0)):
		"""An object constructor method"""
		self.__size = size
		self.__position = position

	@property
	def size(self):
		"""gets the size private attribute value
		returns:
			the size private attribute
		"""
		return self.__size

	@size.setter
	def size(self, value):
		"""sets the size private attribute value
		validates the assignement of the private size attribute
		Arg:
			value:
				the value to be set
		"""
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		if value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	@property
	def position(self):
		"""Gets the position private attribute value
		returns:
			the position attribute
		"""
		return self.__position

	@position.setter
	def position(self, value):
		"""Sets the position private attribute value
		validates the assignment of the position private attribute
		Arg: value: the value to be set
		"""
		if (
			not isinstance(value, tuple)
			or len(value) != 2
			or not all(isinstance(num, int) for num in value)
			or not all(num >= 0 for num in value)
		):
			raise TypeError("position must be a tuple of 2 positive integers")
		self.__position = value

	def area(self):
		"""A public object method
		returns:
			the current sqaure area
		"""
		return self.__size**2

	def my_print(self):
		"""Displays the square object with # character"""
		if self.__size == 0:
			print("")
			return

		[print("") for x in range(0, self.__position[1])]
		for x in range(0, self.__size):
			[print(" ", end="") for j in range(0, self.__position[0])]
			[print("#", end="") for u in range(0, self.__size)]
			print("")