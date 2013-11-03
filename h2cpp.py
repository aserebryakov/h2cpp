# This file contains main() of the script

import sys
import cpp_generator

VERSION = "0.00"

def main(argv):
	print("h2cpp v" + VERSION);
	cpp_generator.generate_cpp(argv[0]);

main(sys.argv[1:])
