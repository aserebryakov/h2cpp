# The InFile class unit test

import sys
from infile import InFile

testfile_name = "testfile.txt"
testfile_text = "This is a\ntest file"


def precondition(filename):
	descriptor = open(filename, "w")
	descriptor.write(testfile_text)
	descriptor.close()

def test_run():
	failed = 0
	passed = 0
	infile = None
	precondition(testfile_name)
	
	print("Incorrect file name passing : ")
	try:
		infile = InFile("incorrect_name.txt")
		failed = failed + 1
		print("FAIL")
	except IOError:
		passed = passed + 1
		print("PASS")


	print("File opening : ")
	try:
		infile = InFile(testfile_name)
		passed = passed + 1
		print("PASS")
	except IOError:
		failed = failed + 1
		print("FAIL")

	print("File content : ")
	if(infile.get_content() == testfile_text):
		passed = passed + 1
		print("PASS")
	else:
		failed = failed + 1
		print("FAIL")

	print("File lines : ")
	
	test_lines = testfile_text.splitlines()
	infile_lines = infile.get_lines()
	result = 1

	for i in range(len(test_lines)):
		if(test_lines[i] != infile_lines[i]):
			result = 0
			print("test line : {0}\n infile line {1}").format(test_lines[i], infile_lines[i])
			break

	if(result == 0):
		print("FAIL")
		failed = failed + 1
	else:
		print("PASS")
		passed = passed + 1

	print("Failed: {0} Passed {1} Total {2}").format(failed, passed, failed + passed)
	
test_run()
