#pragma once
struct color {
    unsigned char r;
    unsigned char g;
    unsigned char b;
    unsigned char a;
    void init(unsigned char _r, unsigned char _g, unsigned char _b, unsigned char _a) {
        r = _r;
        g = _g;
        b = _b;
        a = _a;

    }
    color(unsigned char _r, unsigned char _g, unsigned char _b, unsigned char _a) {
        init(_r, _g, _b, _a);
    }
    color() {

    }

    void invert() {
        r = 0xFF - r;
        g = 0xFF - g;
        b = 0xFF - b;
    }
};