import PyQt6.QtWidgets as qw
import PyQt6.QtCore as qc
from PyQt6.QtGui import QFont, QIcon
import pyqtgraph as pg
import numpy as np

class TimeDetails(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.ts = qw.QDoubleSpinBox()
        self.te = qw.QDoubleSpinBox()
        self.t_step = qw.QDoubleSpinBox()

        self.ts.setButtonSymbols(qw.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.te.setButtonSymbols(qw.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.t_step.setButtonSymbols(qw.QAbstractSpinBox.ButtonSymbols.NoButtons)

        layout = qw.QHBoxLayout()
        layout.addWidget(qw.QLabel("Start time:"))
        layout.addWidget(self.ts)
        layout.addWidget(qw.QLabel("End time:"))
        layout.addWidget(self.te)
        layout.addWidget(qw.QLabel("Step size:"))
        layout.addWidget(self.t_step)

        self.setLayout(layout)

class OtherDetails(qw.QWidget):
    def __init__(self, title="Title"):
        super().__init__()
        self.t1 = qw.QLabel(text=title)
        self.w1 = qw.QDoubleSpinBox()

        self.w1.setButtonSymbols(qw.QAbstractSpinBox.ButtonSymbols.NoButtons)
        
        layout = qw.QHBoxLayout()
        layout.addWidget(self.t1)
        layout.addWidget(self.w1)

        self.setLayout(layout)

class MotionPlotter(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.ts, self.te, self.t_step, self.a, self.u, self.x0 = 0, 0, 0, 0, 0, 0

        self.setWindowTitle("Motion Plot")
        self.setGeometry(100, 100, 600, 400)

        layout = qw.QVBoxLayout()
        self.setLayout(layout)

        self.p1 = pg.PlotWidget(title="Displacement vs Time")
        self.p2 = pg.PlotWidget(title="Velocity vs Time")

        layout.addWidget(self.p1)
        layout.addWidget(self.p2)

    def initialize(self, v1, v2, v3, v4, v5, v6):
        self.ts, self.te, self.t_step = v1, v2, v3
        self.a, self.u, self.x0 = v4, v5, v6
        self.plotMotion()

    def plotMotion(self):
        t = np.arange(self.ts, self.te, self.t_step)

        v = self.u + self.a * t
        x = self.x0 + self.u * t + 0.5 * self.a * t ** 2

        self.p1.plotItem.clear()
        self.p2.plotItem.clear()

        self.p1.plotItem.plot(t, x, pen=pg.mkPen(color='r', width=2), name="Displacement")
        self.p1.setLabel('left', 'Displacement (m)')
        self.p1.setLabel('bottom', 'Time (s)')
        self.p1.plotItem.showGrid(x=True, y=True)

        self.p2.plotItem.plot(t, v, pen=pg.mkPen(color='b', width=2), name="Velocity")
        self.p2.setLabel('left', 'Velocity (m/s)')
        self.p2.setLabel('bottom', 'Time (s)')
        self.p2.plotItem.showGrid(x=True, y=True)

class MainWindow(qw.QMainWindow):
    params = qc.pyqtSignal(float, float, float, float, float, float)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kinematics")
        self.setFixedSize(400, 400)
        self.setWindowIcon(QIcon("Kinematics\\img1.jpg"))  # Optional: adjust path or comment if no icon

        self.title = qw.QLabel("Simulation Parameters")
        f = QFont("JetBrains Mono", 16, QFont.Weight.Bold)
        self.title.setFont(f)
        self.title.setAlignment(qc.Qt.AlignmentFlag.AlignCenter)

        self.time = TimeDetails()
        self.a = OtherDetails("Acceleration (constant):")
        self.u = OtherDetails("Initial Velocity:")
        self.x0 = OtherDetails("Starting Displacement:")

        self.submit = qw.QPushButton("Visualize")
        self.submit.setFixedWidth(120)
        self.submit.clicked.connect(self.sendParams)

        layout = qw.QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.addWidget(self.title)
        layout.addWidget(self.time)
        layout.addWidget(self.a)
        layout.addWidget(self.u)
        layout.addWidget(self.x0)
        layout.addWidget(self.submit, alignment=qc.Qt.AlignmentFlag.AlignCenter)

        container = qw.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.motion_plot = MotionPlotter()
        self.params.connect(self.motion_plot.initialize)

    def sendParams(self):
        v1 = self.time.ts.value()
        v2 = self.time.te.value()
        v3 = self.time.t_step.value()
        v4 = self.a.w1.value()
        v5 = self.u.w1.value()
        v6 = self.x0.w1.value()

        self.params.emit(v1, v2, v3, v4, v5, v6)
        self.motion_plot.show()


if __name__ == "__main__":
    app = qw.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
