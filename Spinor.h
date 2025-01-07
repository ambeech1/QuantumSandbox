#ifndef SPINOR_H
#define SPINOR_H

#include "State2D.h"
#include "SpinState.h"
#include <vector>
#include <utility>

class Spinor : public State2D {
    private:
        SpinState S;
    public:
        void setSpinState(float s);
        void setSpinState(std::vector<double> sz);
        void setSpinState(float s, std::vector<double> sz);
        SpinState getSpinState();
        float getSpin();
        std::vector<double> getSpinZComponents();
        std::pair<std::vector<State2D>, std::vector<float>> splitBySZ();
};

#endif // SPINOR_H
