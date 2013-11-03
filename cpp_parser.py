# This module contains main parsing logic

import re


def find_all(array, regex):
	matches = []

	print(array)
	for string in array:
		if regex.search(string) != None:
			matches.append(string)

	print(matches)
	return matches


def file_read(filename):
	input_file = open(filename, "r")
	content = input_file.read()
	input_file.close()
	return content.splitlines()


def get_namespaces(content):
	namespaces = []
	ns_temp = []
	expr = re.compile("namespace\s+[a-zA-Z0-9_]+")
	ns_temp = find_all(content, expr)
	for ns in ns_temp:
		ex = re.compile("\s*namespace\s+")
		ns = ex.sub("", ns)
		namespaces.append(ns)

	print(namespaces)
	return namespaces


def get_class(content):
	expr = re.compile("class\s+[a-zA-Z0-9_]+")
	class_name = find_all(content, expr)
	class_name = re.compile("\s*class\s+").sub("", class_name[0])
	return class_name


def get_methods(content):
	methods = []
	expr = re.compile("[\w\s_:]+\([^)]*\)") 
	methods_tmp = find_all(content, expr)

	for method in methods_tmp:
		method = re.sub(r"\s+", "", method, 1)
		print(method)
		methods.append(method)

	print("Methods\n")
	print(methods)

	return methods


def get_arguments(method_decl):
	arguments_list = []
	arg_list_tmp = re.sub(r".*\(" ,"", method_decl)
	arg_list_tmp = re.sub(r"\).*" ,"", arg_list_tmp)
	arg_list_tmp = re.sub(r"\s?=\s?[0-9a-zA-Z_]+\s?", "", arg_list_tmp)
	arg_list_tmp = re.split(", ", arg_list_tmp)
	
	for arg in arg_list_tmp:
		arg = re.sub(r"^[^\s]+\s+", "", arg)
		if arg != "":
			arguments_list.append(arg)

	return arguments_list


def get_return_type(method_decl):
	ret_type = re.sub(r"^\s*", "", method_decl)
	
	# ret_type_1 and ret_type_2 are introduced to handle the case of the constructor

	ret_type_1 = re.sub(r"\(.+", "", ret_type)
	ret_type_2 = re.sub(r"\s+.*", "", ret_type_1)

	if(ret_type_1 == ret_type_2):
		ret_type = ""
	else:
		ret_type = ret_type_2

	return ret_type

