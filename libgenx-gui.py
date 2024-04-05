import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtGui import QAction, QIcon

from ui.MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

        spacer = QtWidgets.QWidget()  # spacer for widgets
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

    # TOOLBAR

        # CONFIG
        config_action = QAction(QIcon('ui/configure.svg'), "Configuration", self)
        config_action.triggered.connect(self.config_action)
        self.toolbar.addAction(config_action)

        # <--- left side
        self.toolbar.addWidget(spacer)
        # right side --->

        # ABOUT
        about_action = QAction(QIcon('ui/help-about.svg'), "About", self)
        about_action.triggered.connect(self.about_action)
        self.toolbar.addAction(about_action)

        # EXIT
        exit_action = QAction(QIcon('ui/window-close.svg'), "Exit", self)
        exit_action.triggered.connect(self.exit_action)
        self.toolbar.addAction(exit_action)

    # PROCEDURE SLOTS

        self.buttonSearch.clicked.connect(self.search)

    # ----- SLOTS -----

    # TOOLBAR ACTIONS

    @Slot()  # exit
    def exit_action(self): sys.exit('Goodbye!')

    @Slot()   # about
    def about_action(self): print('About...')

    @Slot()  # config
    def config_action(self): print('Config...')

    # PROCEDURES

    @Slot()  # search button
    def search(self): print('Search...')


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
