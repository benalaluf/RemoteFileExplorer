__author__ = 'Ben'

import json
import os
import shutil
import socket
import threading

from src.Protocol.protocol import HandelPacket, PacketType, Packet


class ServerClientData:
    pass


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
            print("got connectoin ",addr)
            threading.Thread(target=self.handel_client, args=(conn,)).start()

    def handel_client(self, conn):
        while True:
            packet = HandelPacket.recv_packet(conn)
            self.handel_packet(packet)

    def handel_packet(self, packet: Packet):
        print(packet.payload.decode())
        if packet.packet_type == PacketType.COPY:
            self.handle_copy(packet)
        if packet.packet_type == PacketType.DELETE:
            self.handle_delete(packet)
        if packet.packet_type == PacketType.CREATE:
            self.handle_create(packet)
        if packet.packet_type == PacketType.OPEN:
            self.handle_open(packet)
        if packet.packet_type == PacketType.LSDIR:
            self.handle_lsdir(packet)

    def handle_copy(self, packet):
        json_issue = packet.payload.decode().replace("\\","\\\\")
        packet_data = json.loads(json_issue)
        print('copying',packet_data.get('src'), packet_data.get('dst'))
        # shutil.copy(packet_data.get('src'), packet_data.get('dst'))


    def handle_delete(self, packet):
        packet_data = json.load(packet.payload)
        print('deleting', packet_data.get('path'))
        # os.remove(packet_data.path)

    def handle_create(self, packet):
        packet_data = json.loads(packet.payload)
        print('creating',packet_data['path'], packet_data['filename'])
        # os.mkdir(packet_data['path'], packet_data['filename'])

    def handle_open(self, packet):
        packet_data = json.loads(packet.payload)
        print(packet_data['path'])
        # os.startfile(packet_data['path'])

    def handle_lsdir(self, packet):
        pass
