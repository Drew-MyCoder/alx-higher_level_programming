#!/usr/bin/python3

"""Square Class
No modules were imported
"""


class Square:
	"""Defines blueprint for square
	Attribute: Size: an integer indicating size square object
	"""


	def __init__(self, size=0):
		"""An object constructor method
		Initializes squarecsize
		Arg: size: has default value of 0
		"""
		self.__size = size

	@property
	def size(self):
		"""Gets the private size atrribute value
		Returns:
			the size private attribute
		"""
		return self.__size
