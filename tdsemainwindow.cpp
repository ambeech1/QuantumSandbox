#include "tdsemainwindow.h"
#include "ui_tdsemainwindow.h"

TDSEMainWindow::TDSEMainWindow(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::TDSEMainWindow)
{
    ui->setupUi(this);
}

TDSEMainWindow::~TDSEMainWindow()
{
    delete ui;
}
