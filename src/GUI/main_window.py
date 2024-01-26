from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QDialog

from src.GUI.client.Pages.copy_page import CopyPage
from src.GUI.client.Pages.create_page import CreatePage
from src.GUI.client.Pages.delete_page import DeletePage
from src.GUI.client.Pages.menu_widget import MainMenuPage
from src.GUI.client.Pages.open_page import OpenPage


class ClientGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.menu_page = MainMenuPage(self)
        self.copy_page = CopyPage(self)
        self.delete_page = DeletePage(self)
        self.create_page = CreatePage(self)
        self.open_page = OpenPage(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("ChatRoom")
        self.setGeometry(100, 100, 600, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        central_layout = QVBoxLayout()
        central_layout.addWidget(self.stacked_widget)

        central_widget.setLayout(central_layout)

        self.stacked_widget.addWidget(self.menu_page)
        self.stacked_widget.addWidget(self.copy_page)
        self.stacked_widget.addWidget(self.delete_page)
        self.stacked_widget.addWidget(self.create_page)
        self.stacked_widget.addWidget(self.open_page)

    def show_copy_page(self):
        self.stacked_widget.setCurrentWidget(self.copy_page)

    def show_menu_page(self):
        self.stacked_widget.setCurrentWidget(self.menu_page)

    def show_delete_page(self):
        self.stacked_widget.setCurrentWidget(self.delete_page)

    def show_create_page(self):
        self.stacked_widget.setCurrentWidget(self.create_page)

    def show_open_page(self):
        self.stacked_widget.setCurrentWidget(self.open_page)

    def closeEvent(self, event):
        exit(0)
