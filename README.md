# utilities
Tiny tools to help development. Each directory in this repo contains a single tool (or a collection of conceptually related tools).

## TOC
1. [csv-to-std-vector](./csv-to-std-vector) is a header only tool to parse and convert csv file to `std::vector<std::vector<double> >`.
2. [cpp-class-generator](./cpp-class-generator) is python script that creates an empty c++ class with header guards, empty constructor and etc.
3. [matlab-color-palette](./matlab-color-palette) contains matlab's new color palette. More on [mathworks website](http://www.mathworks.com/help/matlab/graphics_transition/why-are-plot-lines-different-colors.html).
4. [matlab-denavit-hartenberg](./matlab-denavit-hartenberg) single function that returns denavit hartenberg matrix, given (\alpha, a, d, \theta).
5. [cpp-snake-robot-generator](./cpp-snake-robot-generator) creates a c++ class with kinematics (EE pose and EE Jacobian) of a snake like robot with *n* spherical joints (in other words *dof = nx3*).
6. [eigen-pinv](./eigen-pinv) is a header with methods for calculation of pseudo-inverse with Eigen library. One method is taken from Eigen mailing list or their Wiki. Currently it contains:
    1. `pinv` (SVD based, slower)
    2. `pinv2` (right pseudo-inverse, faster but unstable near singularity)
    3. `Wpinv` (Weighted pseudo-inverse)
7. [quintic-polynomial](./quintic-polynomial) single header, templated cpp class to generate 'q, qd, qdd', given that initial and final velocities and accelerations are zero.
8. [gazebo-dummy-model](./gazebo-dummy-model) helper/simple gazebo object that does not interact/collide with  environment. Inspired by v-rep dummy object.
9. [cpp-project-generator](./cpp-project-generator) creates simple c++ proejct with src, include, build and CMakeLists.txt. It does globbing in cmake so be careful!
10. [component-generator](./component-generator) creates an empty c++/orocos component
## TODO
* Test [cpp-snake-robot-generator](./cpp-snake-robot-generator).
* In [cpp-snake-robot-generator](./cpp-snake-robot-generator), get the info as command line arguments (currently are set from the script).
* In [eigen-pinv](./eigen-pinv):
    1. Fix includes
    2. Test new templated version
* Add documentation to [quintic-polynomial](./quintic-polynomial).
* [component-generator](./component-generator) needs to be tested. 
* [component-generator](./component-generator) can have a template of a port 
