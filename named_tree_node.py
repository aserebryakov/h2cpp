# This module implements a named tree node concept
#
# NamedTreeNode:
#   variables:
#     - name
#     - depth
#     - items
#   methods:
#     - addItem
#     - createItem
#     - getItems
#     - getName
#     - getDepth
#     - toString
#


class NamedTreeNode:
	"""NamedTreeNode class"""
	name = None
	depth = 0
	items = []

	def __init__(self, name, depth):
		"""Constructor"""
		self.name = name
		self.depth = depth
		self.items = []

	def addItem(self, item):
		"""Adds an item to list of items"""
		if isinstance(item, NamedTreeNode):
			self.items.append(item)
		else:
			raise TypeError

	def createItem(self, name):
		"""Creates a new item list of ites"""
		if name != "":
			newItem = NamedTreeNode(name, self.depth + 1)
			self.addItem(newItem)

	def getItems(self):
		"""Returns a list of items"""
		return self.items

	def getName(self):
		"""Returns a name of the node"""
		return self.name

	def getDepth(self):
		"""Returns a depth value"""
		return self.depth

	def toString(self):
		"""Prints name, depth and list of items"""
		print("Name = " + self.name)
		print("Depth = {0}").format(self.depth)
		for item in self.items:
			item.toString() 

