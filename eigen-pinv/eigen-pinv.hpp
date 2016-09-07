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

template<typename _Matrix_Type_>
_Matrix_Type_ pinv(const _Matrix_Type_ &a) {
    _Matrix_Type_ aT= a.transpose();
    _Matrix_Type_ aaT = a*aT;
    return aT*(aaT.inverse());
}

template<typename _Matrix_Type_>
inline _Matrix_Type_ Wpinv(const _Matrix_Type_ &a, const _Matrix_Type_ &w) {
    _Matrix_Type_ aT= a.transpose();
    _Matrix_Type_ aaT = a*w*aT;
    return w*aT*(aaT.inverse());
}


#endif /* EIGEN_PINV_HPP */
