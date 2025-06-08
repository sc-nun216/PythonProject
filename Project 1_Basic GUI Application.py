import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):         
        super().__init__()     
        self.setGeometry(1300, 850, 900, 800) 

        label = QLabel("Hello", self)
        label.setFont(QFont("Sans Serif", 20))
        label.setGeometry(0, 0, 890, 150)
        label.setStyleSheet("color: #6e654f;"
                            "background: #61c4f2;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()  
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
