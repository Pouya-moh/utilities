#!/usr/bin/python

 
# Author:  Pouya Mohammadi
# Date:    Jac 30, 2017
# Description: This is simple script that creates a cpp cmake project
# TODO: Copy constructor
 

import sys
import os
import datetime

def populateMain(main_file):
	main_file.write("#include <iostream>\n\nint main() {\n")
	main_file.write("\tstd::cout<<\"Hello world!\"<<std::endl;\n\treturn 0;\n}")

def populateCMake(projectName, cmake_file):
	cmake_file.write("cmake_minimum_required(VERSION 2.8)\n\n")
	cmake_file.write("project("+projectName+")\n\n")
	cmake_file.write("## Example find_package because I'm lazy\n")
	cmake_file.write("# find_package(samplePkg REQUIRED)\n# IF (samplePkg_FOUND)\n# \tmessage(STATUS \"samplePkg found. Version: ${samplePkg_VERSION}\")\n# \tinclude_directories(BEFORE SYSTEM ${samplePkg_INCLUDE_DIRS})\n# \tadd_definitions(${samplePkg_CFLAGS})\n# \tlink_directories(${samplePkg_LIBRARY_DIR})\n# ENDIF()\n\n")
	cmake_file.write("file(GLOB SOURCES ${PROJECT_SOURCE_DIR}/src/*.cpp)\n")	
	cmake_file.write("include_directories(${PROJECT_SOURCE_DIR}/include)\n\n")	
	cmake_file.write("add_executable(${CMAKE_PROJECT_NAME} ${SOURCES})\n\n")
	cmake_file.write("# add_library(${CMAKE_PROJECT_NAME} ${SOURCES})\n\n")
	cmake_file.write("target_link_libraries(${CMAKE_PROJECT_NAME} ${samplePkg_LIBRARIES})")
def createCppProject(projectName):
	
	try:
		os.mkdir("src")
		os.mkdir("include")
		os.mkdir("build")
		cmake = open('CMakeLists.txt', 'w+')
		filepath = os.path.join('./src', 'main.cpp')		
		main = open(filepath, 'w+')

		populateCMake(projectName, cmake)
		populateMain(main)
	except:
		print("Some files or directories already existing.")
		sys.exit()
	# header = open(className+'.hpp', 'w+')
	# today  = datetime.datetime.now()
	# # ----------------header----------------
	# # credits
	# header.write('/*\n * Author:  Pouya Mohammadi\n * Date:    '+today.strftime("%B")+' '+str(today.day)+', '+str(today.year)+'\n * License: \n * Description: \n * \n */\n\n')
	# # include guard:
	# header.write('#ifndef '+className.upper()+'_HPP\n#define '+className.upper()+'_HPP\n\n')
	# # class declaration and stuff:
	# header.write('class '+className+' {\npublic:\n\t'+className+'();\n\t'+className+'(const '+className+'& orig);\n\tvirtual ~'+className+'();\n\nprivate:\n\nprotected:\n\n};\n')
	# # endof guard
	# header.write('#endif // '+className.upper()+'_HPP\n')
	# # ----------------source----------------
	# source.write('/*\n * Author:  Pouya Mohammadi\n * Date:    '+today.strftime("%B")+' '+str(today.day)+', '+str(today.year)+'\n * License: \n * Description: \n * \n */\n\n')
	# source.write('#include \"'+className+'.hpp\"\n\n')
	# source.write(className+'::'+className+'() {\n\t\n}\n\n')
	# source.write(className+'::'+className+'(const '+className+'& orig) {\n\t\n}\n\n')
	# source.write(className+'::~'+className+'() {\n\t\n}\n')

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
		createCppProject(sys.argv[1])
