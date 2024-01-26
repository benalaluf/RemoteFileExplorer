import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication, QHBoxLayout
from src.GUI.client.Pages.file_dialog import open_file_dialog


class CopyPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()

        self.src_path = ''
        self.dst_path = ''

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

        dst_layout = QHBoxLayout()
        self.dst_label = QLabel("Destination:")
        self.dst_label_path = QLabel("None")
        self.dst_button = QPushButton("Choose")
        self.dst_button.clicked.connect(self.set_dst_path)

        dst_layout.addWidget(self.dst_label)
        dst_layout.addWidget(self.dst_label_path)
        dst_layout.addWidget(self.dst_button)

        layout.addLayout(src_layout)
        layout.addLayout(dst_layout)
        layout.addSpacing(30)

        self.copy_button = QPushButton("Copy")
        self.copy_button.clicked.connect(self.copy)
        self.copy_button.setStyleSheet(
            "height: 40px; background-color: #007ACC; color: white; font-weight: bold; font-size: 18px;border-radius: 20px;"
        )

        layout.addWidget(self.copy_button)

    def set_src_path(self):
        self.src_path = open_file_dialog()
        self.src_label_path.setText(self.src_path)

    def set_dst_path(self):
        self.dst_path = open_file_dialog()
        self.dst_label_path.setText(self.dst_path)

    def copy(self):
        print(f"Copying {self.src_path} to {self.dst_path}")
        # Implement your copy logic here
        self.parent.show_menu_page()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    copy_page = CopyPage(None)
    copy_page.show()
    sys.exit(app.exec_())
