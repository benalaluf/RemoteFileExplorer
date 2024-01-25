import sys

from PyQt5.QtWidgets import QApplication
from src.Client.GUI.main_window import ClientGUI

class FileExplorerApp():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.widget = ClientGUI()


    def start(self):
        self.widget.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    FileExplorerApp().start()