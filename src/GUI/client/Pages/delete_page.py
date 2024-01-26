from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout

from src.GUI.client.Pages.file_dialog import open_file_dialog


class DeletePage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI()

        self.src_path = ''

    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        title_label = QLabel("Delete")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 36px;")
        layout.addWidget(title_label)

        layout.addSpacing(150)

        src_layout = QHBoxLayout()
        self.src_lable = QLabel("src:")
        self.src_lable_path = QLabel("None")
        self.src_button = QPushButton("Choose")
        self.src_button.clicked.connect(self.set_src_path)
        src_layout.addWidget(self.src_lable)
        src_layout.addWidget(self.src_lable_path)
        src_layout.addWidget(self.src_button)

        layout.addLayout(src_layout)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete)

        layout.addWidget(self.delete_button)


    def set_src_path(self):
        self.src_path = self.open_file_dialog()
        print(self.src_path)
        self.src_lable_path.setText(self.src_path)

    def set_dst_path(self):
        self.dst_path = open_file_dialog()
        print(self.dst_path)
        self.dst_lable_path.setText(self.dst_path)

    def delete(self):
        print(f"Deleting {self.src_path}")
        self.parent.show_menu_page()

