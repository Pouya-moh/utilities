/*
 * File:   QuinticPolynomial.cpp
 * Author: Pouya Mohammadi
 *
 * Created on Friday June 3, 2015, 11:57
 * This is based on quintic ploynomial presented in 
 * Prof. Allesandro de Luca's slides of robotics 1.
 */

#include "QuinticPolynomial.hpp"
#include <cmath>
QuinticPolynomial::QuinticPolynomial() {
}

QuinticPolynomial::QuinticPolynomial(double start_time, double end_time, QuinticPolynomial::Vector init_conf, QuinticPolynomial::Vector final_conf){
    this->start_time = start_time;
    this->end_time   = end_time;
    this->deltaT = end_time-start_time;
    this->q_i = init_conf;
    this->q_f = final_conf;
    this->delta_q = q_f - q_i;
    this->dof = q_i.rows();
}

void QuinticPolynomial::setParams(double start_time, double end_time, QuinticPolynomial::Vector init_conf, QuinticPolynomial::Vector final_conf) {
    this->start_time = start_time;
    this->end_time   = end_time;
    this->deltaT = end_time-start_time;
    this->q_i = init_conf;
    this->q_f = final_conf;
    this->delta_q = q_f - q_i;
    this->dof = q_i.rows();
}

QuinticPolynomial::Vector QuinticPolynomial::getQ(double time){
    Vector ret(dof);
    if (time >= end_time)
        time = end_time;

    double tau = (time-start_time)/(deltaT);
    for (int i=0; i<dof; ++i){
        ret(i) = q_i(i) + delta_q(i)*(6*std::pow(tau,5.0)-15*std::pow(tau,4.0)+10*std::pow(tau,3.0));
    }
    return ret;
}

QuinticPolynomial::Vector QuinticPolynomial::getQd(double time){
    QuinticPolynomial::Vector ret(dof);
    if (time >= end_time)
        time = end_time;

    double tau = (time-start_time)/(deltaT);
    for (int i=0; i<dof; ++i){
        ret(i) = delta_q(i)*(30*std::pow(tau,4.0)-60*std::pow(tau,3.0)+30*std::pow(tau,2.0));
    }

    return ret;
}

QuinticPolynomial::Vector QuinticPolynomial::getQdd(double time){
    QuinticPolynomial::Vector ret(dof);
    if (time >= end_time)
        time = end_time;

    double tau = (time-start_time)/(deltaT);
    for (int i=0; i<dof; ++i){
        ret(i) = delta_q(i)*(120*std::pow(tau,3.0)-180*std::pow(tau,2.0)+60*tau);
    }

    return ret;
}

void QuinticPolynomial::setInitialConf(QuinticPolynomial::Vector init){
    this->q_i = init;
    this->delta_q = q_f - q_i;
}
