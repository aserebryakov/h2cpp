# This module contains cpp file generation implementation

import re
import doxycom
import cpp_parser
from outfile import OutFile

tab_level = 0


def tabbing(tab_level):
	tabs = ""
	for i in range(tab_level):
		tabs += "\t"
	return tabs


def write_method(outfile, method, class_name, tab_level):
	return_type = cpp_parser.get_return_type(method)
	args = cpp_parser.get_arguments(method)

	outfile.append(doxycom.doxy_gen_comment(args, return_type, tab_level))
	method = re.sub(r";", "", method)
	method = re.sub(return_type, "", method)
	method = re.sub(r"\s*", "", method, 1)
	method = class_name + "::" + method

	if(return_type != ""):
		method = " " + method

	method = tabbing(tab_level) + return_type + method

	method = method + "\n" + tabbing(tab_level) + "{\n"

	if(return_type != "void") and (return_type != ""):
		method = method + tabbing(tab_level + 1) + return_type + " result;\n"
		method = method + tabbing(tab_level + 1) + "return result;\n"

	method = method + tabbing(tab_level) + "}\n\n"

	outfile.append("\n" + method)


def generate_cpp(header_name):
	cpp_name = re.sub(r".(h|hpp)", ".cpp", header_name)
	outfile = OutFile(cpp_name)	

	header_content = cpp_parser.file_read(header_name)
	namespaces = cpp_parser.get_namespaces(header_content)
	class_name = cpp_parser.get_class(header_content)
	methods = cpp_parser.get_methods(header_content)

	tab_level = len(namespaces)

	outfile.append("#include \"" + header_name + "\"\n\n")

	for i in range(len(namespaces)):
		outfile.append(tabbing(i) +  "namespace " + namespaces[i] + "\n"+ tabbing(i) + "{\n")

	for method in methods:
		write_method(outfile ,method, class_name, tab_level)
	
	for i in range(tab_level, 0, -1):
		outfile.append(tabbing(i - 1) + "}\n")

