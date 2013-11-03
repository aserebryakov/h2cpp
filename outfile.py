# This module incapsulates operations with an output file

import sys


class OutFile:
	"""Output File class"""
	name = None
	descriptor = None

	def __init__(self, filename):
	"""Constructor"""
		self.name = filename
		try:
			self.descriptor = open(self.name, "w")
		except IOError as e:
			print("I/O error {0}: {1}".format(e.errno, e.strerror))
			sys.exit(1)

	def __del__(self):
	"""Destructor"""
		self.descriptor.close()
 	
	def append(self, string):
	"""Adds a string to the file"""
		self.descriptor.write(string)
