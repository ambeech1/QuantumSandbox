#ifndef STATE2D_H
#define STATE2D_H

#include "State.h"
#include <math.h>
#include <vector>

class State2D : public State {
    private:
        const int dim = 2;
        std::vector<std::vector<_complex>> vals;
    public:
        State2D();
        ~State2D();
        void setState(std::vector<std::vector<_complex>> v);
};

#endif // STATE2D_H
