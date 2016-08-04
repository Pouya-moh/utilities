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

template<typename Scalar>
inline Eigen::Matrix<Scalar, Eigen::Dynamic, Eigen::Dynamic> pinv(const Eigen::Matrix<Scalar, Eigen::Dynamic, Eigen::Dynamic> &a, double epsilon = std::numeric_limits<Scalar>::epsilon()) {
    Eigen::Matrix<Scalar, Eigen::Dynamic, Eigen::Dynamic> result;
    if (a.rows() < a.cols()){
        Eigen::Matrix<Scalar, Eigen::Dynamic, Eigen::Dynamic> temp = a.transpose();
        result = pinv(temp);
        return result.transpose();
    }
    Eigen::JacobiSVD< Eigen::Matrix<Scalar, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor> > svd(a, ComputeThinU | ComputeThinV);
    Scalar tolerance = epsilon * std::max(a.cols(), a.rows()) * svd.singularValues().cwiseAbs().maxCoeff();
    result = svd.matrixV() * (svd.singularValues().array().abs() > tolerance).select(svd.singularValues().array().inverse(), 0).matrix().asDiagonal() * svd.matrixU().adjoint();
    return result;
}

inline Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic> pinv2(const Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic> &a) {
    Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic> aT= a.transpose();
    Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic> aaT = a*aT;
    return aT*(aaT.inverse());
}

inline Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic> Wpinv(const Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic> &a) {
    Eigen::MatrixXf W(ROBOT_DOF_SIZE,ROBOT_DOF_SIZE);
    W = Eigen::MatrixXf::Identity(ROBOT_DOF_SIZE,ROBOT_DOF_SIZE);
    for (int i = 6; i < 11; i++)
        W(i,i) = 3;

    Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic> aT= a.transpose();
    Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic> aaT = a*W*aT;
    return W*aT*(aaT.inverse());
}

#endif /* EIGEN_PINV_HPP */
