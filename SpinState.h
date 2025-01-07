#ifndef SPINSTATE_H
#define SPINSTATE_H

#include <vector>

class SpinState {
    private:
        float spin;
        std::vector<double> spinZComponents;
    public:
        void setSpin(float s);
        float getSpin();
        void setSpinZComponents(std::vector<double> sz);
        std::vector<double> getSpinZComponents();
};

#endif // SPINSTATE_H
