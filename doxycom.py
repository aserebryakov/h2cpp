# This module contains functions that are used for doxygen comments generation

doxy_header = "/**\n"
doxy_middle = "*"
doxy_footer = "*/\n"
doxy_param  = " @param "
doxy_return = " @return\n"


def doxy_tabbing(tab_level):
	tabs = ""
	for i in range(tab_level):
		tabs += "\t"
	return tabs

def doxy_gen_params(params, tab_level):
	params_string = ""
	
	for param in params:
		params_string = params_string + doxy_tabbing(tab_level) + doxy_middle + doxy_param + param + "\n"
	return params_string

def doxy_gen_comment(params, return_type, tab_level):
	doxy_comment = doxy_tabbing(tab_level) + doxy_header + doxy_gen_params(params, tab_level)
	
	if return_type == "void":
		doxy_comment = doxy_comment + doxy_tabbing(tab_level) + doxy_middle + doxy_return
	
	doxy_comment = doxy_comment + doxy_tabbing(tab_level) + doxy_footer

	return doxy_comment

