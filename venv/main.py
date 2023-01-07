import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from welcome_page import *



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    From = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(From)
    From.show()
    sys.exit(app.exec_())