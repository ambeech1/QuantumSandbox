#ifndef _COMPLEX_
#define _COMPLEX_

#include <complex>

#define i Complex(0, 1)
#define e double(2.718281828459045235360287471352)
#define pi double(3.1415926535897932384626433832795)

class Complex : public std::complex<double> {
public:
    Complex(double real, double imag);

    Complex operator-() const;

    friend Complex operator+(const Complex& lhs, const Complex& rhs);
    friend Complex operator-(const Complex& lhs, const Complex& rhs);
    friend Complex operator*(const Complex& lhs, const Complex& rhs);
    friend Complex operator/(const Complex& lhs, const Complex& rhs);

    friend Complex operator+(const int& lhs, const Complex& rhs);
    friend Complex operator+(const Complex& lhs, const int& rhs);
    friend Complex operator-(const int& lhs, const Complex& rhs);
    friend Complex operator-(const Complex& lhs, const int& rhs);
    friend Complex operator*(const int& lhs, const Complex& rhs);
    friend Complex operator*(const Complex& lhs, const int& rhs);
    friend Complex operator/(const int& lhs, const Complex& rhs);
    friend Complex operator/(const Complex& lhs, const int& rhs);

    friend Complex operator+(const double& lhs, const Complex& rhs);
    friend Complex operator+(const Complex& lhs, const double& rhs);
    friend Complex operator-(const double& lhs, const Complex& rhs);
    friend Complex operator-(const Complex& lhs, const double& rhs);
    friend Complex operator*(const double& lhs, const Complex& rhs);
    friend Complex operator*(const Complex& lhs, const double& rhs);
    friend Complex operator/(const double& lhs, const Complex& rhs);
    friend Complex operator/(const Complex& lhs, const double& rhs);
};

#endif
