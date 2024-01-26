import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QVBoxLayout,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QLabel,
)


class FileManagerWidget(QDialog):
    def __init__(self):
        super(FileManagerWidget, self).__init__()

        self.setWindowTitle('File Manager')
        self.setGeometry(100, 100, 600, 400)
        self.current_path = os.path.expanduser("~")
        self.current_dir = os.path.expanduser("~")

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.path_label = QLabel('', self)
        self.path_label.setFont(QFont('Helvetica', 14))
        self.path_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.path_label)

        self.file_list = QListWidget(self)
        self.file_list.setStyleSheet(
            "QListWidget {border: 2cpx; }"
            "QListWidget::item { padding: 5px; }"
            "QListWidget::item:selected { background-color: #007ACC;  }"
        )
        self.clear_view()
        self.file_list.itemClicked.connect(self.update_view)
        layout.addWidget(self.file_list)

        button_layout = QVBoxLayout()
        ok_button = QPushButton('OK', self)
        ok_button.clicked.connect(self.accept_and_close)
        ok_button.setStyleSheet(
            "QPushButton { background-color: #007ACC; color: white; padding: 8px; border-radius: 5px; font-size: 14px; }"
            "QPushButton:hover { background-color: #005D99; }"
        )
        button_layout.addWidget(ok_button)
        layout.addLayout(button_layout)

        self.cd(self.current_path)

    def clear_view(self):
        self.file_list.clear()
        self.file_list.addItem("..")

    def get_result(self):
        return self.current_path

    def accept_and_close(self):
        self.accept()

    def cd(self, path):
        try:
            if os.path.isdir(path):
                self.clear_view()
                for item in os.listdir(path):
                    good_item = QListWidgetItem(item)
                    good_item.setFont(QFont('Helvetica', 14))
                    if os.path.isfile(f'{path}/{item}'):
                        good_item.setForeground(QColor("white"))
                    else:
                        good_item.setForeground(QColor("#007ACC"))
                    self.file_list.addItem(good_item)

                self.current_dir = os.path.abspath(path)

                self.path_label.setText(self.current_dir)
                self.current_path = self.current_dir
        except Exception as e:
            print(e)

    def update_view(self, item):
        current = item.text()

        if os.path.isdir(f'{self.current_dir}/{current}'):
            self.cd(f'{self.current_dir}/{current}')
        else:
            self.current_path = os.path.abspath(f'{self.current_dir}/{current}')
            self.path_label.setText(self.current_path)
        print(self.current_path)


def open_file_dialog():
    popup = FileManagerWidget()
    result = popup.exec_()

    if result == QDialog.Accepted:
        value = popup.get_result()
        return value
    return None


if __name__ == "__main__":
    app = QApplication([])
    file_manager = FileManagerWidget()
    file_manager.show()
    app.exec_()
