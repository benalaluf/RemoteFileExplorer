from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QDialog, QLineEdit
from file_dialog import FileManagerWidget


class CreatePage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI()

        self.src_path = ''
        self.new_name = ''

    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        title_label = QLabel("Create")
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

        new_text_layout = QHBoxLayout()
        self.new_name_lable = QLabel("Enter the name of the item:")
        self.new_name_text = QLineEdit()
        self.new_name_text.setPlaceholderText("write file name")
        new_text_layout.addWidget(self.new_name_lable)
        new_text_layout.addWidget(self.new_name_text)

        layout.addLayout(new_text_layout)

        self.copy_button = QPushButton("Create")
        self.copy_button.clicked.connect(self.create)
        self.copy_button.clicked.connect(self.set_new_name)


        layout.addWidget(self.copy_button)


    def set_src_path(self):
        self.src_path = self.open_file_dialog()
        print(self.src_path)
        self.src_lable_path.setText(self.src_path)

    def set_new_name(self):
        self.new_name = self.new_name_text.text()
        print(self.new_name)
        

    def create(self):
        print(f"create {self.new_name}")
        self.parent.show_menu_page()


    def open_file_dialog(self):
        popup = FileManagerWidget(self)
        result = popup.exec_()

        if result == QDialog.Accepted:
            value = popup.get_result()
            # print("Value from pop-up window:", value)
            return value
        return None

