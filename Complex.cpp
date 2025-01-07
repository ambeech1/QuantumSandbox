#include "Complex.h"
#include <cmath>

Complex::Complex(double real, double imag) : std::complex<double>(real, imag) {}

Complex Complex::operator-() const {
    return Complex(-this->real(), -this->imag());
}

Complex operator+(const Complex& lhs, const Complex& rhs) {
    return Complex(lhs.real() + rhs.real(), lhs.imag() + rhs.imag());
}

Complex operator-(const Complex& lhs, const Complex& rhs) {
    return Complex(lhs.real() - rhs.real(), lhs.imag() - rhs.imag());
}

Complex operator*(const Complex& lhs, const Complex& rhs) {
    return Complex(lhs.real() * rhs.real() - lhs.imag() * rhs.imag(), lhs.real() * rhs.imag() + lhs.imag() * rhs.real());
}

Complex operator/(const Complex& lhs, const Complex& rhs) {
    return Complex(((lhs.real() * rhs.real() + lhs.imag() * rhs.imag()) / (rhs.real() * rhs.real() + rhs.imag() * rhs.imag())), ((lhs.imag() * rhs.real() - lhs.real() * rhs.imag()) / (rhs.real() * rhs.real() + rhs.imag() * rhs.imag())));
}

Complex operator+(const int& lhs, const Complex& rhs) {
    return Complex(lhs + rhs.real(), rhs.imag());
}

Complex operator+(const Complex& lhs, const int& rhs) {
    return Complex(lhs.real() + rhs, lhs.imag());
}

Complex operator-(const int& lhs, const Complex& rhs) {
    return Complex(lhs - rhs.real(), -rhs.imag());
}

Complex operator-(const Complex& lhs, const int& rhs) {
    return Complex(lhs.real() - rhs, lhs.imag());
}

Complex operator*(const int& lhs, const Complex& rhs) {
    return Complex(lhs * rhs.real(), lhs * rhs.imag());;
}

Complex operator*(const Complex& lhs, const int& rhs) {
    return Complex(lhs.real() * rhs, lhs.imag() * rhs);
}

Complex operator/(const int& lhs, const Complex& rhs) {
    return Complex(((lhs * rhs.real()) / (rhs.real() * rhs.real() + rhs.imag() * rhs.imag())), ((-lhs * rhs.imag()) / (rhs.real() * rhs.real() + rhs.imag() * rhs.imag())));
}

Complex operator/(const Complex& lhs, const int& rhs) {
    return Complex(((lhs.real() * rhs) / (rhs * rhs)), ((lhs.imag() * rhs) / (rhs * rhs)));
}

Complex operator+(const double& lhs, const Complex& rhs) {
    return Complex(lhs + rhs.real(), rhs.imag());
}

Complex operator+(const Complex& lhs, const double& rhs) {
    return Complex(lhs.real() + rhs, lhs.imag());
}

Complex operator-(const double& lhs, const Complex& rhs) {
    return Complex(lhs - rhs.real(), -rhs.imag());
}

Complex operator-(const Complex& lhs, const double& rhs) {
    return Complex(lhs.real() - rhs, lhs.imag());
}

Complex operator*(const double& lhs, const Complex& rhs) {
    return Complex(lhs * rhs.real(), lhs * rhs.imag());
}

Complex operator*(const Complex& lhs, const double& rhs) {
    return Complex(lhs.real() * rhs, lhs.imag() * rhs);
}

Complex operator/(const double& lhs, const Complex& rhs) {
    return Complex(((lhs * rhs.real()) / (rhs.real() * rhs.real() + rhs.imag() * rhs.imag())), ((-lhs * rhs.imag()) / (rhs.real() * rhs.real() + rhs.imag() * rhs.imag())));
}

Complex operator/(const Complex& lhs, const double& rhs) {
    return Complex(((lhs.real() * rhs) / (rhs * rhs)), ((lhs.imag() * rhs) / (rhs * rhs)));
}

Complex exp(Complex& z) {
    return exp(z.real()) * (cos(z.imag()) + i * sin(z.imag()));
}

Complex sin(Complex& z) {
    return sin(z.real()) * cosh(z.imag()) - i * cos(z.real()) * sinh(z.imag());
}

Complex cos(Complex& z) {
    return cos(z.real()) * cosh(z.imag()) + i * sin(z.real()) * sinh(z.imag());
}

Complex tan(Complex& z) {
    return sin(z) / cos(z);
}

Complex sinh(Complex& z) {
    Complex s = i * z;
    return -i * sin(s);
}

Complex cosh(Complex& z) {
    Complex s = i * z;
    return cos(s);
}

Complex tanh(Complex& z) {
    return sinh(z) / cosh(z);
}

Complex conj(Complex& z) {
    return Complex(z.real(), -z.imag());
}

Complex ln(double x) {
    return Complex(log(x), 0);
}

Complex ln(Complex z) {
    return norm(z) + i * arg(z);
}

double norm(Complex& z) {
    return sqrt((z * conj(z)).real());
}

double normSq(Complex& z) {
    return (z * conj(z)).real();
}

Complex pow(Complex& z, Complex p) {
    double Re =  (pow(norm(z), p.real()) * exp(i * p.imag() * ln(norm(z))) * exp(i * p.real() * arg(z)) * exp(-p.imag() * arg(z))).real();
    double Im =  (pow(norm(z), p.real()) * exp(i * p.imag() * ln(norm(z))) * exp(i * p.real() * arg(z)) * exp(-p.imag() * arg(z))).imag();
    return Complex(Re, Im);
}
