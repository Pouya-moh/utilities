#!/usr/bin/python

 
# Author:  Pouya Mohammadi
# Date:    June 30, 2016
# Description: This is a simple c++ class generator. It creates empty classes with header, source and minimum necessary content.
# TODO: Copy constructor
 

import sys
import os.path
import datetime

def writeRoll(idx):	
	return '\tA'+str(idx)+' << cos(th'+str(idx)+'),  0, -sin(th'+str(idx)+'), 0,\n\t\t  sin(th'+str(idx)+'),  0,  cos(th'+str(idx)+'), 0,\n\t\t         0, -1,         0, 0,\n\t\t         0,  0,         0, 1;\n\n'	

def writePitch(idx):
	return '\tA'+str(idx)+' << cos(th'+str(idx)+'), 0,  sin(th'+str(idx)+'), 0,\n\t\t  sin(th'+str(idx)+'), 0, -cos(th'+str(idx)+'), 0,\n\t\t         0, 1,         0, 0,\n\t\t         0, 0,         0, 1;\n\n'

def writeYaw(idx):
	return '\tA'+str(idx)+' << cos(th'+str(idx)+'), -sin(th'+str(idx)+'), 0,   0,\n\t\t  sin(th'+str(idx)+'),  cos(th'+str(idx)+'), 0,   0,\n\t\t         0,         0, 1,  d'+str(int(idx/3))+',\n\t\t         0,         0, 0,   1;\n\n'


def printMatrixes(dof):
	ret = ''

	for i in xrange(3,dof*3+1,3):
		ret = ret + '\tdouble d'+str(int(i/3))+' = 0.3;\n'

	ret = ret + '\n'
	for i in xrange(1,dof*3+1):
		ret = ret + '\tdouble th'+str(i)+' = configuration.at('+str(i)+');\n'

	ret = ret + '\n'
	for i in xrange(1,dof*3+1,3):
		ret = ret + writeRoll(i)
		ret = ret + writePitch(i+1)
		ret = ret + writeYaw(i+2)

	return ret

def printRotoTrans(dof):
	ret = '\tT1 = A1;\n'
	for i in xrange(2,dof*3+1):
		ret = ret + '\tT'+str(i)+' = T'+str(i-1)+'*A'+str(i)+';\n'

	return ret

def printJacobiran(dof):
	ret = '\n\tupdateConfiguration(configuration);\n\n'
	ret = ret + '\tz0  << 0, 0, 1;\n'
	ret = ret + '\tp0  << 0, 0, 0;\n'
	ret = ret + '\tpEE = T'+str(dof*3)+'.block<3,1>(0,3);\n\n'
	for i in xrange(1,dof*3+1):
		ret = ret + '\tJac.block<3,1>(0,'+str(i-1)+') = (T'+str(i-1)+'.block<3,1>(0,2)).cross(pEE-(T'+str(i-1)+'.block<3,1>(0,3)));\n'

	ret = ret + '\n'

	for i in xrange(1,dof*3+1):
		ret = ret + '\tJac.block<3,1>(3,'+str(i-1)+') = (T'+str(i-1)+'.block<3,1>(0,2));\n'

	return ret

def printMatrixDeclarations(dof):
	ret = '\tEigen::Vector3d z0, p0;\n\n'
	for i in xrange(1,dof*3+1):
		ret = ret + '\tRotoTranslationMatrix A'+str(i)+'\n'
	
	ret = ret + '\n'

	for i in xrange(1,dof*3+1):
		ret = ret + '\tRotoTranslationMatrix T'+str(i)+'\n'

	ret = ret + '\n\n'
	return ret

def createClass(className, dof_size):
	source = open(className+'.cpp', 'w+')
	header = open(className+'.hpp', 'w+')
	today  = datetime.datetime.now()
	# ----------------header----------------
	# credits
	header.write('/*\n * Author:  Pouya Mohammadi\n * Date:    '+today.strftime("%B")+' '+str(today.day)+', '+str(today.year)+'\n * License: \n * Description: \n * \n */\n\n')
	# include guard:
	header.write('#ifndef '+className.upper()+'_HPP\n#define '+className.upper()+'_HPP\n\n')
	# includes:
	header.write('#include <vector>\n#include <Eigen/Core>\n\n')
	header.write('typedef Eigen::Matrix<double, 4, 4> RotoTranslationMatrix;\n\n')

	# class declaration and stuff:
	header.write('class '+className+' {\npublic:\n\t'+className+'();\n\t'+className+'(const '+className+'& orig);\n\tvirtual ~'+className+'();\n\n')
	# methods:
	header.write('\t//consider using return statement\n\tvoid getEEPose(std::vector<double> & configuration, RotoTranslationMatrix & ee_pose);\n\tvoid getJacobian(std::vector<double> & configuration, Eigen::MatrixXd & Jac);\n\n')
	header.write('\tvoid updateConfiguration(std::vector<double> & configuration);\n\n')
	header.write('private:\n')
	header.write(printMatrixDeclarations(dof_size))

	header.write('protected:\n\n};\n')
	# endof guard
	header.write('#endif // '+className.upper()+'_HPP\n')
	# ----------------source----------------
	source.write('/*\n * Author:  Pouya Mohammadi\n * Date:    '+today.strftime("%B")+' '+str(today.day)+', '+str(today.year)+'\n * License: \n * Description: \n * \n */\n\n')
	source.write('#include \"'+className+'.hpp\"\n\n')
	source.write(className+'::'+className+'() {\n\t\n}\n\n')
	source.write(className+'::'+className+'(const '+className+'& orig) {\n\t\n}\n\n')
	source.write(className+'::~'+className+'() {\n\t\n}\n\n')
	source.write('void '+className+'::'+'updateConfiguration(std::vector<double> & configuration) {\n')
	source.write('\n'+printMatrixes(dof_size)+'\n'+printRotoTrans(dof_size)+'}\n\n')
	source.write('void '+className+'::'+'getJacobian(std::vector<double> & configuration, Eigen::MatrixXd & Jac) {\n'+printJacobiran(dof_size)+'}\n\n')
	source.write('void '+className+'::'+'getEEPose(std::vector<double> & configuration, RotoTranslationMatrix & ee_pose) { \n\n\tupdateConfiguration(configuration);\n\treturn this->T'+str(dof_size*3)+';\n}')
#============================================================

if len(sys.argv)!=2:
	print "Usage: Pass number of spherical joints as input argument.\nE.g., ./class-generator-extended.py 3"
	sys.exit()
else:
	# if os.path.isfile(sys.argv[1]+'.cpp'):
	# 	print sys.argv[1]+".cpp already exists"
	# 	sys.exit()
	# elif os.path.isfile(sys.argv[1]+'.hpp'):
	# 	print sys.argv[1]+".hpp already exists"
	# else:
	# 	createClass(sys.argv[1])
	createClass('SnakeLike_'+str(int(sys.argv[1])*3)+'_DOF', int(sys.argv[1]))
