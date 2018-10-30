import socket

class SocketClient(object):
    """description of class"""
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, ip_address, port):
        port_description = (ip_address, port)

        # Bind to the port description
        self.sock.connect(port_description)

    def loop_listen(self):
        for i in range(10):
            print(self.sock.recv(1024))

    def end_connection(self):
        print("Ending the TCP Connection.")
        self.sock.close()

if __name__ == "__main__":
    test_client = SocketClient()

    test_client.connect(ip_address='127.0.0.1', port=12345)

    test_client.loop_listen()

    test_client.end_connection()