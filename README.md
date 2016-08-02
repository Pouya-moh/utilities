# utilities
Tiny tools to help development. Each directory in this repo contains a single tool (or a collection of conceptually related tools).

## TOC
1. [csv-to-std-vector](./csv-to-std-vector) is a header only tool to parse and convert csv file to `std::vector<std::vector<double> >`.
2. [cpp-class-generator](./cpp-class-generator) is python script that creates an empty c++ class with header guards, empty constructor and etc.
3. [matlab-color-palette](./matlab-color-palette) contains matlab's new color palette. More on [mathworks website](http://www.mathworks.com/help/matlab/graphics_transition/why-are-plot-lines-different-colors.html).
4. [matlab-denavit-hartenberg](./matlab-denavit-hartenberg) single function that returns denavit hartenberg matrix, given (\alpha, a, d, \theta).
5. [cpp-snake-robot-generator](./cpp-snake-robot-generator) creates a c++ class with kinematics (EE pose and EE Jacobian) of a snake like robot with *n* spherical joints (in other words *dof = nx3*).

## TODO
1. Test [cpp-snake-robot-generator](./cpp-snake-robot-generator).
2. In [cpp-snake-robot-generator](./cpp-snake-robot-generator), get the info as command line arguments (currently are set from the script).