import json
import os
import sys

# import qdarktheme
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication

from src.Conn.client_conn import ClientConn
from src.GUI.main_window import ClientGUI

from src.Protocol.protocol import Packet, PacketType
import threading


class ClientApp:

    def __init__(self, ip, port):
        self.app = QApplication(sys.argv)
        # qdarktheme.setup_theme()

        self.client_conn = ClientConn(ip, port)
        self.client_gui = ClientGUI()

        self.client_conn.expand_handle_packet(self.handle_packet)
        self.client_gui.attack_client_conn(self.client_conn)
        self.connect_buttons()

        self.mute = False
        self.save_dir = os.path.expanduser("~")+"\\Desktop\\ServerOpen"
        print(self.save_dir)

    def main(self):
        threading.Thread(target=self.client_conn.main).start()
        os.mkdir(self.save_dir)

        self.run_gui()

    def run_gui(self):
        self.client_gui.show()
        sys.exit(self.app.exec_())

    def handle_packet(self, packet: Packet):
        if packet.packet_type == PacketType.LSDIR:
            self.lsdir(packet)

        if packet.packet_type == PacketType.OPEN:
            self._open(packet)

    def connect_buttons(self):
        self.client_gui.copy_page.copy_button.clicked.connect(self._copy)
        self.client_gui.delete_page.delete_button.clicked.connect(self._copy)
        self.client_gui.create_page.create_button.clicked.connect(self._copy)

    def _copy(self):
        src = self.client_gui.copy_page.src_label_path.text()
        dst = self.client_gui.copy_page.dst_label_path.text()
        self.client_conn.copy(src, dst)

    def _delete(self):
        path = self.client_gui.delete_page.src_lable_path.text()
        self.client_conn.delete(path)

    def _create(self):
        path = self.client_gui.create_page.src_lable_path.text()
        file_name = self.client_gui.create_page.new_name_text.text()
        self.client_conn.create(path, file_name)
        pass

    def lsdir(self, packet):
        data = json.loads(packet.payload.decode())
        is_file = data.get('isfile')
        path = data.get('path')
        dirs = data.get('dirs')
        files = data.get('files')
        self.client_gui.update_lsdir(is_file, path, dirs, files)

    def _open(self,packet):
        data = json.loads(packet.payload.decode())
        filename = data.get("filename")
        filedata = data.get("filedata")

        with open(os.path.join(self.save_dir,filename), 'wb') as f:
            f.write(filedata)

        os.startfile(os.path.join(self.save_dir,filename))
