import PyQt6.QtWidgets as qw
import PyQt6.QtCore as qc
from PyQt6.QtGui import QFont, QIcon

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

class MainWindow(qw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kinematics")
        self.setFixedSize(400, 400)
        self.setWindowIcon(QIcon("Kinematics\\img1.jpg"))

        self.title = qw.QLabel("Simulation Parameters")
        f = QFont("JetBrains Mono", 16, QFont.Weight.Bold)
        self.title.setFont(f)
        self.title.setAlignment(qc.Qt.AlignmentFlag.AlignCenter)

        self.time = TimeDetails()

        self.a = OtherDetails("Acceleration (constant):")
        self.u = OtherDetails("Initial Velcoity:")
        self.x0 = OtherDetails("Starting displacement:")

        self.submit = qw.QPushButton("Visualize")
        self.submit.setFixedWidth(120)

        layout = qw.QVBoxLayout()
        layout.setSpacing(10)  # Set spacing between widgets
        layout.setContentsMargins(15, 15, 15, 15)  # Set margins around the layout
        layout.addWidget(self.title)
        layout.addWidget(self.time)
        layout.addWidget(self.a)
        layout.addWidget(self.u)
        layout.addWidget(self.x0)
        layout.addWidget(self.submit, alignment=qc.Qt.AlignmentFlag.AlignCenter)
        
        container = qw.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

class MotionPlotter(qw.QWidget):
    pass

app = qw.QApplication([])
window = MainWindow()
window.show()
app.exec()
