__author__ = 'Ben'

import json
import os
import shutil
import socket
import threading

from src.Protocol.protocol import HandelPacket, PacketType, Packet, SendPacket


import base64


class ServerConn:

    def __init__(self, ip: str, port: int):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (ip, port)
        self.server.bind(self.addr)

    def main(self):
        self.accept_connections()

    def accept_connections(self):
        self.server.listen()
        print(f'Listening... {self.addr}')
        while True:
            conn, addr = self.server.accept()
            print("got connectoin ", addr)
            threading.Thread(target=self.handel_client, args=(conn,)).start()

    def handel_client(self, conn):
        while True:
            packet = HandelPacket.recv_packet(conn)
            self.handel_packet(packet, conn)

    def handel_packet(self, packet: Packet, conn):
        # print(packet.payload.decode())
        if packet.packet_type == PacketType.COPY:
            self.handle_copy(packet)
        if packet.packet_type == PacketType.DELETE:
            self.handle_delete(packet)
        if packet.packet_type == PacketType.CREATE:
            self.handle_create(packet)
        if packet.packet_type == PacketType.OPEN:
            self.handle_open(packet,conn)
        if packet.packet_type == PacketType.LSDIR:
            self.handle_lsdir(packet, conn)

    def handle_copy(self, packet):
        json_issue = packet.payload.decode().replace("\\", "\\\\")
        packet_data = json.loads(json_issue)
        print('copying', packet_data.get('src'), packet_data.get('dst'))
        shutil.copy(packet_data.get('src'), packet_data.get('dst'))

    def handle_delete(self, packet):
        packet_data = json.loads(packet.payload.decode())
        print('deleting', packet_data.get('path'))
        os.remove(packet_data.path)

    def handle_create(self, packet):
        packet_data = json.loads(packet.payload.decode())
        print('creating', packet_data['path'], packet_data['filename'])
        os.mkdir(packet_data['path'], packet_data['filename'])

    def handle_open(self, packet, conn):
        packet_data = json.loads(packet.payload.decode())
        path = packet_data['path']
        print(path)
        path= os.path.abspath(path)
        print(path)
        with open(path, "rb") as f:
            data = f.read()
        encoded_content = base64.b64encode(data).decode()
        respones = {
            "filename": path.split("\\")[-1],
            "filedata": encoded_content
        }
        packet_data = json.dumps(respones).encode()
        SendPacket.send_packet(conn, Packet(PacketType.OPEN,packet_data))


    def handle_lsdir(self, packet, conn):
        data = json.loads(packet.payload)
        path = data.get('path')
        dirs = []
        files = []
        print(path)
        try:
            if os.path.isdir(path):
                isFile = False
                for itemm in os.listdir(path):
                    if os.path.isdir(os.path.join(path,itemm)):
                        dirs.append(itemm)
                    else:
                        files.append(itemm)
            else:
                isFile = True

            data_to_send = {
                "isfile": isFile,
                "path": path,
                "dirs": dirs,
                "files": files
            }
            respons = json.dumps(data_to_send)
            packet = Packet(PacketType.LSDIR, respons.encode())
            SendPacket.send_packet(conn, packet)
        except Exception as e:
            print(e)
