#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "tisemainwindow.h"
#include "tdsemainwindow.h"
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_aboutApp_clicked()
{
    QMessageBox::about(this, "About Quantum Sandbox", "");
}

void MainWindow::on_aboutQt_clicked()
{
    QMessageBox::aboutQt(this, "About Qt");
}

void MainWindow::on_startTise_clicked()
{
    TISEMainWindow tiseMainWindow;
    tiseMainWindow.setModal(true);
    tiseMainWindow.exec();
}

void MainWindow::on_startTdse_clicked()
{
    TDSEMainWindow tdseMainWindow;
    tdseMainWindow.setModal(true);
    tdseMainWindow.exec();
}

