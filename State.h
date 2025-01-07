#ifndef STATE_H
#define STATE_H

#include <vector>

class State {
    private:
        std::vector<double> posExp;
        std::vector<double> velExp;
        std::vector<double> momExp;
        std::vector<double> aMomExp;
        double enrgExp;
        double kEnrgExp;
        double pEnrgExp;
    public:
        State();
        ~State();
        std::vector<double> getPosExp();
        std::vector<double> getVelExp();
        std::vector<double> getMomExp();
        std::vector<double> getAMomExp();
        double getEnrgExp();
        double getKEnrgExp();
        double getPEnrgExp();
};

#endif // STATE_H
