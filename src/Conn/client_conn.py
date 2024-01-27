__author__ = 'Ben'

import json
import threading
from socket import socket, AF_INET, SOCK_STREAM

from src.Protocol.protocol import HandelPacket, Packet, PacketType, SendPacket


class ClientConn:

    def __init__(self, ip: str, port: int):
        self.server_addr = (ip, port)
        print('server addr',self.server_addr)
        self.handle_packet_expansion = None
        self.client = socket(AF_INET, SOCK_STREAM)

    def main(self):
        self.connect_to_server()
        threading.Thread(target=self.receive).start()

    def connect_to_server(self):
        try:
            print("trying to connect")
            self.client.connect(self.server_addr)
            print(f'CONNECTED {self.server_addr}')
        except Exception as e:
            print(e)
            self.client.close()
            exit(1)

    def copy(self, src, dst):
        print('sending')
        data = f'{{"src": "{src}", "dst": "{dst}"}}'
        packet = Packet(PacketType.COPY, data.encode())
        SendPacket.send_packet(self.client, packet)

    def delete(self, path):
        print('sending')
        data = f'{{"path": "{path}"}}'
        packet = Packet(PacketType.DELETE, data.encode())
        SendPacket.send_packet(self.client, packet)

    def create(self, path, filename):
        print('sending')
        data = f'{{"path": "{path}", "filename": "{filename}"}}'
        packet = Packet(PacketType.CREATE, data.encode())
        SendPacket.send_packet(self.client, packet)

    def open(self, path):
        print('sending')
        data = f'{{"path": "{path}"}}'
        packet = Packet(PacketType.OPEN, data.encode())
        SendPacket.send_packet(self.client, packet)

    def receive(self):
        while True:
            try:
                packet = HandelPacket.recv_packet(self.client)
                self.handle_packet(packet)
            except Exception as e:
                print("dissconetig", e)
                break
        self.client.close()

    def lsdir(self, path):
        data = f'{{"path": "{path}"}}'
        packet = Packet(PacketType.LSDIR, data.encode())
        SendPacket.send_packet(self.client,packet)
        print("sending ",data)

    def handle_packet(self, packet: Packet):
        if self.handle_packet_expansion:
            self.handle_packet_expansion(packet)

    def expand_handle_packet(self, handle_packet_func):
        self.handle_packet_expansion = handle_packet_func
