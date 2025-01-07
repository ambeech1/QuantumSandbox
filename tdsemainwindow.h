#ifndef TDSEMAINWINDOW_H
#define TDSEMAINWINDOW_H

#include <QDialog>

namespace Ui {
class TDSEMainWindow;
}

class TDSEMainWindow : public QDialog
{
    Q_OBJECT

public:
    explicit TDSEMainWindow(QWidget *parent = nullptr);
    ~TDSEMainWindow();

private:
    Ui::TDSEMainWindow *ui;
};

#endif // TDSEMAINWINDOW_H
