import socket

class SocketClient(object):
    """description of class"""
    def __init__(self, sock=None, buffer_size=1024):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.buffer_size = buffer_size

    def connect(self, ip_address, port):
        port_description = (ip_address, port)

        # Bind to the port description
        self.sock.connect(port_description)

        print("Successfully created connection with server @ address {} through port {}".format(ip_address, port))


    def loop_listen(self):
        for i in range(10):
            print(self.sock.recv(self.buffer_size))

    def send_message(self, message):
        self.sock.send(message.encode())

    def prompt_for_message(self):
        message = input('What would you like to send to the server?')
        self.send_message(message)

    def end_connection(self):
        print("Ending the TCP Connection.")
        self.sock.close()

if __name__ == "__main__":
    test_client = SocketClient()

    test_client.connect(ip_address="localhost", port=8081)


    while(True):
        test_client.prompt_for_message()

    test_client.end_connection()
