from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QDialog, QPushButton
from copy_page import CopyPage
from file_dialog import FileManagerWidget
from menu_widget import MainMenuPage
from delete_page import DeletePage
class ClientGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.menu_page = MainMenuPage(self)
        self.copy_page = CopyPage(self)
        self.delete_page = DeletePage(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("ChatRoom")
        self.setGeometry(100, 100, 600, 800)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        central_layout = QVBoxLayout()
        central_layout.addWidget(self.stacked_widget)

        central_widget.setLayout(central_layout)

        self.stacked_widget.addWidget(self.menu_page)
        self.stacked_widget.addWidget(self.copy_page)
        self.stacked_widget.addWidget(self.delete_page)

    def show_copy_page(self):
        self.stacked_widget.setCurrentWidget(self.copy_page)

    def show_menu_page(self):
        self.stacked_widget.setCurrentWidget(self.menu_page)

    def show_delete_page(self):
        self.stacked_widget.setCurrentWidget(self.delete_page)


    def closeEvent(self, event):
        exit(0)

    def open_file_dialog(self):
        popup = FileManagerWidget(self)
        result = popup.exec_()

        if result == QDialog.Accepted:
            value = popup.get_result()
            print("Value from pop-up window:", value)
            return value
        return None

