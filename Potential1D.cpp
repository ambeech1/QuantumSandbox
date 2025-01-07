#include "Potential1D.h"
#include <vector>
#include <cmath>

std::vector<double> InfWell(std::vector<double> POS) {
    std::vector<double> POT(POS.size());
    for (int i = 0; i < POS.size(); i++) {
        if (abs(POS[i]) < 5) {
            POT[i] = 0;
        }
        else {
            POT[i] = 1000000000;
        }
    }
    return POT;
}

std::vector<double> FWell(std::vector<double> POS) {
    std::vector<double> POT(POS.size());
    for (int i = 0; i < POS.size(); i++) {
        if (abs(POS[i]) < 5) {
            POT[i] = 0;
        }
        else {
            POT[i] = 10;
        }
    }
    return POT;
}

std::vector<double> Barrier(std::vector<double> POS) {
    std::vector<double> POT(POS.size());
    for (int i = 0; i < POS.size(); i++) {
        if (abs(POS[i]) < 0.5) {
            POT[i] = 50;
        }
        else {
            POT[i] = 0;
        }
    }
    return POT;
}

std::vector<double> Quad(std::vector<double> POS) {
    std::vector<double> POT(POS.size());
    for (int i = 0; i < POS.size(); i++) {
        POT[i] = pow(POS[i], 2) / 5;
    }
    return POT;
}




Potential1D::Potential1D() : xmin(-10), xmax(10), N(101), fx(InfWell), form(infWell) {
    dx = (xmax - xmin) / (N - 1);
    setPos();
    setPot(form);
}


Potential1D::Potential1D(double min, double max, double num) : xmin(min), xmax(max), N(num), fx(InfWell), form(infWell) {
    dx = (xmax - xmin) / (N - 1);
    setPos();
    setPot(form);
}


Potential1D::Potential1D(double min, double max, double num, FORM p) : xmin(min), N(num), xmax(max), form(p) {
    dx = (xmax - xmin) / (N - 1);
    setPos();
    setPot(form);
}


void Potential1D::setPosMin(double min) {
    xmin = min;
    dx = (xmax - xmin) / (N - 1);
    setPos();
    setPot(form);
}


void Potential1D::setPosMax(double max) {
    xmax = max;
    dx = (xmax - xmin) / (N - 1);
    setPos();
    setPot(form);
}


void Potential1D::setPosN(double num) {
    N = num;
    dx = (xmax - xmin) / (N - 1);
    setPos();
    setPot(form);
}


void Potential1D::setPot(FORM p) {
    form = p;
    switch(p) {
    case infWell:
        fx = InfWell;
        break;
    case fWell:
        fx = FWell;
        break;
    case barrier:
        fx = Barrier;
        break;
    case quad:
        fx = Quad;
        break;
    }
    pot = invoke(pos, fx);
}


std::vector<double> Potential1D::getPos() {
    return pos;
}


std::vector<double> Potential1D::getPot() {
    return pot;
}


void Potential1D::setPos() {
    pos.resize(N);
    for (int i = 0; i < N; i++) {
        pos[i] = xmin + (i * dx);
    }
}


std::vector<double> Potential1D::invoke(std::vector<double> POS, std::vector<double> (*func)(std::vector<double> POS)) {
    return func(POS);
}


double Potential1D::getPosMin() {
    return xmin;
}


double Potential1D::getPosMax() {
    return xmax;
}


double Potential1D::getPosN() {
    return N;
}
