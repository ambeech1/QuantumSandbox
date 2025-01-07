#include <Eigen/Sparse>
#include <Spectra/SymEigsSolver.h>
#include <Spectra/MatOp/SparseSymMatProd.h>
#include <cmath>
#include <utility>
#include "Potential1D.h"

std::pair<std::vector<double>, std::vector<std::vector<double>>> solveEigen(int prQuNum, Potential1D pot = Potential1D(), double hbar = 1, double m = 0.5) {
    // instantiate constants
    double xmin = pot.getPosMin();
    double xmax = pot.getPosMax();
    int N = pot.getPosN();
    double dx = (xmin - xmax) / (N - 1);
    double A = -(pow(hbar, 2)) / (2 * m);

    // instantiate position
    Eigen::VectorXd x(N);
    for (int i = 0; i < N; i++) {
        x(i) = xmin + (i * dx);
    }

    // instantiate potential energy
    std::vector<double> v = pot.getPot();
    Eigen::VectorXd V(N);
    for (int i = 0; i < N; i++) {
        V(i) = v[i];
    }

    // instantiate Hamiltonian
    Eigen::SparseMatrix<double> H(N, N);
    H.reserve(3 * N - 2);
    for (int i = 0; i < N; i++) {
        H.insert(i, i) = V(i) - (2.0 * A / pow(dx, 2));
    }
    for (int i = 0; i < N - 1; i++) {
        H.insert(i, i + 1) = A / pow(dx, 2);
        H.insert(i + 1, i) = A / pow(dx, 2);
    }

    Spectra::SparseSymMatProd<double> op(H);
    Spectra::SymEigsSolver<Spectra::SparseSymMatProd<double>> eigs(op, prQuNum, N);
    eigs.init();
    int nconv = eigs.compute(Spectra::SortRule::SmallestMagn);

    // get eigenvalues
    Eigen::VectorXd eigenvalues = eigs.eigenvalues();
    std::vector<double> evals;
    for (int i = 0; i < prQuNum; i++) {
        evals.push_back(eigenvalues[i]);
    }

    // get eigenvectors
    Eigen::MatrixXd eigenvectors = eigs.eigenvectors();
    std::vector<std::vector<double>> evects;
    for (int i = 0; i < prQuNum; i++) {
        std::vector<double> stdV(eigenvectors.col(i).real().data(), eigenvectors.col(i).real().data() + eigenvectors.col(i).real().size());
        evects.push_back(stdV);
    }

    return std::pair<std::vector<double>, std::vector<std::vector<double>>>(evals, evects);
}
