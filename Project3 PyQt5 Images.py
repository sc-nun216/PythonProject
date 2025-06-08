# PyQt5 Images

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):         # constructor
        super().__init__()      # to pass arg to parent use superclass
        self.setGeometry(1300, 850, 900, 800) # x, y coordinates on window, width, height of window

        label = QLabel(self)  #self refers to window object
        label.setGeometry(0, 0, 550, 400)

        pixmap = QPixmap("project_GUI.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True) # takes the height and width of window

        #center positioning
        label.setGeometry((self.width() - label.width()) //2,
                          (self.height() - label.height()) //2,
                          label.width(), label.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()  #default behavior is to hide it
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()