import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import QFile
from Python_UI_Files.ui_mainwindow import Ui_MainWindow

from Python_UI_Files.ui_tisemainwindow import Ui_TISEMainWindow

# secondary windows
class TISEMainWindow(QDialog):
    def __init__(self):
        super(TISEMainWindow, self).__init__()
        self.setWindowTitle("Time-Independent Schrodinger Equation")
        self.ui = Ui_TISEMainWindow()
        self.ui.setupUi(self)

# main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Quantum Sandbox")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # windows
        self.tiseWindow = None

        # start windows
        self.ui.startTise.clicked.connect(self.startTiseClicked)

    # "open window" functions:
    def startTiseClicked(self):
        if self.tiseWindow is None or not self.tiseWindow.isVisible():
            self.tiseWindow = TISEMainWindow()
            self.tiseWindow.ui.tabDSelect.setCurrentIndex(0)
            self.tiseWindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())