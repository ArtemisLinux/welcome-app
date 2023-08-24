## Artemis OS Welcome
## Maintained by: Frazer Grant
## Version: 0.1



## Modules to import ##
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import *





## Main Window ##
class MainUI(QDialog):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("dev.ui", self)
        width = 160
        height = 130
        self.setFixedSize(width, height)

## Buttons ##
        self.close.clicked.connect(QCoreApplication.instance().quit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setDesktopFileName("artemisos-welcome-app")    #
    ui = MainUI()
    ui.show()
    app.exec_()




