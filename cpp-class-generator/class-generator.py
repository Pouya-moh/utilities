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
	header.write('#ifndef '+className.upper()+'_HPP\n#define '+className.upper()+'_HPP\n\n')
	# class declaration and stuff:
	header.write('class '+className+' {\npublic:\t'+className+'();\n\t'+className+'(const '+className+'& orig);\n\tvirtual ~'+className+'();\n\nprivate:\n\nprotected:\n\n};\n')
	# endof guard
	header.write('#endif // '+className.upper()+'_HPP\n')
	# ----------------source----------------
	source.write('/*\n * Author:  Pouya Mohammadi\n * Date:    '+today.strftime("%B")+' '+str(today.day)+', '+str(today.year)+'\n * License: \n * Description: \n * \n */\n\n')
	source.write('#include \"'+className+'.hpp\"\n\n')
	source.write(className+'::'+className+'() {\n\t\n}\n\n')
	source.write(className+'::'+className+'(const '+className+'& orig) {\n\t\n}\n\n')
	source.write(className+'::~'+className+'() {\n\t\n}\n')

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
