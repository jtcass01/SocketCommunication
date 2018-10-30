import socket

class SocketServer(object):
    """description of class"""
    def __init__(self, sock=None):
        self.client = None

        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, ip_address, port):
        port_description = (ip_address, port)

        # Bind to the port description
        self.sock.bind(port_description)

        # Sets up and start TCP Listener
        self.sock.listen(1)

        # Wait for TCP connection to arrive [Returns client]
        print("Waiting for client...")
        self.client, client_address = self.sock.accept()
        print("Creating connection with client from ", client_address)

    def send_message(self, message):
        self.client.send(message)

    def end_connection(self):
        print("Ending the TCP Connection.")
        self.client.close()


if __name__ == "__main__":
    test_server = SocketServer()

    test_server.connect(ip_address='127.0.0.1', port=12345)

    for i in range(10):
        test_server.send_message(b'Test')

    test_server.end_connection()