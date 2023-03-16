#!/usr/bin/python3

"""Square Class
no modules were imported
"""

class Square:
	"""Defines the square
	Private instance size: integer indicating the size of sqaure object""""

	def __init__(self, size=0):
		"""An object constructor method
		Arg: size: has default value of 0.
		Raises:
			TypeError: if size is not an integer
			ValueError: if size < 0
		"""
		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		if size < 0:
			raise ValueError("size must be >= 0")
		self.__size = size
