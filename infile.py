# This module incapsulates work with an input file
#
# InFile:
#   variables:
#   - descriptor
#   - content
#   - lines
#   methods:
#   - get_content
#   - get_lines

import sys


class InFile:
	"""InFile class"""
	descriptor = None
	content = None
	lines = []

	def __init__(self, filename):
		"""Constructor"""
		try:
			self.descriptor = open(filename, "r")
		except IOError as e:
			print("I/O error {0}: {1}".format(e.errno, e.strerror))
			raise IOError

		self.content = self.descriptor.read()
		self.lines = self.content.splitlines()
		self.descriptor.close()

	def get_content(self):
		"""Returns file content as one string"""
		return self.content

	def get_lines(self):
		"""Returns file content as a list of strings""" 
		return self.lines
