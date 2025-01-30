# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tisemainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_TISEMainWindow(object):
    def setupUi(self, TISEMainWindow):
        if not TISEMainWindow.objectName():
            TISEMainWindow.setObjectName(u"TISEMainWindow")
        TISEMainWindow.resize(1309, 894)
        self.verticalLayout_11 = QVBoxLayout(TISEMainWindow)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tabDSelect = QTabWidget(TISEMainWindow)
        self.tabDSelect.setObjectName(u"tabDSelect")
        self.oneD = QWidget()
        self.oneD.setObjectName(u"oneD")
        self.verticalLayout_12 = QVBoxLayout(self.oneD)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.label = QLabel(self.oneD)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tise1DTabInfo = QPushButton(self.oneD)
        self.tise1DTabInfo.setObjectName(u"tise1DTabInfo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tise1DTabInfo.sizePolicy().hasHeightForWidth())
        self.tise1DTabInfo.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.tise1DTabInfo)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(4, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TISEPlot1D = PlotWidget()
        self.TISEPlot1D.setObjectName(u"TISEPlot1D")
        self.verticalLayout_8 = QVBoxLayout(self.TISEPlot1D)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.verticalLayout.addWidget(self.TISEPlot1D)

        self.tabs1d = QTabWidget(self.oneD)
        self.tabs1d.setObjectName(u"tabs1d")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabs1d.sizePolicy().hasHeightForWidth())
        self.tabs1d.setSizePolicy(sizePolicy1)
        self.plotsettings = QWidget()
        self.plotsettings.setObjectName(u"plotsettings")
        self.verticalLayout_9 = QVBoxLayout(self.plotsettings)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_5 = QLabel(self.plotsettings)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.ymin = QLineEdit(self.plotsettings)
        self.ymin.setObjectName(u"ymin")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.ymin)

        self.label_6 = QLabel(self.plotsettings)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.ymax = QLineEdit(self.plotsettings)
        self.ymax.setObjectName(u"ymax")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.ymax)


        self.gridLayout.addLayout(self.formLayout_4, 1, 0, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_2 = QLabel(self.plotsettings)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.xmin = QLineEdit(self.plotsettings)
        self.xmin.setObjectName(u"xmin")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.xmin)

        self.label_4 = QLabel(self.plotsettings)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.xmax = QLineEdit(self.plotsettings)
        self.xmax.setObjectName(u"xmax")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.xmax)


        self.gridLayout.addLayout(self.formLayout_3, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_10 = QLabel(self.plotsettings)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.yminR = QLineEdit(self.plotsettings)
        self.yminR.setObjectName(u"yminR")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.yminR)

        self.label_11 = QLabel(self.plotsettings)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.ymaxR = QLineEdit(self.plotsettings)
        self.ymaxR.setObjectName(u"ymaxR")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ymaxR)


        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)

        self.autoRange1d = QPushButton(self.plotsettings)
        self.autoRange1d.setObjectName(u"autoRange1d")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.autoRange1d.sizePolicy().hasHeightForWidth())
        self.autoRange1d.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.autoRange1d, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnMinimumWidth(1, 1)

        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.showAxisLabels = QCheckBox(self.plotsettings)
        self.showAxisLabels.setObjectName(u"showAxisLabels")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.showAxisLabels.sizePolicy().hasHeightForWidth())
        self.showAxisLabels.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.showAxisLabels)

        self.showAxes = QCheckBox(self.plotsettings)
        self.showAxes.setObjectName(u"showAxes")
        sizePolicy3.setHeightForWidth(self.showAxes.sizePolicy().hasHeightForWidth())
        self.showAxes.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.showAxes)

        self.showGrid = QCheckBox(self.plotsettings)
        self.showGrid.setObjectName(u"showGrid")
        sizePolicy3.setHeightForWidth(self.showGrid.sizePolicy().hasHeightForWidth())
        self.showGrid.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.showGrid)

        self.showLegend = QCheckBox(self.plotsettings)
        self.showLegend.setObjectName(u"showLegend")
        sizePolicy3.setHeightForWidth(self.showLegend.sizePolicy().hasHeightForWidth())
        self.showLegend.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.showLegend)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.showXTicks = QCheckBox(self.plotsettings)
        self.showXTicks.setObjectName(u"showXTicks")

        self.verticalLayout_10.addWidget(self.showXTicks)

        self.showYTicksL = QCheckBox(self.plotsettings)
        self.showYTicksL.setObjectName(u"showYTicksL")

        self.verticalLayout_10.addWidget(self.showYTicksL)

        self.showYTicksR = QCheckBox(self.plotsettings)
        self.showYTicksR.setObjectName(u"showYTicksR")

        self.verticalLayout_10.addWidget(self.showYTicksR)

        self.pushButton = QPushButton(self.plotsettings)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_10.addWidget(self.pushButton)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)

        self.scrollArea = QScrollArea(self.plotsettings)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 304, 123))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 2)

        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.tabs1d.addTab(self.plotsettings, "")
        self.potentialenergy = QWidget()
        self.potentialenergy.setObjectName(u"potentialenergy")
        self.horizontalLayout_4 = QHBoxLayout(self.potentialenergy)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_8 = QLabel(self.potentialenergy)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_8)

        self.lineEdit = QLineEdit(self.potentialenergy)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.lineEdit)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 4)

        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.TISEPotSyntax = QPushButton(self.potentialenergy)
        self.TISEPotSyntax.setObjectName(u"TISEPotSyntax")
        sizePolicy1.setHeightForWidth(self.TISEPotSyntax.sizePolicy().hasHeightForWidth())
        self.TISEPotSyntax.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.TISEPotSyntax)

        self.verticalLayout_4.setStretch(0, 3)
        self.verticalLayout_4.setStretch(1, 1)

        self.horizontalLayout_11.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 2)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_11)

        self.tabs1d.addTab(self.potentialenergy, "")
        self.solutionparameters = QWidget()
        self.solutionparameters.setObjectName(u"solutionparameters")
        self.verticalLayout_15 = QVBoxLayout(self.solutionparameters)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.formLayout_16 = QFormLayout()
        self.formLayout_16.setObjectName(u"formLayout_16")
        self.formLayout_16.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_27 = QLabel(self.solutionparameters)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_16.setWidget(0, QFormLayout.LabelRole, self.label_27)

        self.label_28 = QLabel(self.solutionparameters)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_16.setWidget(1, QFormLayout.LabelRole, self.label_28)

        self.xMinSol = QLineEdit(self.solutionparameters)
        self.xMinSol.setObjectName(u"xMinSol")

        self.formLayout_16.setWidget(0, QFormLayout.FieldRole, self.xMinSol)

        self.xMaxSol = QLineEdit(self.solutionparameters)
        self.xMaxSol.setObjectName(u"xMaxSol")

        self.formLayout_16.setWidget(1, QFormLayout.FieldRole, self.xMaxSol)


        self.horizontalLayout_5.addLayout(self.formLayout_16)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_7 = QLabel(self.solutionparameters)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.posStep = QLineEdit(self.solutionparameters)
        self.posStep.setObjectName(u"posStep")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.posStep)

        self.label_13 = QLabel(self.solutionparameters)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.prQuNum = QLineEdit(self.solutionparameters)
        self.prQuNum.setObjectName(u"prQuNum")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.prQuNum)

        self.checkBox_8 = QCheckBox(self.solutionparameters)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.formLayout_7.setWidget(2, QFormLayout.SpanningRole, self.checkBox_8)


        self.horizontalLayout_5.addLayout(self.formLayout_7)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.computeSol = QPushButton(self.solutionparameters)
        self.computeSol.setObjectName(u"computeSol")
        sizePolicy.setHeightForWidth(self.computeSol.sizePolicy().hasHeightForWidth())
        self.computeSol.setSizePolicy(sizePolicy)

        self.verticalLayout_14.addWidget(self.computeSol)

        self.progressBar = QProgressBar(self.solutionparameters)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy4)
        self.progressBar.setValue(24)

        self.verticalLayout_14.addWidget(self.progressBar)


        self.horizontalLayout_5.addLayout(self.verticalLayout_14)

        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout_15.addLayout(self.horizontalLayout_5)

        self.tabs1d.addTab(self.solutionparameters, "")
        self.display = QWidget()
        self.display.setObjectName(u"display")
        self.verticalLayout_18 = QVBoxLayout(self.display)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.radioButton_9 = QRadioButton(self.display)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.verticalLayout_16.addWidget(self.radioButton_9)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_9 = QCheckBox(self.display)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout_2.addWidget(self.checkBox_9, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.checkBox_10 = QCheckBox(self.display)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout_2.addWidget(self.checkBox_10, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 3)

        self.verticalLayout_16.addLayout(self.gridLayout_2)

        self.radioButton_10 = QRadioButton(self.display)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.verticalLayout_16.addWidget(self.radioButton_10)


        self.horizontalLayout_6.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.checkBox_11 = QCheckBox(self.display)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.verticalLayout_17.addWidget(self.checkBox_11)

        self.checkBox_12 = QCheckBox(self.display)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.verticalLayout_17.addWidget(self.checkBox_12)

        self.checkBox_13 = QCheckBox(self.display)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.verticalLayout_17.addWidget(self.checkBox_13)


        self.horizontalLayout_6.addLayout(self.verticalLayout_17)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_18.addLayout(self.horizontalLayout_6)

        self.tabs1d.addTab(self.display, "")
        self.managesolutions = QWidget()
        self.managesolutions.setObjectName(u"managesolutions")
        self.tabs1d.addTab(self.managesolutions, "")

        self.verticalLayout.addWidget(self.tabs1d)

        self.verticalLayout.setStretch(0, 7)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

        self.verticalLayout_12.addLayout(self.horizontalLayout)

        self.tabDSelect.addTab(self.oneD, "")
        self.twoD = QWidget()
        self.twoD.setObjectName(u"twoD")
        self.verticalLayout_7 = QVBoxLayout(self.twoD)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.label_3 = QLabel(self.twoD)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_3)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.pushButton_2 = QPushButton(self.twoD)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.pushButton_2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 4)
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_5.setStretch(3, 2)
        self.verticalLayout_5.setStretch(4, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.TISEPlot2D = QWidget(self.twoD)
        self.TISEPlot2D.setObjectName(u"TISEPlot2D")
        self.TISEPlot2D.setEnabled(True)
        self.TISEPlot2D.setMinimumSize(QSize(0, 0))

        self.verticalLayout_6.addWidget(self.TISEPlot2D)

        self.tabs2d = QTabWidget(self.twoD)
        self.tabs2d.setObjectName(u"tabs2d")
        sizePolicy1.setHeightForWidth(self.tabs2d.sizePolicy().hasHeightForWidth())
        self.tabs2d.setSizePolicy(sizePolicy1)
        self.plotsettings_2 = QWidget()
        self.plotsettings_2.setObjectName(u"plotsettings_2")
        self.verticalLayout_21 = QVBoxLayout(self.plotsettings_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_14 = QLabel(self.plotsettings_2)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.ymin_2 = QLineEdit(self.plotsettings_2)
        self.ymin_2.setObjectName(u"ymin_2")

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.ymin_2)

        self.label_15 = QLabel(self.plotsettings_2)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.ymax_2 = QLineEdit(self.plotsettings_2)
        self.ymax_2.setObjectName(u"ymax_2")

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.ymax_2)


        self.gridLayout_3.addLayout(self.formLayout_8, 1, 0, 1, 1)

        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_16 = QLabel(self.plotsettings_2)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.xmin_2 = QLineEdit(self.plotsettings_2)
        self.xmin_2.setObjectName(u"xmin_2")

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.xmin_2)

        self.label_17 = QLabel(self.plotsettings_2)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.label_17)

        self.xmax_2 = QLineEdit(self.plotsettings_2)
        self.xmax_2.setObjectName(u"xmax_2")

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.xmax_2)


        self.gridLayout_3.addLayout(self.formLayout_9, 0, 0, 1, 1)

        self.autoRange1d_2 = QPushButton(self.plotsettings_2)
        self.autoRange1d_2.setObjectName(u"autoRange1d_2")
        sizePolicy2.setHeightForWidth(self.autoRange1d_2.sizePolicy().hasHeightForWidth())
        self.autoRange1d_2.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.autoRange1d_2, 0, 1, 2, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnMinimumWidth(0, 1)
        self.gridLayout_3.setColumnMinimumWidth(1, 1)

        self.horizontalLayout_7.addLayout(self.gridLayout_3)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.showAxisLabels_2 = QCheckBox(self.plotsettings_2)
        self.showAxisLabels_2.setObjectName(u"showAxisLabels_2")

        self.verticalLayout_19.addWidget(self.showAxisLabels_2)

        self.showTicks = QCheckBox(self.plotsettings_2)
        self.showTicks.setObjectName(u"showTicks")

        self.verticalLayout_19.addWidget(self.showTicks)

        self.showColormap = QCheckBox(self.plotsettings_2)
        self.showColormap.setObjectName(u"showColormap")

        self.verticalLayout_19.addWidget(self.showColormap)


        self.horizontalLayout_7.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.lineEdit_8 = QLineEdit(self.plotsettings_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy5)

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_19 = QLabel(self.plotsettings_2)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.label_19)


        self.verticalLayout_20.addLayout(self.formLayout_10)


        self.horizontalLayout_7.addLayout(self.verticalLayout_20)

        self.scrollArea_2 = QScrollArea(self.plotsettings_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 227, 130))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_7.addWidget(self.scrollArea_2)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 2)
        self.horizontalLayout_7.setStretch(3, 2)

        self.verticalLayout_21.addLayout(self.horizontalLayout_7)

        self.tabs2d.addTab(self.plotsettings_2, "")
        self.potentialenergy_2 = QWidget()
        self.potentialenergy_2.setObjectName(u"potentialenergy_2")
        self.horizontalLayout_8 = QHBoxLayout(self.potentialenergy_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.formLayout_11 = QFormLayout()
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.formLayout_11.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_20 = QLabel(self.potentialenergy_2)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.label_20)

        self.lineEdit_2 = QLineEdit(self.potentialenergy_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy5.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy5)

        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.lineEdit_2)

        self.pushButton_5 = QPushButton(self.potentialenergy_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.formLayout_11.setWidget(1, QFormLayout.SpanningRole, self.pushButton_5)


        self.horizontalLayout_8.addLayout(self.formLayout_11)

        self.formLayout_12 = QFormLayout()
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.formLayout_12.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_21 = QLabel(self.potentialenergy_2)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_12.setWidget(0, QFormLayout.LabelRole, self.label_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.radioButton_11 = QRadioButton(self.potentialenergy_2)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.verticalLayout_22.addWidget(self.radioButton_11)

        self.radioButton_12 = QRadioButton(self.potentialenergy_2)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.verticalLayout_22.addWidget(self.radioButton_12)

        self.radioButton_13 = QRadioButton(self.potentialenergy_2)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.verticalLayout_22.addWidget(self.radioButton_13)

        self.radioButton_14 = QRadioButton(self.potentialenergy_2)
        self.radioButton_14.setObjectName(u"radioButton_14")

        self.verticalLayout_22.addWidget(self.radioButton_14)


        self.formLayout_12.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_22)


        self.horizontalLayout_8.addLayout(self.formLayout_12)

        self.formLayout_13 = QFormLayout()
        self.formLayout_13.setObjectName(u"formLayout_13")
        self.formLayout_13.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_22 = QLabel(self.potentialenergy_2)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_13.setWidget(0, QFormLayout.LabelRole, self.label_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.radioButton_15 = QRadioButton(self.potentialenergy_2)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.verticalLayout_23.addWidget(self.radioButton_15)

        self.radioButton_16 = QRadioButton(self.potentialenergy_2)
        self.radioButton_16.setObjectName(u"radioButton_16")

        self.verticalLayout_23.addWidget(self.radioButton_16)

        self.radioButton_17 = QRadioButton(self.potentialenergy_2)
        self.radioButton_17.setObjectName(u"radioButton_17")

        self.verticalLayout_23.addWidget(self.radioButton_17)

        self.radioButton_18 = QRadioButton(self.potentialenergy_2)
        self.radioButton_18.setObjectName(u"radioButton_18")

        self.verticalLayout_23.addWidget(self.radioButton_18)


        self.formLayout_13.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_23)


        self.horizontalLayout_8.addLayout(self.formLayout_13)

        self.tabs2d.addTab(self.potentialenergy_2, "")
        self.solutionparameters_2 = QWidget()
        self.solutionparameters_2.setObjectName(u"solutionparameters_2")
        self.verticalLayout_25 = QVBoxLayout(self.solutionparameters_2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.formLayout_15 = QFormLayout()
        self.formLayout_15.setObjectName(u"formLayout_15")
        self.formLayout_15.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_25 = QLabel(self.solutionparameters_2)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_15.setWidget(0, QFormLayout.LabelRole, self.label_25)

        self.label_26 = QLabel(self.solutionparameters_2)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_15.setWidget(1, QFormLayout.LabelRole, self.label_26)

        self.lineEdit_11 = QLineEdit(self.solutionparameters_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.formLayout_15.setWidget(0, QFormLayout.FieldRole, self.lineEdit_11)

        self.lineEdit_12 = QLineEdit(self.solutionparameters_2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.formLayout_15.setWidget(1, QFormLayout.FieldRole, self.lineEdit_12)

        self.label_29 = QLabel(self.solutionparameters_2)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_15.setWidget(2, QFormLayout.LabelRole, self.label_29)

        self.label_30 = QLabel(self.solutionparameters_2)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_15.setWidget(3, QFormLayout.LabelRole, self.label_30)

        self.lineEdit_13 = QLineEdit(self.solutionparameters_2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.formLayout_15.setWidget(2, QFormLayout.FieldRole, self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.solutionparameters_2)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.formLayout_15.setWidget(3, QFormLayout.FieldRole, self.lineEdit_14)


        self.horizontalLayout_9.addLayout(self.formLayout_15)

        self.formLayout_14 = QFormLayout()
        self.formLayout_14.setObjectName(u"formLayout_14")
        self.formLayout_14.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_23 = QLabel(self.solutionparameters_2)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_14.setWidget(0, QFormLayout.LabelRole, self.label_23)

        self.lineEdit_6 = QLineEdit(self.solutionparameters_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout_14.setWidget(0, QFormLayout.FieldRole, self.lineEdit_6)

        self.label_24 = QLabel(self.solutionparameters_2)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_14.setWidget(2, QFormLayout.LabelRole, self.label_24)

        self.lineEdit_7 = QLineEdit(self.solutionparameters_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout_14.setWidget(2, QFormLayout.FieldRole, self.lineEdit_7)

        self.checkBox_14 = QCheckBox(self.solutionparameters_2)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.formLayout_14.setWidget(3, QFormLayout.SpanningRole, self.checkBox_14)

        self.label_18 = QLabel(self.solutionparameters_2)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_14.setWidget(1, QFormLayout.LabelRole, self.label_18)

        self.lineEdit_3 = QLineEdit(self.solutionparameters_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout_14.setWidget(1, QFormLayout.FieldRole, self.lineEdit_3)


        self.horizontalLayout_9.addLayout(self.formLayout_14)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.updatePlot1d_2 = QPushButton(self.solutionparameters_2)
        self.updatePlot1d_2.setObjectName(u"updatePlot1d_2")
        sizePolicy.setHeightForWidth(self.updatePlot1d_2.sizePolicy().hasHeightForWidth())
        self.updatePlot1d_2.setSizePolicy(sizePolicy)

        self.verticalLayout_24.addWidget(self.updatePlot1d_2)

        self.progressBar_2 = QProgressBar(self.solutionparameters_2)
        self.progressBar_2.setObjectName(u"progressBar_2")
        sizePolicy4.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy4)
        self.progressBar_2.setValue(24)

        self.verticalLayout_24.addWidget(self.progressBar_2)


        self.horizontalLayout_9.addLayout(self.verticalLayout_24)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 1)
        self.horizontalLayout_9.setStretch(3, 2)

        self.verticalLayout_25.addLayout(self.horizontalLayout_9)

        self.tabs2d.addTab(self.solutionparameters_2, "")
        self.display_2 = QWidget()
        self.display_2.setObjectName(u"display_2")
        self.verticalLayout_28 = QVBoxLayout(self.display_2)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.radioButton_19 = QRadioButton(self.display_2)
        self.radioButton_19.setObjectName(u"radioButton_19")

        self.verticalLayout_26.addWidget(self.radioButton_19)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.radioButton_21 = QRadioButton(self.display_2)
        self.radioButton_21.setObjectName(u"radioButton_21")

        self.gridLayout_4.addWidget(self.radioButton_21, 0, 1, 1, 1)

        self.radioButton_22 = QRadioButton(self.display_2)
        self.radioButton_22.setObjectName(u"radioButton_22")

        self.gridLayout_4.addWidget(self.radioButton_22, 1, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 3)

        self.verticalLayout_26.addLayout(self.gridLayout_4)

        self.radioButton_20 = QRadioButton(self.display_2)
        self.radioButton_20.setObjectName(u"radioButton_20")

        self.verticalLayout_26.addWidget(self.radioButton_20)


        self.horizontalLayout_10.addLayout(self.verticalLayout_26)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.checkBox_17 = QCheckBox(self.display_2)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.verticalLayout_27.addWidget(self.checkBox_17)

        self.checkBox_18 = QCheckBox(self.display_2)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.verticalLayout_27.addWidget(self.checkBox_18)

        self.checkBox_19 = QCheckBox(self.display_2)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.verticalLayout_27.addWidget(self.checkBox_19)

        self.checkBox = QCheckBox(self.display_2)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_27.addWidget(self.checkBox)


        self.horizontalLayout_10.addLayout(self.verticalLayout_27)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 2)

        self.verticalLayout_28.addLayout(self.horizontalLayout_10)

        self.tabs2d.addTab(self.display_2, "")
        self.managesolutions_2 = QWidget()
        self.managesolutions_2.setObjectName(u"managesolutions_2")
        self.tabs2d.addTab(self.managesolutions_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabs2d.addTab(self.tab, "")

        self.verticalLayout_6.addWidget(self.tabs2d)

        self.verticalLayout_6.setStretch(0, 5)
        self.verticalLayout_6.setStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.tabDSelect.addTab(self.twoD, "")

        self.verticalLayout_11.addWidget(self.tabDSelect)


        self.retranslateUi(TISEMainWindow)
        self.autoRange1d.clicked.connect(self.ymax.clear)
        self.autoRange1d.clicked.connect(self.ymin.clear)
        self.autoRange1d.clicked.connect(self.xmax.clear)
        self.autoRange1d.clicked.connect(self.xmin.clear)
        self.autoRange1d.clicked.connect(self.yminR.clear)
        self.autoRange1d.clicked.connect(self.ymaxR.clear)

        self.tabDSelect.setCurrentIndex(1)
        self.tabs1d.setCurrentIndex(0)
        self.tabs2d.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TISEMainWindow)
    # setupUi

    def retranslateUi(self, TISEMainWindow):
        TISEMainWindow.setWindowTitle(QCoreApplication.translate("TISEMainWindow", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("TISEMainWindow", u"Time-\n"
"Independent\n"
"Schrodinger\n"
"Equation\n"
"(TISE); 1D", None))
        self.tise1DTabInfo.setText(QCoreApplication.translate("TISEMainWindow", u"More Information on Tabs", None))
        self.label_5.setText(QCoreApplication.translate("TISEMainWindow", u"y Min (Left)", None))
        self.label_6.setText(QCoreApplication.translate("TISEMainWindow", u"y Max (Left)", None))
        self.label_2.setText(QCoreApplication.translate("TISEMainWindow", u"x Min", None))
        self.xmin.setText("")
        self.label_4.setText(QCoreApplication.translate("TISEMainWindow", u"x Max", None))
        self.label_10.setText(QCoreApplication.translate("TISEMainWindow", u"y Min (Right)", None))
        self.label_11.setText(QCoreApplication.translate("TISEMainWindow", u"y Max (Right)", None))
        self.autoRange1d.setText(QCoreApplication.translate("TISEMainWindow", u"Auto Range", None))
        self.showAxisLabels.setText(QCoreApplication.translate("TISEMainWindow", u"Show Axis Labels", None))
        self.showAxes.setText(QCoreApplication.translate("TISEMainWindow", u"Show Axes", None))
        self.showGrid.setText(QCoreApplication.translate("TISEMainWindow", u"Show Grid", None))
        self.showLegend.setText(QCoreApplication.translate("TISEMainWindow", u"Show Legend", None))
        self.showXTicks.setText(QCoreApplication.translate("TISEMainWindow", u"Show x Ticks", None))
        self.showYTicksL.setText(QCoreApplication.translate("TISEMainWindow", u"Show y Ticks (Left)", None))
        self.showYTicksR.setText(QCoreApplication.translate("TISEMainWindow", u"Show y Ticks (Right)", None))
        self.pushButton.setText(QCoreApplication.translate("TISEMainWindow", u"Move Legend", None))
        self.tabs1d.setTabText(self.tabs1d.indexOf(self.plotsettings), QCoreApplication.translate("TISEMainWindow", u"Plot Settings", None))
        self.label_8.setText(QCoreApplication.translate("TISEMainWindow", u"Potential\n"
"Energy\n"
"Function", None))
        self.TISEPotSyntax.setText(QCoreApplication.translate("TISEMainWindow", u"Syntax Information", None))
        self.tabs1d.setTabText(self.tabs1d.indexOf(self.potentialenergy), QCoreApplication.translate("TISEMainWindow", u"Potential Energy", None))
        self.label_27.setText(QCoreApplication.translate("TISEMainWindow", u"x Min", None))
        self.label_28.setText(QCoreApplication.translate("TISEMainWindow", u"x Max", None))
        self.label_7.setText(QCoreApplication.translate("TISEMainWindow", u"Number of Position Steps", None))
        self.label_13.setText(QCoreApplication.translate("TISEMainWindow", u"Principal Quantum Number", None))
        self.checkBox_8.setText(QCoreApplication.translate("TISEMainWindow", u"Calculate Up To Principal Quantum Number", None))
        self.computeSol.setText(QCoreApplication.translate("TISEMainWindow", u"Compute Solution", None))
        self.tabs1d.setTabText(self.tabs1d.indexOf(self.solutionparameters), QCoreApplication.translate("TISEMainWindow", u"Solution Parameters", None))
        self.radioButton_9.setText(QCoreApplication.translate("TISEMainWindow", u"Probability Amplitude", None))
        self.checkBox_9.setText(QCoreApplication.translate("TISEMainWindow", u"Real", None))
        self.checkBox_10.setText(QCoreApplication.translate("TISEMainWindow", u"Imaginary", None))
        self.radioButton_10.setText(QCoreApplication.translate("TISEMainWindow", u"Probability Density", None))
        self.checkBox_11.setText(QCoreApplication.translate("TISEMainWindow", u"Position Expectation", None))
        self.checkBox_12.setText(QCoreApplication.translate("TISEMainWindow", u"Velocity Expectation", None))
        self.checkBox_13.setText(QCoreApplication.translate("TISEMainWindow", u"Momentum Expectation", None))
        self.tabs1d.setTabText(self.tabs1d.indexOf(self.display), QCoreApplication.translate("TISEMainWindow", u"Display", None))
        self.tabs1d.setTabText(self.tabs1d.indexOf(self.managesolutions), QCoreApplication.translate("TISEMainWindow", u"Manage Solutions", None))
        self.tabDSelect.setTabText(self.tabDSelect.indexOf(self.oneD), QCoreApplication.translate("TISEMainWindow", u"1D", None))
        self.label_3.setText(QCoreApplication.translate("TISEMainWindow", u"Time-\n"
"Independent\n"
"Schrodinger\n"
"Equation\n"
"(TISE); 2D", None))
        self.pushButton_2.setText(QCoreApplication.translate("TISEMainWindow", u"More Information on Tabs", None))
        self.label_14.setText(QCoreApplication.translate("TISEMainWindow", u"y Min", None))
        self.label_15.setText(QCoreApplication.translate("TISEMainWindow", u"y Max", None))
        self.label_16.setText(QCoreApplication.translate("TISEMainWindow", u"x Min", None))
        self.xmin_2.setText("")
        self.label_17.setText(QCoreApplication.translate("TISEMainWindow", u"x Max", None))
        self.autoRange1d_2.setText(QCoreApplication.translate("TISEMainWindow", u"Auto\n"
"Range", None))
        self.showAxisLabels_2.setText(QCoreApplication.translate("TISEMainWindow", u"Show Axis Labels", None))
        self.showTicks.setText(QCoreApplication.translate("TISEMainWindow", u"Show Ticks", None))
        self.showColormap.setText(QCoreApplication.translate("TISEMainWindow", u"Show Color Map", None))
        self.label_19.setText(QCoreApplication.translate("TISEMainWindow", u"Set\n"
"Aspect\n"
"Ratio", None))
        self.tabs2d.setTabText(self.tabs2d.indexOf(self.plotsettings_2), QCoreApplication.translate("TISEMainWindow", u"Plot Settings", None))
        self.label_20.setText(QCoreApplication.translate("TISEMainWindow", u"Potential\n"
"Energy\n"
"Function", None))
        self.pushButton_5.setText(QCoreApplication.translate("TISEMainWindow", u"Syntax Information", None))
        self.label_21.setText(QCoreApplication.translate("TISEMainWindow", u"Potential\n"
"Energy\n"
"Units", None))
        self.radioButton_11.setText(QCoreApplication.translate("TISEMainWindow", u"Make Dimensionless", None))
        self.radioButton_12.setText(QCoreApplication.translate("TISEMainWindow", u"eV", None))
        self.radioButton_13.setText(QCoreApplication.translate("TISEMainWindow", u"keV", None))
        self.radioButton_14.setText(QCoreApplication.translate("TISEMainWindow", u"MeV", None))
        self.label_22.setText(QCoreApplication.translate("TISEMainWindow", u"Position\n"
"Units", None))
        self.radioButton_15.setText(QCoreApplication.translate("TISEMainWindow", u"Make Dimensionless", None))
        self.radioButton_16.setText(QCoreApplication.translate("TISEMainWindow", u"nm", None))
        self.radioButton_17.setText(QCoreApplication.translate("TISEMainWindow", u"um", None))
        self.radioButton_18.setText(QCoreApplication.translate("TISEMainWindow", u"mm", None))
        self.tabs2d.setTabText(self.tabs2d.indexOf(self.potentialenergy_2), QCoreApplication.translate("TISEMainWindow", u"Potential Energy", None))
        self.label_25.setText(QCoreApplication.translate("TISEMainWindow", u"x Min", None))
        self.label_26.setText(QCoreApplication.translate("TISEMainWindow", u"x Max", None))
        self.label_29.setText(QCoreApplication.translate("TISEMainWindow", u"y Min", None))
        self.label_30.setText(QCoreApplication.translate("TISEMainWindow", u"y Max", None))
        self.label_23.setText(QCoreApplication.translate("TISEMainWindow", u"x Position Step", None))
        self.label_24.setText(QCoreApplication.translate("TISEMainWindow", u"Principal Quantum Number", None))
        self.checkBox_14.setText(QCoreApplication.translate("TISEMainWindow", u"Calculate Up To Principal Quantum Number", None))
        self.label_18.setText(QCoreApplication.translate("TISEMainWindow", u"y Position Step", None))
        self.updatePlot1d_2.setText(QCoreApplication.translate("TISEMainWindow", u"Compute Solution", None))
        self.tabs2d.setTabText(self.tabs2d.indexOf(self.solutionparameters_2), QCoreApplication.translate("TISEMainWindow", u"Solution Parameters", None))
        self.radioButton_19.setText(QCoreApplication.translate("TISEMainWindow", u"Probability Amplitude", None))
        self.radioButton_21.setText(QCoreApplication.translate("TISEMainWindow", u"Real", None))
        self.radioButton_22.setText(QCoreApplication.translate("TISEMainWindow", u"Imaginary", None))
        self.radioButton_20.setText(QCoreApplication.translate("TISEMainWindow", u"Probability Density", None))
        self.checkBox_17.setText(QCoreApplication.translate("TISEMainWindow", u"Position Expectation", None))
        self.checkBox_18.setText(QCoreApplication.translate("TISEMainWindow", u"Velocity Expectation", None))
        self.checkBox_19.setText(QCoreApplication.translate("TISEMainWindow", u"Momentum Expectation", None))
        self.checkBox.setText(QCoreApplication.translate("TISEMainWindow", u"Angular Momentum Expectation", None))
        self.tabs2d.setTabText(self.tabs2d.indexOf(self.display_2), QCoreApplication.translate("TISEMainWindow", u"Display", None))
        self.tabs2d.setTabText(self.tabs2d.indexOf(self.managesolutions_2), QCoreApplication.translate("TISEMainWindow", u"Manage Solutions", None))
        self.tabs2d.setTabText(self.tabs2d.indexOf(self.tab), QCoreApplication.translate("TISEMainWindow", u"Spin Parameters", None))
        self.tabDSelect.setTabText(self.tabDSelect.indexOf(self.twoD), QCoreApplication.translate("TISEMainWindow", u"2D", None))
    # retranslateUi

