# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input = QWidget(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.input)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelAuthor = QLabel(self.input)
        self.labelAuthor.setObjectName(u"labelAuthor")

        self.horizontalLayout.addWidget(self.labelAuthor)

        self.inAuthor = QLineEdit(self.input)
        self.inAuthor.setObjectName(u"inAuthor")
        self.inAuthor.setMinimumSize(QSize(200, 0))
        self.inAuthor.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.inAuthor)

        self.labelTitle = QLabel(self.input)
        self.labelTitle.setObjectName(u"labelTitle")

        self.horizontalLayout.addWidget(self.labelTitle)

        self.inTitle = QLineEdit(self.input)
        self.inTitle.setObjectName(u"inTitle")
        self.inTitle.setMinimumSize(QSize(400, 0))
        self.inTitle.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout.addWidget(self.inTitle)

        self.buttonSearch = QPushButton(self.input)
        self.buttonSearch.setObjectName(u"buttonSearch")

        self.horizontalLayout.addWidget(self.buttonSearch)


        self.verticalLayout.addWidget(self.input, 0, Qt.AlignLeft)

        self.output = QTableWidget(self.centralwidget)
        self.output.setObjectName(u"output")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setMinimumSize(QSize(1000, 650))

        self.verticalLayout.addWidget(self.output)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolbar = QToolBar(MainWindow)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMovable(False)
        self.toolbar.setIconSize(QSize(32, 32))
        self.toolbar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"libgenx - Library Genesis Explorer", None))
        self.labelAuthor.setText(QCoreApplication.translate("MainWindow", u"Author:", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"Title:", None))
        self.buttonSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.toolbar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

