#ifndef CSVTOSTDVECTOR_H
#define CSVTOSTDVECTOR_H

#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <stdlib.h>

/**
    Author: Pouya Mohammadi
    Date:   28 June, 2016
    This is a simple method that converts a csv file to a vector of vector fo doubles
    It works byt it is not the best way, nor is the most elegant or efficient way.
*/

inline std::vector<std::vector<double> > parseCSVtoSTD(std::string path_to_file, char delimiter){
    std::vector<std::vector<double> > ret;
    std::ifstream input_file(path_to_file.c_str());
    std::string line;

    while (getline(input_file, line)) {
        std::stringstream linestream(line);
        std::string value;
        std::vector<double> single_row;
        int idx = 0;
        while (getline(linestream, value, delimiter)){
            double tmp = ::atof(value.c_str());
            single_row.push_back(tmp);
            idx++;
        }
        ret.push_back(single_row);
    }
    return ret;
}

#endif // CSVTOSTDVECTOR_H
