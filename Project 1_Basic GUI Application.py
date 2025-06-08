import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):         # constructor
        super().__init__()      # to pass arg to parent use superclass
        self.setGeometry(1300, 850, 900, 800) # x, y coordinates on window, width, height of window

        label = QLabel("Hello", self)
        label.setFont(QFont("Sans Serif", 20))
        label.setGeometry(0, 0, 890, 150)
        label.setStyleSheet("color: #6e654f;"
                            "background: #61c4f2;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        #label.setAlignment(Qt.AlignTop) # vertically top
        #label.setAlignment(Qt.AlignBottom)  # vertically Bottom
        #label.setAlignment(Qt.AlignVCenter)  # vertically center

        #label.setAlignment(Qt.AlignRight)  # horizontally right
        #label.setAlignment(Qt.AlignHCenter)  # horizontally center
        #label.setAlignment(Qt.AlignLeft)  # horizontally left

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)  # center & top
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)  # center & bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # | or operator Center
        #shortcut for center alignment
        label.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()  #default behavior is to hide it
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()