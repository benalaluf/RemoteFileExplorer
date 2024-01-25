import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QFileDialog, \
    QWidget, QListWidgetItem, QColorDialog, QLabel, QDialog


class FileManagerWidget(QDialog):
    def __init__(self, parent):
        super(FileManagerWidget, self).__init__()
        self.parent = parent

        self.setWindowTitle('File Manager')
        self.setGeometry(100, 100, 500, 400)
        self.current_path = "c:\\"
        self.current_dir = "c:\\"

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.path_label = QLabel('', self)
        self.path_label.setFont(QFont('Helvetica', 14))
        self.path_label.setAlignment(Qt.AlignCenter)
        self.path_label.adjustSize()
        layout.addWidget(self.path_label)

        self.file_list = QListWidget(self)
        self.clear_view()
        self.file_list.itemClicked.connect(self.update_view)
        layout.addWidget(self.file_list)

        button = QPushButton('ok', self)
        button.clicked.connect(self.accept_and_close)
        layout.addWidget(button)
        # self.setCentralWidget(central_widget)

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
                    if os.path.isfile(f'{path}\\{item}'):
                        good_item.setForeground(QColor("red"))
                    else:
                        good_item.setForeground(QColor("blue"))
                    self.file_list.addItem(good_item)

                self.current_dir = os.path.abspath(path)

                self.path_label.setText(self.current_dir)
                self.current_path = self.current_dir
        except Exception as e:
            print(e)

    def update_view(self, item):
        current = item.text()

        if os.path.isdir(f'{self.current_dir}\\{current}'):
            self.cd(f'{self.current_dir}\\{current}')
        else:

            self.current_path = os.path.abspath(f'{self.current_dir}\\{current}')
            self.path_label.setText(self.current_path)
        print(self.current_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    file_manager = FileManagerWidget()
    file_manager.show()
    sys.exit(app.exec_())
