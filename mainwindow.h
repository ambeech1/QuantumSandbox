#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_aboutQt_clicked();

    void on_aboutApp_clicked();

    void on_startTise_clicked();

    void on_startTdse_clicked();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
