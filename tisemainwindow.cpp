#include "tisemainwindow.h"
#include "ui_tisemainwindow.h"
#include "Potential1D.h"
#include "VecQVecConvert.cpp"
#include "TISE_1D.cpp"
#include <QVector>
#include <QPen>
#include <QColor>

int legendPosInd;
double tickAspectRatio = 1.0;

double xmin1D = -10;
double xmax1D = 10;
double ymin1D1 = -7;
double ymax1D1 = 7;
double ymin1D2 = -7;
double ymax1D2 = 7;
double xmin1Dsol = -10;
double xmax1Dsol = 10;
int N1D = 501;

Potential1D Pot1D;
QPen pot1Dpen;
int pot1DpenR = 0;
int pot1DpenG = 0;
int pot1DpenB = 0;
int pot1DpenLw = 2;

int prQuNum = 1;
bool upToPr = false;

TISEMainWindow::TISEMainWindow(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::TISEMainWindow)
{
    Pot1D.setPosMin(xmin1Dsol);
    Pot1D.setPosMax(xmax1Dsol);
    Pot1D.setPosN(N1D);

    // set up default tab and widget settings
    ui->setupUi(this);
    ui->tabDSelect->setCurrentIndex(0);
    ui->tabs1d->setCurrentIndex(0);
    ui->tabs2d->setCurrentIndex(0);
    ui->showAxisLabels->setChecked(true);
    ui->showAxisLabels_2->setChecked(true);
    ui->showLegend->setChecked(true);
    ui->showXTicks->setChecked(true);
    ui->showYTicksL->setChecked(true);
    ui->showYTicksR->setChecked(true);
    ui->showTicks->setChecked(true);
    ui->showGrid->setChecked(true);
    ui->showAxes->setChecked(true);

    // set up legend (1D)
    ui->TISEPlot1D->legend->setVisible(true);
    QFont legendFont = font();
    legendFont.setPointSize(9);
    ui->TISEPlot1D->legend->setFont(legendFont);
    ui->TISEPlot1D->legend->setBrush(QBrush(QColor(255, 255, 255, 230)));
    ui->TISEPlot1D->axisRect()->insetLayout()->setInsetAlignment(0, Qt::AlignTop | Qt::AlignRight);
    legendPosInd = 0;

    // set up plot (1D)
    ui->TISEPlot1D->addGraph(ui->TISEPlot1D->xAxis, ui->TISEPlot1D->yAxis2);
    pot1Dpen.setColor(QColor(pot1DpenR, pot1DpenG, pot1DpenB));
    pot1Dpen.setWidthF(pot1DpenLw);
    ui->TISEPlot1D->graph(0)->setPen(pot1Dpen);
    ui->TISEPlot1D->graph(0)->setLineStyle(QCPGraph::lsLine);
    ui->TISEPlot1D->graph(0)->setPen(QPen(pot1Dpen));
    ui->TISEPlot1D->graph(0)->setName("Potential Energy");
    //ui->TISEPlot1D->addGraph(ui->TISEPlot1D->xAxis, ui->TISEPlot1D->yAxis);
    //ui->TISEPlot1D->graph(1)->setLineStyle(QCPGraph::lsLine);
    //ui->TISEPlot1D->graph(1)->setName("Wavefunction");
    ui->TISEPlot1D->xAxis->setLabel("Position");
    ui->TISEPlot1D->yAxis->setLabel("Wavefunction");
    ui->TISEPlot1D->yAxis2->setLabel("Potential Energy");
    ui->TISEPlot1D->xAxis->setRange(xmin1D, xmax1D);
    ui->TISEPlot1D->yAxis->setRange(ymin1D1, ymax1D1);
    ui->TISEPlot1D->yAxis2->setRange(ymin1D2, ymax1D2);
    ui->TISEPlot1D->yAxis2->setVisible(true);
    ui->TISEPlot1D->xAxis->grid()->setSubGridVisible(true);
    ui->TISEPlot1D->yAxis->grid()->setSubGridVisible(true);

    // set up colorbar (2D)


    // set up plot (2D)
    ui->TISEPlot2D->addGraph(ui->TISEPlot2D->xAxis, ui->TISEPlot2D->yAxis);
    ui->TISEPlot2D->xAxis->setLabel("Position (x)");
    ui->TISEPlot2D->yAxis->setLabel("Position (y)");
    ui->TISEPlot2D->xAxis->setRange(-10, 10);
    ui->TISEPlot2D->yAxis->setRange(-7, 7);
    ui->TISEPlot2D->yAxis2->setRange(-7, 7);
    ui->TISEPlot2D->xAxis->grid()->setZeroLinePen(QPen(QColor(255, 255, 255, 100), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
    ui->TISEPlot2D->yAxis->grid()->setZeroLinePen(QPen(QColor(255, 255, 255, 100), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
    ui->TISEPlot2D->xAxis->grid()->setPen(QPen(QColor(255, 255, 255, 100), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
    ui->TISEPlot2D->yAxis->grid()->setPen(QPen(QColor(255, 255, 255, 100), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));

    // Initialize Plot (1D)
    QVector<double> X(vec2qvec(Pot1D.getPos()));
    QVector<double> Y(vec2qvec(Pot1D.getPot()));

    ui->TISEPlot1D->graph(0)->setData(X, Y);
    ui->TISEPlot1D->replot();
    ui->TISEPlot1D->update();
}

TISEMainWindow::~TISEMainWindow()
{
    delete ui;
}

// maintain axes aspect ratio
void TISEMainWindow::resizeEvent(QResizeEvent *event) {
    QDialog::resizeEvent(event);
    QCPAxis *x = ui->TISEPlot2D->axisRect()->axis(QCPAxis::atBottom);
    QCPAxis *y = ui->TISEPlot2D->axisRect()->axis(QCPAxis::atLeft);
    y->setScaleRatio(x, tickAspectRatio);
    ui->TISEPlot2D->replot();
    ui->TISEPlot2D->update();
}

// 1D

void TISEMainWindow::on_tise1DTabInfo_clicked()
{
    QMessageBox::about(this, "Tab Descriptions", "Plot Settings: Adjust the appearance and axis ranges of the plot window.\n\nPotential Energy: Configure the desired potential energy function and boundary conditions.\n\nSolution Parameters: Adjust the accuracy of the solution, as well as particle mass and the scale of Planck's constant.\n\nDisplay: Choose what variables should appear on the plot.\n\nManage Solutions: Show and hide previously found solutions, and save desired solutions to be viewed and manipulated in the TDSE module.");
}

void TISEMainWindow::on_xmin_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        ui->TISEPlot1D->xAxis->setRangeLower(-10);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        double xmin = arg1.toDouble();
        ui->TISEPlot1D->xAxis->setRangeLower(xmin);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}

void TISEMainWindow::on_xmax_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        ui->TISEPlot1D->xAxis->setRangeUpper(10);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        double xmax = arg1.toDouble();
        ui->TISEPlot1D->xAxis->setRangeUpper(xmax);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}

void TISEMainWindow::on_ymin_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        ui->TISEPlot1D->yAxis->setRangeLower(-7);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        double ymin = arg1.toDouble();
        ui->TISEPlot1D->yAxis->setRangeLower(ymin);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}

void TISEMainWindow::on_ymax_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        ui->TISEPlot1D->yAxis->setRangeUpper(7);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        double ymax = arg1.toDouble();
        ui->TISEPlot1D->yAxis->setRangeUpper(ymax);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}

void TISEMainWindow::on_autoRange1d_clicked()
{
    if (ui->TISEPlot1D->itemCount() == 1) {
        ui->TISEPlot1D->xAxis->setRange(-10, 10);
        ui->TISEPlot1D->yAxis->setRange(-7, 7);
        ui->TISEPlot1D->yAxis2->setRange(-7, 7);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        ui->TISEPlot1D->rescaleAxes();
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}

void TISEMainWindow::on_yminR_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        ui->TISEPlot1D->yAxis2->setRangeLower(-7);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        double ymin = arg1.toDouble();
        ui->TISEPlot1D->yAxis2->setRangeLower(ymin);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}

void TISEMainWindow::on_ymaxR_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        ui->TISEPlot1D->yAxis2->setRangeUpper(7);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        double ymax = arg1.toDouble();
        ui->TISEPlot1D->yAxis2->setRangeUpper(ymax);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}

void TISEMainWindow::on_showAxisLabels_stateChanged(int arg1)
{
    if (ui->showAxisLabels->isChecked()) {
        ui->TISEPlot1D->xAxis->setLabel("Position");
        ui->TISEPlot1D->yAxis->setLabel("Wavefunction");
        ui->TISEPlot1D->yAxis2->setLabel("Potential Energy");
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        ui->TISEPlot1D->xAxis->setLabel("");
        ui->TISEPlot1D->yAxis->setLabel("");
        ui->TISEPlot1D->yAxis2->setLabel("");
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}

void TISEMainWindow::on_showLegend_stateChanged(int arg1)
{
    if (ui->showLegend->isChecked()) {
        ui->TISEPlot1D->legend->setVisible(true);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        ui->TISEPlot1D->legend->setVisible(false);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}

void TISEMainWindow::on_showGrid_stateChanged(int arg1)
{
    if (ui->showGrid->isChecked()) {
        ui->TISEPlot1D->xAxis->grid()->setSubGridVisible(true);
        ui->TISEPlot1D->yAxis->grid()->setSubGridVisible(true);
        ui->TISEPlot1D->xAxis->grid()->setPen(QPen(QColor(0, 0, 0, 30), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
        ui->TISEPlot1D->yAxis->grid()->setPen(QPen(QColor(0, 0, 0, 30), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
        if (!ui->showAxes->isChecked()) {
            ui->TISEPlot1D->xAxis->grid()->setZeroLinePen(QPen(QColor(0, 0, 0, 30), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
            ui->TISEPlot1D->yAxis->grid()->setZeroLinePen(QPen(QColor(0, 0, 0, 30), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
        }
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
        QColor();
    }
    else {
        ui->TISEPlot1D->xAxis->grid()->setSubGridVisible(false);
        ui->TISEPlot1D->yAxis->grid()->setSubGridVisible(false);
        ui->TISEPlot1D->xAxis->grid()->setPen(QPen(QColor(255, 255, 255, 100), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
        ui->TISEPlot1D->yAxis->grid()->setPen(QPen(QColor(255, 255, 255, 100), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
        if (!ui->showAxes->isChecked()) {
            ui->TISEPlot1D->xAxis->grid()->setZeroLinePen(QPen(QColor(255, 255, 255, 100), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
            ui->TISEPlot1D->yAxis->grid()->setZeroLinePen(QPen(QColor(255, 255, 255, 100), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
        }
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}

void TISEMainWindow::on_showAxes_stateChanged(int arg1)
{
    if (ui->showAxes->isChecked()) {
        ui->TISEPlot1D->xAxis->grid()->setZeroLinePen(QPen(QColor(0, 0, 0, 100), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
        ui->TISEPlot1D->yAxis->grid()->setZeroLinePen(QPen(QColor(0, 0, 0, 100), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        if (ui->showGrid->isChecked()) {
            ui->TISEPlot1D->xAxis->grid()->setZeroLinePen(QPen(QColor(0, 0, 0, 30), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
            ui->TISEPlot1D->yAxis->grid()->setZeroLinePen(QPen(QColor(0, 0, 0, 30), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
        }
        else {
            ui->TISEPlot1D->xAxis->grid()->setZeroLinePen(QPen(QColor(255, 255, 255, 100), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
            ui->TISEPlot1D->yAxis->grid()->setZeroLinePen(QPen(QColor(255, 255, 255, 100), 1, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
        }
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}

void TISEMainWindow::on_showXTicks_stateChanged(int arg1)
{
    if (ui->showXTicks->isChecked()) {
        ui->TISEPlot1D->xAxis->setTicks(true);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        ui->TISEPlot1D->xAxis->setTicks(false);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}

void TISEMainWindow::on_showYTicksL_stateChanged(int arg1)
{
    if (ui->showYTicksL->isChecked()) {
        ui->TISEPlot1D->yAxis->setTicks(true);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        ui->TISEPlot1D->yAxis->setTicks(false);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}

void TISEMainWindow::on_showYTicksR_stateChanged(int arg1)
{
    if (ui->showYTicksR->isChecked()) {
        ui->TISEPlot1D->yAxis2->setTicks(true);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        ui->TISEPlot1D->yAxis2->setTicks(false);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}

void TISEMainWindow::on_pushButton_clicked()
{
    if (legendPosInd == 0) {
        ui->TISEPlot1D->axisRect()->insetLayout()->setInsetAlignment(0, Qt::AlignBottom | Qt::AlignRight);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
        legendPosInd = 1;
    }
    else if (legendPosInd == 1) {
        ui->TISEPlot1D->axisRect()->insetLayout()->setInsetAlignment(0, Qt::AlignBottom | Qt::AlignLeft);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
        legendPosInd = 2;
    }
    else if (legendPosInd == 2) {
        ui->TISEPlot1D->axisRect()->insetLayout()->setInsetAlignment(0, Qt::AlignTop | Qt::AlignLeft);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
        legendPosInd = 3;
    }
    else if (legendPosInd == 3) {
        ui->TISEPlot1D->axisRect()->insetLayout()->setInsetAlignment(0, Qt::AlignTop | Qt::AlignRight);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
        legendPosInd = 0;
    }
}



// 2D
void TISEMainWindow::on_pushButton_2_clicked()
{
    QMessageBox::about(this, "Tab Descriptions", "Plot Settings: Adjust the appearance and axis ranges of the plot window.\n\nPotential Energy: Configure the desired potential energy function and boundary conditions. Specify a spin-dependency if desired.\n\nSolution Parameters: Adjust the accuracy of the solution, as well as particle mass and the scale of Planck's constant.\n\nDisplay: Choose what variables should appear on the plot.\n\nManage Solutions: Show and hide previously found solutions, and save desired solutions to be viewed and manipulated in the TDSE module.\n\nSpin Parameters: Configure the spin components of the wavefunction, if desired.");
}

void TISEMainWindow::on_xmin_2_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        ui->TISEPlot2D->xAxis->setRangeLower(-10);
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
    else {
        double xmin = arg1.toDouble();
        ui->TISEPlot2D->xAxis->setRangeLower(xmin);
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
}

void TISEMainWindow::on_xmax_2_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        ui->TISEPlot2D->xAxis->setRangeUpper(10);
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
    else {
        double xmax = arg1.toDouble();
        ui->TISEPlot2D->xAxis->setRangeUpper(xmax);
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
}

void TISEMainWindow::on_ymin_2_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        ui->TISEPlot2D->yAxis->setRangeLower(-7);
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
    else {
        double ymin = arg1.toDouble();
        ui->TISEPlot2D->yAxis->setRangeLower(ymin);
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
}

void TISEMainWindow::on_ymax_2_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        ui->TISEPlot2D->yAxis->setRangeUpper(7);
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
    else {
        double ymax = arg1.toDouble();
        ui->TISEPlot2D->yAxis->setRangeUpper(ymax);
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
}

void TISEMainWindow::on_autoRange1d_2_clicked()
{
    if (ui->TISEPlot2D->itemCount() == 0) {
        ui->TISEPlot2D->xAxis->setRange(-10, 10);
        ui->TISEPlot2D->yAxis->setRange(-7, 7);
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
    else {
        ui->TISEPlot2D->rescaleAxes();
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
}

void TISEMainWindow::on_showAxisLabels_2_stateChanged(int arg1)
{
    if (ui->showAxisLabels_2->isChecked()) {
        ui->TISEPlot2D->xAxis->setLabel("Position (x)");
        ui->TISEPlot2D->yAxis->setLabel("Position (y)");
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
    else {
        ui->TISEPlot2D->xAxis->setLabel("");
        ui->TISEPlot2D->yAxis->setLabel("");
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
}

/**
void TISEMainWindow::on_showLegend_2_stateChanged(int arg1)
{

}
*/

void TISEMainWindow::on_showColormap_stateChanged(int arg1)
{

}

void TISEMainWindow::on_showTicks_stateChanged(int arg1)
{
    if (ui->showTicks->isChecked()) {
        ui->TISEPlot2D->xAxis->setTicks(true);
        ui->TISEPlot2D->yAxis->setTicks(true);
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
    else {
        ui->TISEPlot2D->xAxis->setTicks(false);
        ui->TISEPlot2D->yAxis->setTicks(false);
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
}

void TISEMainWindow::on_lineEdit_8_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        tickAspectRatio = 1.0;
        ui->TISEPlot2D->axisRect()->axis(QCPAxis::atLeft)->setScaleRatio(ui->TISEPlot2D->axisRect()->axis(QCPAxis::atBottom), tickAspectRatio);
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
    else {
        tickAspectRatio = arg1.toDouble();
        ui->TISEPlot2D->axisRect()->axis(QCPAxis::atLeft)->setScaleRatio(ui->TISEPlot2D->axisRect()->axis(QCPAxis::atBottom), tickAspectRatio);
        ui->TISEPlot2D->replot();
        ui->TISEPlot2D->update();
    }
}





void TISEMainWindow::on_infWel_clicked()
{
    // remove existing wavefunctions
    int numGraphs = ui->TISEPlot1D->clearGraphs();

    ui->TISEPlot1D->addGraph(ui->TISEPlot1D->xAxis, ui->TISEPlot1D->yAxis2);
    pot1Dpen.setColor(QColor(pot1DpenR, pot1DpenG, pot1DpenB));
    pot1Dpen.setWidthF(pot1DpenLw);
    ui->TISEPlot1D->graph(0)->setPen(pot1Dpen);
    ui->TISEPlot1D->graph(0)->setLineStyle(QCPGraph::lsLine);
    ui->TISEPlot1D->graph(0)->setPen(QPen(pot1Dpen));
    ui->TISEPlot1D->graph(0)->setName("Potential Energy");
    Pot1D.setPot(infWell);
    QVector<double> X(vec2qvec(Pot1D.getPos()));
    QVector<double> Y(vec2qvec(Pot1D.getPot()));
    ui->TISEPlot1D->graph(0)->setData(X, Y);
    ui->TISEPlot1D->replot();
    ui->TISEPlot1D->update();
}


void TISEMainWindow::on_fWell_clicked()
{
    // remove existing wavefunctions
    int numGraphs = ui->TISEPlot1D->clearGraphs();

    ui->TISEPlot1D->addGraph(ui->TISEPlot1D->xAxis, ui->TISEPlot1D->yAxis2);
    pot1Dpen.setColor(QColor(pot1DpenR, pot1DpenG, pot1DpenB));
    pot1Dpen.setWidthF(pot1DpenLw);
    ui->TISEPlot1D->graph(0)->setPen(pot1Dpen);
    ui->TISEPlot1D->graph(0)->setLineStyle(QCPGraph::lsLine);
    ui->TISEPlot1D->graph(0)->setPen(QPen(pot1Dpen));
    ui->TISEPlot1D->graph(0)->setName("Potential Energy");
    Pot1D.setPot(fWell);
    QVector<double> X(vec2qvec(Pot1D.getPos()));
    QVector<double> Y(vec2qvec(Pot1D.getPot()));
    ui->TISEPlot1D->graph(0)->setData(X, Y);
    ui->TISEPlot1D->replot();
    ui->TISEPlot1D->update();
}


void TISEMainWindow::on_barrier_clicked()
{
    // remove existing wavefunctions
    int numGraphs = ui->TISEPlot1D->clearGraphs();

    ui->TISEPlot1D->addGraph(ui->TISEPlot1D->xAxis, ui->TISEPlot1D->yAxis2);
    pot1Dpen.setColor(QColor(pot1DpenR, pot1DpenG, pot1DpenB));
    pot1Dpen.setWidthF(pot1DpenLw);
    ui->TISEPlot1D->graph(0)->setPen(pot1Dpen);
    ui->TISEPlot1D->graph(0)->setLineStyle(QCPGraph::lsLine);
    ui->TISEPlot1D->graph(0)->setPen(QPen(pot1Dpen));
    ui->TISEPlot1D->graph(0)->setName("Potential Energy");
    Pot1D.setPot(barrier);
    QVector<double> X(vec2qvec(Pot1D.getPos()));
    QVector<double> Y(vec2qvec(Pot1D.getPot()));
    ui->TISEPlot1D->graph(0)->setData(X, Y);
    ui->TISEPlot1D->replot();
    ui->TISEPlot1D->update();
}


void TISEMainWindow::on_quad_clicked()
{
    // remove existing wavefunctions
    int numGraphs = ui->TISEPlot1D->clearGraphs();

    ui->TISEPlot1D->addGraph(ui->TISEPlot1D->xAxis, ui->TISEPlot1D->yAxis2);
    pot1Dpen.setColor(QColor(pot1DpenR, pot1DpenG, pot1DpenB));
    pot1Dpen.setWidthF(pot1DpenLw);
    ui->TISEPlot1D->graph(0)->setPen(pot1Dpen);
    ui->TISEPlot1D->graph(0)->setLineStyle(QCPGraph::lsLine);
    ui->TISEPlot1D->graph(0)->setPen(QPen(pot1Dpen));
    ui->TISEPlot1D->graph(0)->setName("Potential Energy");

    Pot1D.setPot(quad);
    QVector<double> X(vec2qvec(Pot1D.getPos()));
    QVector<double> Y(vec2qvec(Pot1D.getPot()));
    ui->TISEPlot1D->graph(0)->setData(X, Y);
    ui->TISEPlot1D->replot();
    ui->TISEPlot1D->update();
}


void TISEMainWindow::on_R_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        pot1DpenR = 0;
        pot1Dpen.setColor(QColor(pot1DpenR, pot1DpenG, pot1DpenB));
        ui->TISEPlot1D->graph(0)->setPen(pot1Dpen);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        pot1DpenR = arg1.toDouble();
        pot1Dpen.setColor(QColor(pot1DpenR, pot1DpenG, pot1DpenB));
        ui->TISEPlot1D->graph(0)->setPen(pot1Dpen);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}


void TISEMainWindow::on_G_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        pot1DpenG = 0;
        pot1Dpen.setColor(QColor(pot1DpenR, pot1DpenG, pot1DpenB));
        ui->TISEPlot1D->graph(0)->setPen(pot1Dpen);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        pot1DpenG = arg1.toDouble();
        pot1Dpen.setColor(QColor(pot1DpenR, pot1DpenG, pot1DpenB));
        ui->TISEPlot1D->graph(0)->setPen(pot1Dpen);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}


void TISEMainWindow::on_B_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        pot1DpenB = 0;
        pot1Dpen.setColor(QColor(pot1DpenR, pot1DpenG, pot1DpenB));
        ui->TISEPlot1D->graph(0)->setPen(pot1Dpen);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        pot1DpenB = arg1.toDouble();
        pot1Dpen.setColor(QColor(pot1DpenR, pot1DpenG, pot1DpenB));
        ui->TISEPlot1D->graph(0)->setPen(pot1Dpen);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}


void TISEMainWindow::on_curveWidth_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        pot1DpenLw = 0;
        pot1Dpen.setWidthF(pot1DpenLw);
        ui->TISEPlot1D->graph(0)->setPen(pot1Dpen);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        pot1DpenLw = arg1.toDouble();
        pot1Dpen.setWidthF(pot1DpenLw);
        ui->TISEPlot1D->graph(0)->setPen(pot1Dpen);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}


void TISEMainWindow::on_xMinSol_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        xmin1Dsol = -10;
        Pot1D.setPosMin(xmin1Dsol);
        QVector<double> X(vec2qvec(Pot1D.getPos()));
        QVector<double> Y(vec2qvec(Pot1D.getPot()));
        ui->TISEPlot1D->graph(0)->setData(X, Y);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        double xmin1Dsol = arg1.toDouble();
        Pot1D.setPosMin(xmin1Dsol);
        QVector<double> X(vec2qvec(Pot1D.getPos()));
        QVector<double> Y(vec2qvec(Pot1D.getPot()));
        ui->TISEPlot1D->graph(0)->setData(X, Y);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}


void TISEMainWindow::on_xMaxSol_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        xmax1Dsol = 10;
        Pot1D.setPosMax(xmax1Dsol);
        QVector<double> X(vec2qvec(Pot1D.getPos()));
        QVector<double> Y(vec2qvec(Pot1D.getPot()));
        ui->TISEPlot1D->graph(0)->setData(X, Y);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        double xmax1Dsol = arg1.toDouble();
        Pot1D.setPosMax(xmax1Dsol);
        QVector<double> X(vec2qvec(Pot1D.getPos()));
        QVector<double> Y(vec2qvec(Pot1D.getPot()));
        ui->TISEPlot1D->graph(0)->setData(X, Y);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}


void TISEMainWindow::on_posStep_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        N1D = 101;
        Pot1D.setPosN(N1D);
        QVector<double> X(vec2qvec(Pot1D.getPos()));
        QVector<double> Y(vec2qvec(Pot1D.getPot()));
        ui->TISEPlot1D->graph(0)->setData(X, Y);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
    else {
        double N1D = arg1.toDouble();
        Pot1D.setPosN(N1D);
        QVector<double> X(vec2qvec(Pot1D.getPos()));
        QVector<double> Y(vec2qvec(Pot1D.getPot()));
        ui->TISEPlot1D->graph(0)->setData(X, Y);
        ui->TISEPlot1D->replot();
        ui->TISEPlot1D->update();
    }
}


void TISEMainWindow::on_prQuNum_textChanged(const QString &arg1)
{
    if (arg1 == "") {
        prQuNum= 1;
    }
    else {
        prQuNum = arg1.toDouble();
    }
}


void TISEMainWindow::on_computeSol_clicked()
{
    // remove existing wavefunctions
    int numGraphs = ui->TISEPlot1D->clearGraphs();

    ui->TISEPlot1D->addGraph(ui->TISEPlot1D->xAxis, ui->TISEPlot1D->yAxis2);
    pot1Dpen.setColor(QColor(pot1DpenR, pot1DpenG, pot1DpenB));
    pot1Dpen.setWidthF(pot1DpenLw);
    ui->TISEPlot1D->graph(0)->setPen(pot1Dpen);
    ui->TISEPlot1D->graph(0)->setLineStyle(QCPGraph::lsLine);
    ui->TISEPlot1D->graph(0)->setPen(QPen(pot1Dpen));
    ui->TISEPlot1D->graph(0)->setName("Potential Energy");

    QVector<double> X(vec2qvec(Pot1D.getPos()));
    QVector<double> Y(vec2qvec(Pot1D.getPot()));

    ui->TISEPlot1D->graph(0)->setData(X, Y);

    // add new wavefunctions
    std::pair<std::vector<double>, std::vector<std::vector<double>>> eig(solveEigen(prQuNum, Pot1D, 1, 0.5));
    std::vector<double> evals = eig.first;
    std::vector<std::vector<double>> evects = eig.second;
    for (int i = 0; i < evals.size(); i++) {
        ui->TISEPlot1D->addGraph(ui->TISEPlot1D->xAxis, ui->TISEPlot1D->yAxis);
        ui->TISEPlot1D->graph(i + 1)->setLineStyle(QCPGraph::lsLine);
        std::string legendText = "Wavefunction (n = " + std::to_string(i + 1) + ")";
        ui->TISEPlot1D->graph(i + 1)->setName(QString::fromStdString(legendText));

        QVector<double> X(vec2qvec(Pot1D.getPos()));
        QVector<double> Y(vec2qvec(evects[i]));

        ui->TISEPlot1D->graph(i + 1)->setData(X, Y);
    }

    ui->TISEPlot1D->replot();
    ui->TISEPlot1D->update();
}


void TISEMainWindow::on_checkBox_8_stateChanged(int arg1)
{
    upToPr = (ui->checkBox_8->isChecked());
}

