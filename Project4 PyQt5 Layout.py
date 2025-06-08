# PyQt5 Layouts

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):         # constructor
        super().__init__()      # to pass arg to parent use superclass
        self.setGeometry(1300, 850, 900, 800) # x, y coordinates on window, width, height of window
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("No.1", self)
        label2 = QLabel("No.2", self)
        label3 = QLabel("No.3", self)
        label4 = QLabel("No.4", self)
        label5 = QLabel("No.5", self)

        label1.setStyleSheet("background-color: #ed8e87;")
        label2.setStyleSheet("background-color: #8da1f0;")
        label3.setStyleSheet("background-color: #e8e890;")
        label4.setStyleSheet("background-color: #7ed9ab;")
        label5.setStyleSheet("background-color: #f0c195;")

        # Vertical Layout
        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget.setLayout(vbox)

        #Horizontal Layout
        hbox = QHBoxLayout()

        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)

        central_widget.setLayout(hbox)

        grid = QGridLayout()

        grid.addWidget(label1, 0, 0)  #specific row and column
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 1, 2)

        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()  #default behavior is to hide it
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()