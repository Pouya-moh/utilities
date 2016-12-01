#include "QuinticPolynomial.hpp"
#include <iostream>
#include <stdlib.h>
#include <time.h>

int main() {
    srand (time(NULL));
    Eigen::VectorXd vi(2), vf(2);
//    QuinticPolynomial<double>::Vector vi(10), vf(10);
//    QuinticPolynomial<double>::Vector vi(10), vf(10);
    vi.setRandom();
    vf.setRandom();
    QuinticPolynomial<double> trj(0, 10, vi, vf);

//    std::cout<<trj.getQi()<<std::endl;//<< vi.transpose()<<std::endl<<vf.transpose()<<std::endl;

    for(double i=0; i<10; i+=0.01){
        std::cout<<trj.getQ(i).transpose()<<trj.getQd(i).transpose()<<trj.getQdd(i).transpose()<<std::endl;
    }
    return 0;
}
