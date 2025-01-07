#ifndef TISEMAINWINDOW_H
#define TISEMAINWINDOW_H

#include <QDialog>

namespace Ui {
class TISEMainWindow;
}

class TISEMainWindow : public QDialog
{
    Q_OBJECT

public:
    explicit TISEMainWindow(QWidget *parent = nullptr);
    ~TISEMainWindow();

protected:
    virtual void resizeEvent(QResizeEvent *);

private slots:
    void on_tise1DTabInfo_clicked();

    void on_pushButton_2_clicked();

    void on_xmin_textChanged(const QString &arg1);

    void on_xmax_textChanged(const QString &arg1);

    void on_ymin_textChanged(const QString &arg1);

    void on_ymax_textChanged(const QString &arg1);

    void on_autoRange1d_clicked();

    void on_yminR_textChanged(const QString &arg1);

    void on_ymaxR_textChanged(const QString &arg1);

    void on_showAxisLabels_stateChanged(int arg1);

    void on_showLegend_stateChanged(int arg1);

    void on_showGrid_stateChanged(int arg1);

    void on_showAxes_stateChanged(int arg1);

    void on_showXTicks_stateChanged(int arg1);

    void on_showYTicksL_stateChanged(int arg1);

    void on_showYTicksR_stateChanged(int arg1);

    void on_pushButton_clicked();

    void on_xmin_2_textChanged(const QString &arg1);

    void on_xmax_2_textChanged(const QString &arg1);

    void on_ymin_2_textChanged(const QString &arg1);

    void on_ymax_2_textChanged(const QString &arg1);

    void on_autoRange1d_2_clicked();

    void on_showAxisLabels_2_stateChanged(int arg1);

    void on_showColormap_stateChanged(int arg1);

    void on_showTicks_stateChanged(int arg1);

    void on_lineEdit_8_textChanged(const QString &arg1);

    void on_infWel_clicked();

    void on_fWell_clicked();

    void on_barrier_clicked();

    void on_quad_clicked();

    void on_R_textChanged(const QString &arg1);

    void on_G_textChanged(const QString &arg1);

    void on_B_textChanged(const QString &arg1);

    void on_curveWidth_textChanged(const QString &arg1);

    void on_xMinSol_textChanged(const QString &arg1);

    void on_xMaxSol_textChanged(const QString &arg1);

    void on_posStep_textChanged(const QString &arg1);

    void on_prQuNum_textChanged(const QString &arg1);

    void on_computeSol_clicked();

    void on_checkBox_8_stateChanged(int arg1);

private:
    Ui::TISEMainWindow *ui;
};

#endif // TISEMAINWINDOW_H
