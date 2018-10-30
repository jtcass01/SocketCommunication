import socket

class SocketServer(object):
    """description of class"""
    def __init__(self, sock=None, buffer_size = 1024):
        self.client = None

        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

        self.buffer_size = buffer_size

    def connect(self, ip_address, port):
        port_description = (ip_address, port)

        # Bind to the port description
        self.sock.bind(port_description)

        # Sets up and start TCP Listener
        self.sock.listen(2)

        # Wait for TCP connection to arrive [Returns client]
        print("Waiting for client...")
        self.client, client_address = self.sock.accept()
        print("Creating connection with client from ", client_address)

    def send_message(self, message):
        self.client.send(message)

    def loop_listen(self):
        while(True):
            data = self.client.recv(self.buffer_size).decode('utf-8')
            if data != '':
                print("Recieved {} of type {}".format(data, type(data)))

    def end_connection(self):
        print("Ending the TCP Connection.")
        self.client.close()


if __name__ == "__main__":
    test_server = SocketServer()

    test_server.connect(ip_address="localhost", port=8081)

    test_server.loop_listen()

    test_server.end_connection()
