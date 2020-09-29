#pragma once
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include "./Split.h"
std::vector<std::string> LoadFile(std::string &FilePath){
	std::vector<std::string> ret;
	std::fstream file(FilePath,std::ios::in);
	std::string tmp = "";
	do  {
		getline(file,tmp);
		ret.push_back(tmp);
	} while (!(file.eof()));

	file.close();
	return  ret;
}