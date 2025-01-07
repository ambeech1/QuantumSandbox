#ifndef STATE1D_H
#define STATE1D_H

#include "State.h"
#include <complex>
#include <vector>
#include <QVector>

class State1D : public State {
    private:
        const int dim = 1;
        QVector<std::complex<double>> vals;
    public:
        State1D();
        ~State1D();
        void setState(QVector<std::complex<double>> v);
        QVector<std::complex<double>> getPsi();
        std::vector<double> getReal();
        std::vector<double> getImag();
        std::vector<double> getNorm();
        std::vector<double> getNormSq();
};

#endif // STATE1D_H
