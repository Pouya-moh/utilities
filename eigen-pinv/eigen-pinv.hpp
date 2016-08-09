/*
 * File:   eigen-pinv.hpp
 * Author: Pouya Mohammadi
 *
 * Created on Friday June 14, 2013, 12:29
 */


#ifndef EIGEN_PINV_HPP
#define EIGEN_PINV_HPP

#include <iostream>
#include "Eigen/Eigen/SVD"
#include "Eigen/Eigen/Core"
#include "Eigen/Eigen/Dense"
#include "constant_values.hpp"
#include <limits>

template<typename _Matrix_Type_>
_Matrix_Type_ pinv_SVD(const _Matrix_Type_ &a, double epsilon = std::numeric_limits<double>::epsilon()) {
    Eigen::JacobiSVD< _Matrix_Type_ > svd(a ,Eigen::ComputeThinU | Eigen::ComputeThinV);
    double tolerance = epsilon * std::max(a.cols(), a.rows()) *svd.singularValues().array().abs()(0);
    return svd.matrixV() *  (svd.singularValues().array().abs() > tolerance).select(svd.singularValues().array().inverse(), 0).matrix().asDiagonal() * svd.matrixU().adjoint();
}

inline Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> pinv2(const Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> &a) {
    Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> aT= a.transpose();
    Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> aaT = a*aT;
    return aT*(aaT.inverse());
}

inline Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> Wpinv(const Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> &a) {
    Eigen::MatrixXf W(ROBOT_DOF_SIZE,ROBOT_DOF_SIZE);
    W = Eigen::MatrixXf::Identity(ROBOT_DOF_SIZE,ROBOT_DOF_SIZE);
    for (int i = 6; i < 11; i++)
        W(i,i) = 3;

    Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> aT= a.transpose();
    Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> aaT = a*W*aT;
    return W*aT*(aaT.inverse());
}

#endif /* EIGEN_PINV_HPP */
