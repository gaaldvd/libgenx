import sys
import json

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QSizePolicy, QListWidgetItem, QMenu
from PySide6.QtCore import Slot
from PySide6.QtGui import QAction, QIcon, QDesktopServices

import libgenx_common as lgx
from libgen_api import LibgenSearch
from ui.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.config_pane.hide()
        self.details_pane.hide()
        self.inTitle.setFocus()
        self.results = []
        self.links = {}

        self.config = lgx.load_config()
        self.inDownDir.setText(self.config['downloadDir'])
        self.checkPdf.setChecked(True) if self.config['pdfOnly'] else self.checkPdf.setChecked(False)

        spacer = QWidget()  # spacer for toolbar items
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.args = lgx.parse_args(sys.argv[1:]) if sys.argv[2] or sys.argv[4] else None
        print(self.args) if self.args else print("no args")

        if self.args:
            self.inAuthor.setText(self.args['author'])
            self.inTitle.setText(self.args['title'])
            self.search()

        # TOOLBAR ACTIONS

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

        # CONFIG SIGNALS

        self.buttonDownDir.clicked.connect(self.set_download_dir)
        self.buttonSaveConfig.clicked.connect(self.save_config)

        # PROCEDURE SIGNALS

        self.buttonSearch.clicked.connect(self.search)
        self.inAuthor.returnPressed.connect(self.search)
        self.inTitle.returnPressed.connect(self.search)
        self.output.itemClicked.connect(self.show_details)
        # self.output.itemSelectionChanged.connect(self.show_details)
        self.output.itemDoubleClicked.connect(self.download)

    def contextMenuEvent(self, event):  # todo try to reimplement with customContextMenuRequested()
        menu = QMenu(self)
        actions = []
        for key in self.links.keys():
            if key == 'GET':
                continue
            else:
                actions.append(menu.addAction(key))
        action = menu.exec(self.mapToGlobal(event.pos()))
        if action:
            QDesktopServices.openUrl(self.links[action.text()])

    # ----- SLOTS -----

    # TOOLBAR ACTION SLOTS

    @Slot()  # exit
    def exit_action(self): sys.exit("Goodbye!")

    @Slot()  # about todo open dialog window
    def about_action(self): print("About...")

    @Slot()  # open config pane
    def config_action(self): self.config_pane.show() if self.config_pane.isHidden() else self.config_pane.hide()

    # CONFIG SLOTS

    @Slot()  # open directory browser
    def set_download_dir(self):
        self.inDownDir.setText(QFileDialog.getExistingDirectory(self, "Select directory", ""))

    @Slot()  # save configuration to config.json
    def save_config(self):
        self.config['downloadDir'] = self.inDownDir.text()
        self.config['pdfOnly'] = True if self.checkPdf.isChecked() else False
        with open("config.json", "w") as config_file:
            json.dump(self.config, config_file)
            print(f"Configuration saved - "
                  f"Download directory: {self.config['downloadDir']}, PDF only: {self.config['pdfOnly']}")
        self.config_pane.hide()

    # PROCEDURE SLOTS

    @Slot()  # open the details pane on item selection todo itemSelectionChanged messes things up...
    def show_details(self):
        self.config_pane.hide()
        self.details_pane.show()
        try:
            result = self.results[self.output.currentRow()]
            self.details.setText(f"{result['Author']}: {result['Title']}\n"
                                 f"{result['Publisher']} ({result['Year']}) - "
                                 f"{result['Language']}, {result['Pages']} pages")
            s = LibgenSearch()
            self.links = s.resolve_download_links(self.results[self.output.currentRow()])
        except IndexError:
            pass
        except UnboundLocalError:
            pass

    @Slot()  # search button / return pressed
    def search(self):
        results, self.results = [], []
        self.details_pane.hide()
        self.config_pane.hide()
        self.output.clear()
        self.statusbar.clearMessage()

        if self.inAuthor.text() or self.inTitle.text():
            results = lgx.search(author=self.inAuthor.text(), title=self.inTitle.text(), pdf=self.config['pdfOnly'])
        else:
            self.statusbar.showMessage("Search fields are empty!")

        if results:
            self.statusbar.showMessage(f"Results: {len(results)}")
            for result in results:
                if self.config['pdfOnly'] and result['Extension'] != "pdf":
                    continue
                else:
                    item = QListWidgetItem(result['Label'])
                    self.output.addItem(item)
                    self.results.append(result)

        # self.inAuthor.clear()
        # self.inTitle.clear()

    @Slot()  # download selected item on double click
    def download(self):
        self.statusbar.showMessage("Downloading...")  # todo it doesn't show up for some reason... or does it?
        lgx.download(self.results[self.output.currentRow()], self.config['downloadDir'], self.links['GET'])
        self.statusbar.showMessage(f"Results: {len(self.results)}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
