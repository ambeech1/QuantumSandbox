#ifndef _POTENTIAL1D_
#define _POTENTIAL1D_

#include <vector>

enum FORM {infWell, fWell, barrier, quad};

class Potential1D {
public:
    Potential1D();
    Potential1D(double min, double max, double num);
    Potential1D(double min, double max, double num, FORM p);
    void setPosMin(double min);
    void setPosMax(double max);
    void setPosN(double num);
    void setPot(FORM p);
    std::vector<double> getPos();
    std::vector<double> getPot();
    double getPosMin();
    double getPosMax();
    double getPosN();
private:
    std::vector<double> pos;
    double xmin;
    double xmax;
    double N;
    double dx;
    std::vector<double> pot;
    std::vector<double> (*fx)(std::vector<double> POS);
    FORM form;
    void setPos();
    std::vector<double> invoke(std::vector<double> POS, std::vector<double> (*func)(std::vector<double> POS));
};

#endif
