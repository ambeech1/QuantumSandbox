#include <vector>
#include <Qvector>

QVector<double> vec2qvec(std::vector<double> V) {
    QVector<double> QV;
    for (double val : V) {
        QV.append(val);
    }
    return QV;
}

std::vector<double> vec2qvec(QVector<double> QV) {
    std::vector<double> V;
    for (double val : QV) {
        V.push_back(val);
    }
    return V;
}
