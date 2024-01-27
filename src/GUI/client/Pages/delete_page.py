import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout



class DeletePage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()

        self.src_path = ''

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        title_label = QLabel("RemoteFileExplorer")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 36px; font-weight: bold;")
        layout.addWidget(title_label)

        layout.addSpacing(60)

        src_layout = QHBoxLayout()
        self.src_label = QLabel("Source:")
        self.src_label_path = QLabel("None")
        self.src_button = QPushButton("Choose")
        self.src_button.clicked.connect(self.set_src_path)

        src_layout.addWidget(self.src_label)
        src_layout.addWidget(self.src_label_path)
        src_layout.addWidget(self.src_button)

        layout.addLayout(src_layout)
        layout.addSpacing(30)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete)
        self.delete_button.setStyleSheet(
            "height: 40px; background-color: #007ACC; color: white; font-weight: bold; font-size: 18px;border-radius: 20px;"
        )

        layout.addWidget(self.delete_button)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.parent.show_menu_page)
        self.back_button.setStyleSheet(
            "height: 40px; background-color: #007ACC; color: white; font-weight: bold; font-size: 18px;border-radius: 20px;"
        )

        layout.addWidget(self.back_button)

    def set_src_path(self):
        self.src_path = self.parent.open_file_dialog()
        self.src_label_path.setText(self.src_path)

    def delete(self):
        print(f"Deleting {self.src_path}")
        os.remove(self.src_path)
        self.parent.show_menu_page()
