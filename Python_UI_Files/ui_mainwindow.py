# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDial
################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget, QMessageBox, QStyle, QDialog)


# main window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 900)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.aboutApp = QPushButton(self.centralwidget)
        self.aboutApp.setObjectName(u"aboutApp")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutApp.sizePolicy().hasHeightForWidth())
        self.aboutApp.setSizePolicy(sizePolicy)
        self.aboutApp.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.aboutApp)

        self.aboutQt = QPushButton(self.centralwidget)
        self.aboutQt.setObjectName(u"aboutQt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.aboutQt.sizePolicy().hasHeightForWidth())
        self.aboutQt.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.aboutQt)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tise = QWidget()
        self.tise.setObjectName(u"tise")
        self.verticalLayout_5 = QVBoxLayout(self.tise)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.tise)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.startTise = QPushButton(self.tise)
        self.startTise.setObjectName(u"startTise")
        sizePolicy.setHeightForWidth(self.startTise.sizePolicy().hasHeightForWidth())
        self.startTise.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.startTise, 0, 1, 1, 1)

        self.tiseInfo = QPushButton(self.tise)
        self.tiseInfo.setObjectName(u"tiseInfo")
        sizePolicy1.setHeightForWidth(self.tiseInfo.sizePolicy().hasHeightForWidth())
        self.tiseInfo.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.tiseInfo, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tise, "")
        self.tdse = QWidget()
        self.tdse.setObjectName(u"tdse")
        self.verticalLayout_7 = QVBoxLayout(self.tdse)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.tdse)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.startTdse = QPushButton(self.tdse)
        self.startTdse.setObjectName(u"startTdse")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.startTdse.sizePolicy().hasHeightForWidth())
        self.startTdse.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.startTdse, 0, 1, 1, 1)

        self.tdseInfo = QPushButton(self.tdse)
        self.tdseInfo.setObjectName(u"tdseInfo")

        self.gridLayout_3.addWidget(self.tdseInfo, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_3)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.tdse, "")
        self.measurement = QWidget()
        self.measurement.setObjectName(u"measurement")
        self.tabWidget.addTab(self.measurement, "")
        self.twoparticles = QWidget()
        self.twoparticles.setObjectName(u"twoparticles")
        self.tabWidget.addTab(self.twoparticles, "")
        self.fourieranalysis = QWidget()
        self.fourieranalysis.setObjectName(u"fourieranalysis")
        self.tabWidget.addTab(self.fourieranalysis, "")
        self.hilbertspaces = QWidget()
        self.hilbertspaces.setObjectName(u"hilbertspaces")
        self.tabWidget.addTab(self.hilbertspaces, "")
        self.samplesimulations = QWidget()
        self.samplesimulations.setObjectName(u"samplesimulations")
        self.tabWidget.addTab(self.samplesimulations, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 5)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 975, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)


        ''' WIDGET FUNCTIONALITY '''
        # aboutApp
        self.aboutApp.clicked.connect(self.aboutAppClicked)

        # aboutQt
        self.aboutQt.clicked.connect(self.aboutQtClicked)


    ''' CONNECT FUNCTIONS '''
    # aboutQtClicked
    def aboutQtClicked(self):
        QMessageBox().aboutQt(None, "About Qt")

    # aboutAppClicked
    def aboutAppClicked(self):
        QMessageBox().about(None, "About Quantum Sandbox", "TEXT")


    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Quantum\n"
"Sandbox", None))
        self.aboutApp.setText(QCoreApplication.translate("MainWindow", u"About This App", None))
        self.aboutQt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"About Eigen", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"About MuParser", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"A toolbox for studying the Time-Independent Schrodinger Equation (TISE).", None))
        self.startTise.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.tiseInfo.setText(QCoreApplication.translate("MainWindow", u"More Information", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tise), QCoreApplication.translate("MainWindow", u"TISE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"A toolbox for studying the Time-Dependent Schrodinger Equation (TDSE).", None))
        self.startTdse.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.tdseInfo.setText(QCoreApplication.translate("MainWindow", u"More Information", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tdse), QCoreApplication.translate("MainWindow", u"TDSE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.measurement), QCoreApplication.translate("MainWindow", u"Measurement", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.twoparticles), QCoreApplication.translate("MainWindow", u"Two Particles", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fourieranalysis), QCoreApplication.translate("MainWindow", u"Fourier Analysis", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hilbertspaces), QCoreApplication.translate("MainWindow", u"Hilbert Spaces", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.samplesimulations), QCoreApplication.translate("MainWindow", u"Sample Simulations", None))
    # retranslateUi

