#pragma once
#include <sstream>
#include <iostream>
#include "color.h"
#include "../Split.h"
using namespace std;
struct bodyPart {
    std::string baseAdress[2];
    color partColor;
    bodyPart(string code1, string code2) {
        std::string code1RRGG = split(code1, ' ')[1];
        std::string code2BBAA = split(code2, ' ')[1];
        char RR[2] = { code1RRGG[0],code1RRGG[1] };
        char GG[2] = { code1RRGG[2],code1RRGG[3] };
        char BB[2] = { code2BBAA[0],code2BBAA[1] };
        char AA[2] = { code2BBAA[2], code2BBAA[3] };
        partColor.r = std::stoi(RR, nullptr, 16);
        partColor.g = std::stoi(GG, nullptr, 16);
        partColor.b = std::stoi(BB, nullptr, 16);
        partColor.a = std::stoi(AA, nullptr, 16);
        baseAdress[0] = split(code1, ' ')[0];
        baseAdress[1] = split(code2, ' ')[0];
    }
    string hex_string(int input) {
        std::stringstream hexstringStream;
        hexstringStream << hex << input;
        return hexstringStream.str();
    }
    string to_uppercase(string input) {
        std::string replacements = "abcdef";
        std::string replacewith = "ABCDEF";
        for (unsigned int i1 = 0; i1 < input.size(); i1++)
            for (unsigned int i = 0; i < 6; i++)
                if (input[i1] == replacements[i])
                    input[i1] = replacewith[i];
        return input;
    }
    void hexCorret(int input) {
        if (input < 16)
            cout << '0';
        cout << to_uppercase(hex_string(input));
    }

    void printColorCode() {
        cout << baseAdress[0] << " ";
        hexCorret(partColor.r);
        hexCorret(partColor.g);
        cout << "\n";
        cout << baseAdress[1] << " ";
        hexCorret(partColor.b);
        hexCorret(partColor.a);
        cout << "\n";
    }
};