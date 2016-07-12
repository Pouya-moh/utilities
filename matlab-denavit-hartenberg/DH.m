function T = DH(al,a,d,th)
% DH calculates homogeneous transformation matrix/DH matrix
% 
%	DH(al,a,d,th)
% 	IMPORTANT NOTE! al is in degrees. I know, I know!! degrees are bad
% 	but in this case I chose it intentionally so that when alpha is 90
% 	or 0 degrees it simple out to 0 or 1 and simplifies the resulting
% 	matrix that is very important for symbolic expressions.
% 	Since most of the times alpha is indeed 0 or 90 I keep it this way
% 
% 	Example:
% 	DH(90, 0, 0.1, theta1)
% 	note that all of the parameters can be symbolic
% 
% 	TODO: add option for accepting an option specifying unit of alpha
% 
% 	Author: Pouya Mohammadi
  
	T=[cos(th)  -cosd(al)*sin(th)  sind(al)*sin(th)   a*cos(th);
	   sin(th)  cosd(al)*cos(th)   -sind(al)*cos(th)  a*sin(th);
	   0        sind(al)           cosd(al)           d;
	   0        0                  0                  1];
end