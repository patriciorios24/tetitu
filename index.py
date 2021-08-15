import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMainWindow


class ejeplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("tik.ui", self)


if "x" == "x":
    app = QApplication(sys.argv)
    GUI = ejeplo_GUI()
    GUI.show()
    sys.exit(app.exec_())


# if __name__ == "ejemplo_GUI":
#    app = QApplication(sys.argv)
#    GUI = ejeplo_GUI()
#    GUI.show()
#   sys.exit(app.exec_())
