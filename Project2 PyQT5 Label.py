
# PyQt5 Labels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):         # constructor
        super().__init__()      # to pass arg to parent use superclass
        self.setWindowTitle("Cool first GUI")
        self.setGeometry(1300, 850, 900, 800) # x, y coordinates on window, width, height of window
        self.setWindowIcon(QIcon("project_GUI.jpg"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()  #default behavior is to hide it
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()