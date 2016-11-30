/*
 * File:   QuinticPolynomial.hpp
 * Author: Pouya Mohammadi
 *
 * Created on Friday June 3, 2015, 11:57
 * This is based on quintic ploynomial presented in 
 * Prof. Allesandro de Luca's slides of robotics 1.
 */

#ifndef QUINTICPOLYNOMIAL_HPP
#define QUINTICPOLYNOMIAL_HPP


#include <eigen3/Eigen/Core>

template <class T>
class QuinticPolynomial
{
public:
    typedef Eigen::Matrix<T, Eigen::Dynamic, 1> Vector;
    double start_time;
    double end_time;
    double deltaT;            

    int dof;

    Vector q_i;
    Vector q_f;
    Vector delta_q;

    QuinticPolynomial();
    QuinticPolynomial(double start_time, double end_time, Vector init_conf, Vector final_conf);
    void setParams(double start_time, double end_time, Vector init_conf, Vector final_conf);
    Vector getQ(double time);
    Vector getQd(double time);
    Vector getQdd(double time);

    void setInitialConf(Vector init);
};

#endif // QUINTICPOLYNOMIAL_HPP
