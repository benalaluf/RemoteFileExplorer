import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication


class MainMenuPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        title_label = QLabel("RemoteFileExplorer")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 36px; font-weight: bold;")
        layout.addWidget(title_label)

        layout.addSpacing(60)

        button_layout = QVBoxLayout()
        self.copy_button = QPushButton("Copy")
        self.copy_button.clicked.connect(self.parent.show_copy_page)
        self.copy_button.setFixedHeight(80)
        self.copy_button.setStyleSheet(
            "height: 40px; background-color: #007ACC; color: white; font-weight: bold; font-size: 18px;border-radius: 20px;"
        )
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.parent.show_delete_page)
        self.delete_button.setFixedHeight(80)
        self.delete_button.setStyleSheet(
            "height: 40px; background-color: #007ACC; color: white; font-weight: bold; font-size: 18px;border-radius: 20px;"
        )
        self.open_button = QPushButton("Open")
        self.open_button.clicked.connect(self.parent.show_open_page)
        self.open_button.setFixedHeight(80)
        self.open_button.setStyleSheet(
            "height: 40px; background-color: #007ACC; color: white; font-weight: bold; font-size: 18px;border-radius: 20px;"
        )
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.parent.show_create_page)
        self.create_button.setFixedHeight(80)
        self.create_button.setStyleSheet(
            "height: 40px; background-color: #007ACC; color: white; font-weight: bold; font-size: 18px;border-radius: 20px;"
        )

        button_layout.addWidget(self.copy_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.open_button)
        button_layout.addWidget(self.create_button)

        layout.addLayout(button_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_menu = MainMenuPage(None)
    main_menu.show()
    sys.exit(app.exec_())
