#!/usr/bin/python

 
# Author:  Pouya Mohammadi
# Date:    June 30, 2016
# Description: This is a simple c++ class generator. It creates empty classes with header, source and minimum necessary content.
# TODO: Copy constructor
 

import sys
import os.path
import datetime

radius = 0.01
length = 0.05
dof    = 20

def writeHeader():	
	ret = '<!-- Created by Pouya Mohammadi -->\n<robot name=\"robot\">\n\t<link name=\"world\"/>\n\n\t<joint name=\"fixed\" type=\"fixed\">\n\t\t<parent link=\"world\"/>\n\t\t<child link=\"base_link\"/>\n\t</joint>\n\n\t<link name=\"base_link\">\n\t\t<origin xyz=\"0 0 '+str(length/2)+'\" rpy=\"0 0 0\"/>\n\t\t<collision>\n\t\t\t<geometry>\n\t\t\t\t<cylinder length=\"'+str(length)+'\" radius=\"'+str(radius)+'\"/>\n\t\t\t</geometry>\n\t\t</collision>\n\t\t<visual>\n\t\t\t<geometry>\n\t\t\t\t<cylinder length=\"'+str(length)+'\" radius=\"'+str(radius)+'\"/>\n\t\t\t</geometry>\n\t\t</visual>\n\t</link>\n'
	ret = ret + '\t<joint name=\"joint_1\" type=\"revolute\">\n\t\t<limit effort=\"1000.0\" lower=\"-1.57075\" upper=\"1.57075\" velocity=\"1\"/>\n\t\t<parent link=\"base_link\"/>\n\t\t<child link=\"link_2\"/>\n\t\t<origin xyz=\"0 0 '+str(length/2)+'\"/>\n\t\t<axis xyz=\"0 1 0\"/>\n\t</joint>\n\n\t<link name=\"link_2\">\n\t\t<origin xyz=\"0 0 '+str(length/2)+'\" rpy=\"0 0 0\"/>\n\t\t<collision>\n\t\t\t<origin xyz=\"0 0 '+str(length/2)+'\"/>\n\t\t\t<geometry>\n\t\t\t\t<cylinder length=\"'+str(length)+'\" radius=\"'+str(radius)+'\"/>\n\t\t\t</geometry>\n\t\t</collision>\n\t\t<visual>\n\t\t\t<origin xyz=\"0 0 '+str(length/2)+'\"/>\n\t\t\t<geometry>\n\t\t\t\t<cylinder length=\"'+str(length)+'\" radius=\"'+str(radius)+'\"/>\n\t\t\t</geometry>\n\t\t</visual>\n\t</link>\n'
	return ret

def writeEndEffector(idx):
	if (idx % 2 == 0):
		ret = '\t<joint name=\"joint_'+str(idx)+'\" type=\"revolute\">\n\t\t<limit effort=\"1000.0\" lower=\"-1.57075\" upper=\"1.57075\" velocity=\"1\"/>\n\t\t<parent link=\"link_'+str(idx)+'\"/>\n\t\t<child link=\"link_EE\"/>\n\t\t<origin xyz=\"0 0 '+str(length)+'"/>\n\t\t<axis xyz=\"1 0 0\"/>\n\t</joint>\n\n\t<link name=\"link_EE\">\n\t\t<origin xyz=\"0 0 '+str(length/2)+'\" rpy=\"0 0 0\"/>\n\t\t<collision>\n\t\t\t<origin xyz=\"0 0 '+str(length/2)+'\"/>\n\t\t\t<geometry>\n\t\t\t\t<cylinder length=\"'+str(length)+'\" radius=\"'+str(radius)+'\"/>\n\t\t\t</geometry>\n\t\t</collision>\n\t\t<visual>\n\t\t\t<origin xyz=\"0 0 '+str(length/2)+'\"/>\n\t\t\t<geometry>\n\t\t\t\t<cylinder length=\"'+str(length)+'\" radius=\"'+str(radius)+'\"/>\n\t\t\t</geometry>\n\t\t</visual>\n\t</link>\n</robot>'
	else:
		ret = '\t<joint name=\"joint_'+str(idx)+'\" type=\"revolute\">\n\t\t<limit effort=\"1000.0\" lower=\"-1.57075\" upper=\"1.57075\" velocity=\"1\"/>\n\t\t<parent link=\"link_'+str(idx)+'\"/>\n\t\t<child link=\"link_EE\"/>\n\t\t<origin xyz=\"0 0 '+str(length)+'"/>\n\t\t<axis xyz=\"0 1 0\"/>\n\t</joint>\n\n\t<link name=\"link_EE\">\n\t\t<origin xyz=\"0 0 '+str(length/2)+'\" rpy=\"0 0 0\"/>\n\t\t<collision>\n\t\t\t<origin xyz=\"0 0 '+str(length/2)+'\"/>\n\t\t\t<geometry>\n\t\t\t\t<cylinder length=\"'+str(length)+'\" radius=\"'+str(radius)+'\"/>\n\t\t\t</geometry>\n\t\t</collision>\n\t\t<visual>\n\t\t\t<origin xyz=\"0 0 '+str(length/2)+'\"/>\n\t\t\t<geometry>\n\t\t\t\t<cylinder length=\"'+str(length)+'\" radius=\"'+str(radius)+'\"/>\n\t\t\t</geometry>\n\t\t</visual>\n\t</link>\n</robot>'
	return ret


def writeJointLink(idx):
	if (idx % 2 == 0):
		ret = '\t<joint name=\"joint_'+str(idx)+'\" type=\"revolute\">\n\t\t<limit effort=\"1000.0\" lower=\"-1.57075\" upper=\"1.57075\" velocity=\"1\"/>\n\t\t<parent link=\"link_'+str(idx)+'\"/>\n\t\t<child link=\"link_'+str(idx+1)+'\"/>\n\t\t<origin xyz=\"0 0 '+str(length)+'"/>\n\t\t<axis xyz=\"1 0 0\"/>\n\t</joint>\n\n\t<link name=\"link_'+str(idx+1)+'\">\n\t\t<origin xyz=\"0 0 '+str(length/2)+'\" rpy=\"0 0 0\"/>\n\t\t<collision>\n\t\t\t<origin xyz=\"0 0 '+str(length/2)+'\"/>\n\t\t\t<geometry>\n\t\t\t\t<cylinder length=\"'+str(length)+'\" radius=\"'+str(radius)+'\"/>\n\t\t\t</geometry>\n\t\t</collision>\n\t\t<visual>\n\t\t\t<origin xyz=\"0 0 '+str(length/2)+'\"/>\n\t\t\t<geometry>\n\t\t\t\t<cylinder length=\"'+str(length)+'\" radius=\"'+str(radius)+'\"/>\n\t\t\t</geometry>\n\t\t</visual>\n\t</link>'
	else:
		ret = '\t<joint name=\"joint_'+str(idx)+'\" type=\"revolute\">\n\t\t<limit effort=\"1000.0\" lower=\"-1.57075\" upper=\"1.57075\" velocity=\"1\"/>\n\t\t<parent link=\"link_'+str(idx)+'\"/>\n\t\t<child link=\"link_'+str(idx+1)+'\"/>\n\t\t<origin xyz=\"0 0 '+str(length)+'"/>\n\t\t<axis xyz=\"0 1 0\"/>\n\t</joint>\n\n\t<link name=\"link_'+str(idx+1)+'\">\n\t\t<origin xyz=\"0 0 '+str(length/2)+'\" rpy=\"0 0 0\"/>\n\t\t<collision>\n\t\t\t<origin xyz=\"0 0 '+str(length/2)+'\"/>\n\t\t\t<geometry>\n\t\t\t\t<cylinder length=\"'+str(length)+'\" radius=\"'+str(radius)+'\"/>\n\t\t\t</geometry>\n\t\t</collision>\n\t\t<visual>\n\t\t\t<origin xyz=\"0 0 '+str(length/2)+'\"/>\n\t\t\t<geometry>\n\t\t\t\t<cylinder length=\"'+str(length)+'\" radius=\"'+str(radius)+'\"/>\n\t\t\t</geometry>\n\t\t</visual>\n\t</link>'
	return ret


# print writeHeader()
# print writeJointLink(2)
# print writeJointLink(3)
# print writeEndEffector(4)

print writeHeader()
for i in xrange(2,dof):
	print writeJointLink(i)

print writeEndEffector(dof)
# if len(sys.argv)!=2:
# 	print "Usage: Pass number of spherical joints as input argument.\nE.g., ./class-generator-extended.py 3"
# 	sys.exit()
# else:
# 	# if os.path.isfile(sys.argv[1]+'.cpp'):
# 	# 	print sys.argv[1]+".cpp already exists"
# 	# 	sys.exit()
# 	# elif os.path.isfile(sys.argv[1]+'.hpp'):
# 	# 	print sys.argv[1]+".hpp already exists"
# 	# else:
# 	# 	createClass(sys.argv[1])
# 	createClass('SnakeLike_'+str(int(sys.argv[1])*3)+'_DOF', int(sys.argv[1]))
