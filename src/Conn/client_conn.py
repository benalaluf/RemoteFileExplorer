__author__ = 'Ben'

import json
import threading
from socket import socket, AF_INET, SOCK_STREAM

from src.Protocol.protocol import HandelPacket, Packet, PacketType, SendPacket


class ClientConn:

    def __init__(self, ip: str, port: int):
        self.server_addr = (ip, port)
        self.handle_packet_expansion = None
        self.client = socket(AF_INET, SOCK_STREAM)

    def main(self):
        self.connect_to_server()
        threading.Thread(target=self.receive).start()
        self.send_test()

    def connect_to_server(self):
        try:
            self.client.connect(self.server_addr)
            print(f'CONNECTED {self.server_addr}')
        except Exception as e:
            print(e)
            self.client.close()
            exit(1)

    def send_test(self):
        print('sending')
        data = '{"src": "nigga", "dst": "hello"}'
        packet = Packet(PacketType.COPY,data.encode())
        SendPacket.send_packet(self.client,packet)

    def receive(self):
        while True:
            try:
                packet = HandelPacket.recv_packet(self.client)
                self.handle_packet(packet)
            except Exception as e:
                print("dissconetig", e)
                break
        self.client.close()

    def handle_packet(self, packet: Packet):
        if self.handle_packet_expansion:
            self.handle_packet_expansion(packet)

    def expand_handle_packet(self, handle_packet_func):
        self.handle_packet_expansion = handle_packet_func
