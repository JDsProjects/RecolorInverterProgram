#pragma once
#include <string>
#include <vector>
std::vector<std::string> split(std::string input, char letter) {
    std::vector<std::string> ret;
    std::string tmp = "";
    for (unsigned int i = 0; i < input.size(); i++) {
        if (input[i] == letter) {
            ret.push_back(tmp);
            tmp = "";
        }
        else {
            tmp += input[i];
        }
    }
    ret.push_back(tmp);
    return ret;
}