"""
LibGenX GUI script.
"""

from sys import argv
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from ui.MainWindow import Ui_MainWindow
from libgenx_common import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

        # [...]

    # SLOTS

    # @Slot()
    # def slot_action() [...]

def main():

    # initialization
    config = load_config()
    query, seq = get_cli_args()
    filters, mode = parse_filter_seq(seq) if seq else None, None
    print(f"config: {config}\n"
          f"query: {query}\nseq: {seq}\n"
          f"filters: {filters}\nmode: {mode}")

    app = QtWidgets.QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
