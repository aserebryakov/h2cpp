# This module contains main parsing logic

import re


def file_read(filename):
	input_file = open(filename, "r")
	content = input_file.read()
	input_file.close()
	return content

def get_namespaces(content):
	namespaces = []
	expr = re.compile("namespace\s+[a-zA-Z0-9_]+")
	ns_temp = expr.findall(content)
	for ns in ns_temp:
		ex = re.compile("namespace\s+")
		ns = ex.sub("", ns)
		namespaces.append(ns)
	return namespaces

def get_class(content):
	expr = re.compile("class\s+[a-zA-Z0-9_]+")
	class_name = expr.findall(content)
	class_name = re.compile("class\s+").sub("", class_name[0])
	return class_name

def get_methods(content):
	expr = re.compile("[\w\s_:]+\([^)]*\)") 
	methods = expr.findall(content)
	return methods

def get_arguments(method_decl):
	arguments_list = []
	arg_list_tmp = re.sub(r".*\(" ,"", method_decl)
	arg_list_tmp = re.sub(r"\).*" ,"", arg_list_tmp)
	arg_list_tmp = re.sub(r"\s?=\s?[0-9a-zA-Z_]+\s?", "", arg_list_tmp)
	arg_list_tmp = re.split(", ", arg_list_tmp)
	
	for arg in arg_list_tmp:
			arg = re.sub(r"^[^\s]+\s+", "", arg)
			arguments_list.append(arg)

	return arguments_list

def get_return_type(method_decl):
	print(method_decl)
	ret_type = re.sub(r"^\s*", "", method_decl)
	print(ret_type)
	ret_type = re.sub(r"\(.+", "", ret_type)
	print(ret_type)
	ret_type = re.sub(r"\s+.*", "", ret_type)

	return ret_type
