#!/usr/bin/python

 
# Author:  Pouya Mohammadi
# Date:    June 30, 2016
# Description: This is a simple c++ class generator. It creates empty classes with header, source and minimum necessary content.
# TODO: Copy constructor
 

import sys
import os.path
import datetime

def createClass(className):
	source = open(className+'.cpp', 'w+')
	header = open(className+'.hpp', 'w+')
	today  = datetime.datetime.now()
	# ----------------header----------------
	# credits
	header.write('/*\n * Author:  Pouya Mohammadi\n * Date:    '+today.strftime("%B")+' '+str(today.day)+', '+str(today.year)+'\n * License: \n * Description: \n * \n */\n\n')
	# include guard:
	header.write('#ifndef '+className.upper()+'_HPP\n#define '+className.upper()+'_HPP\n\n#include <rtt/RTT.hpp>\n\n')
	# class declaration and stuff:
	header.write('class '+className+': public RTT::TaskContext {\npublic:\n\t'+className+'(std::string const & name);\n\n')
	header.write('\tbool configureHook();\n\tbool startHook();\n\tvoid updateHook();\n\tvoid stopHook();\n\tvoid cleanupHook();\n\nprivate:\n\nprotected:\n\n};\n')
	# endof guard
	header.write('#endif // '+className.upper()+'_HPP\n')
	# ----------------source----------------
	source.write('/*\n * Author:  Pouya Mohammadi\n * Date:    '+today.strftime("%B")+' '+str(today.day)+', '+str(today.year)+'\n * License: \n * Description: \n * \n */\n\n')
	source.write('#include \"'+className+'.hpp\"\n#include <rtt/Component.hpp>\n\n')
	source.write(className+'::'+className+'(std::string const & name) : RTT::TaskContext(name) {\n\t\n}\n\n')
	source.write('bool '+className+'::configureHook() {\n\n\treturn true;\n}\n\n')
	source.write('bool '+className+'::startHook() {\n\n\treturn true;\n}\n\n')
	source.write('void '+className+'::updateHook() {\n\n}\n\n')
	source.write('void '+className+'::stopHook() {\n\n}\n\n')
	source.write('void '+className+'::cleanupHook() {\n\n}\n\n')
	source.write('ORO_CREATE_COMPONENT_LIBRARY()ORO_LIST_COMPONENT_TYPE('+className+')')

if len(sys.argv)!=2:
	print "Usage: Pass class name as command line argument. E.g., ./class-generator.py FooBar"
	sys.exit()
else:
	if os.path.isfile(sys.argv[1]+'.cpp'):
		print sys.argv[1]+".cpp already exists"
		sys.exit()
	elif os.path.isfile(sys.argv[1]+'.hpp'):
		print sys.argv[1]+".hpp already exists"
	else:
		createClass(sys.argv[1])
