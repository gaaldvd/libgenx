# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1018, 805)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.config_pane = QFrame(self.centralwidget)
        self.config_pane.setObjectName(u"config_pane")
        self.config_pane.setFrameShape(QFrame.Shape.StyledPanel)
        self.config_pane.setFrameShadow(QFrame.Shadow.Sunken)
        self.config_pane.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.config_pane)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelDownDir = QLabel(self.config_pane)
        self.labelDownDir.setObjectName(u"labelDownDir")
        self.labelDownDir.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_2.addWidget(self.labelDownDir)

        self.inDownDir = QLineEdit(self.config_pane)
        self.inDownDir.setObjectName(u"inDownDir")
        self.inDownDir.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_2.addWidget(self.inDownDir)

        self.buttonDownDir = QPushButton(self.config_pane)
        self.buttonDownDir.setObjectName(u"buttonDownDir")
        self.buttonDownDir.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.buttonDownDir)

        self.checkPdf = QCheckBox(self.config_pane)
        self.checkPdf.setObjectName(u"checkPdf")
        self.checkPdf.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.checkPdf)

        self.spacerConfig = QSpacerItem(296, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.spacerConfig)

        self.buttonSaveConfig = QPushButton(self.config_pane)
        self.buttonSaveConfig.setObjectName(u"buttonSaveConfig")
        self.buttonSaveConfig.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.buttonSaveConfig)


        self.verticalLayout.addWidget(self.config_pane)

        self.input = QWidget(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.input)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelAuthor = QLabel(self.input)
        self.labelAuthor.setObjectName(u"labelAuthor")
        self.labelAuthor.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.labelAuthor)

        self.inAuthor = QLineEdit(self.input)
        self.inAuthor.setObjectName(u"inAuthor")
        self.inAuthor.setMinimumSize(QSize(200, 0))
        self.inAuthor.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.inAuthor)

        self.labelTitle = QLabel(self.input)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.labelTitle)

        self.inTitle = QLineEdit(self.input)
        self.inTitle.setObjectName(u"inTitle")
        self.inTitle.setMinimumSize(QSize(400, 0))
        self.inTitle.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout.addWidget(self.inTitle)

        self.spacerInput = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.spacerInput)

        self.buttonSearch = QPushButton(self.input)
        self.buttonSearch.setObjectName(u"buttonSearch")
        self.buttonSearch.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.buttonSearch)


        self.verticalLayout.addWidget(self.input)

        self.output = QListWidget(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setMinimumSize(QSize(1000, 400))
        font = QFont()
        font.setFamilies([u"Monospace"])
        font.setPointSize(11)
        self.output.setFont(font)
        self.output.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.output.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.output)

        self.details_pane = QFrame(self.centralwidget)
        self.details_pane.setObjectName(u"details_pane")
        self.details_pane.setFrameShape(QFrame.Shape.StyledPanel)
        self.details_pane.setFrameShadow(QFrame.Shadow.Sunken)
        self.details_pane.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.details_pane)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.details = QLabel(self.details_pane)
        self.details.setObjectName(u"details")

        self.verticalLayout_2.addWidget(self.details)


        self.verticalLayout.addWidget(self.details_pane)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolbar = QToolBar(MainWindow)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMovable(False)
        self.toolbar.setIconSize(QSize(32, 32))
        self.toolbar.setFloatable(False)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"libgenx - Library Genesis Explorer", None))
        self.labelDownDir.setText(QCoreApplication.translate("MainWindow", u"Download directory:", None))
        self.buttonDownDir.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.checkPdf.setText(QCoreApplication.translate("MainWindow", u"PDF only", None))
        self.buttonSaveConfig.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.labelAuthor.setText(QCoreApplication.translate("MainWindow", u"Author:", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"Title:", None))
        self.buttonSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.details.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolbar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

