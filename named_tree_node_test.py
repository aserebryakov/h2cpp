# Unit test for named_tree_node

from named_tree_node import NamedTreeNode

def test_run():
	passed = 0;
	failed = 0;

	root = NamedTreeNode("root", 0)
	child1 = NamedTreeNode("Child1", 1)
	
	try:
		root.addItem(child1)
		print("Adding Item Pass")
		passed = passed + 1
	except:
		print("Adding Item Fail")
		failed = failed + 1

	try:
		root.createItem("Child2")
		print("Creating Item Pass")
		passed = passed + 1
	except:
		print("Creating Item Fail")
		failed = failed + 1
	
	
	root.toString()
	
	try:
		root.addItem("Incorrect Item")
		print("Adding incorrect item fail")
		failed = failed + 1
	except TypeError:
		print ("Adding incorrect item pass")
		passed = passed + 1

	print("Passed {0} Failed {1} Total {2}").format(passed, failed, passed + failed)

	if failed > 0:
		return 1
	else:
		return 0

test_run()
