#include "State.h"

State::State() {}

State::~State() {}

std::vector<double> State::getPosExp() {
    return posExp;
}

std::vector<double> State::getVelExp() {
    return velExp;
}

std::vector<double> State::getMomExp() {
    return momExp;
}

std::vector<double> State::getAMomExp() {
    return aMomExp;
}

double State::getEnrgExp() {
    return enrgExp;
}

double State::getKEnrgExp() {
    return kEnrgExp;
}

double State::getPEnrgExp() {
    return pEnrgExp;
}
