#!/usr/bin/python3

"""Square class
No modules were imported
"""


class Square:
	"""Defines blueprint of square
	Atrribute: size: integer indicating the size of square object
	"""

	def __init__(self, size=0):
		"""An object constructo method
		Arg: size: an integer representing the object size		"""
		self.__size = size

	@property
	def size(self):
		"""Gets the private soze attribute value
		Returns:
			The size private attribute
		"""
		return self.__size
	
	@size.setter
	def size(self, value):
		"sets the size private attribute value
		Vaalidates the assignment of the size private attribute
		arg:
			value : the value to be set
		"""
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		if value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value
	
	def area(self):
		"""public object method
		Returns:
			The current square area
		"""
		return self.__size**2

	def my_print(self):
		"""Displays the sqaure object with # character"""

		for x in range(self.size):
			for j in range(self.size):
				print('#', end="\n" if j is self.size -1 and x != j else "")
		print()
