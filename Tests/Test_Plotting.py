import pyqtgraph as pg
from PySide6.QtWidgets import QApplication, QMainWindow
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Temperature vs time plot
        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)
        x = np.linspace(-1, 1, 501)
        y1 = np.sin(x)
        y2 = np.cos(x)
        A = self.plot_graph.plot(x, y1, name = "Sine")
        B = self.plot_graph.plot(x, y2, name = "Cosine")

        A.clear() # use this command to remove a curve
        B.setData(x, np.exp(y2 ** 100)) # use this command to edit a curve



app = QApplication([])
main = MainWindow()
main.show()
app.exec()