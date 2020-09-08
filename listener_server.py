from utilities.Logger import Logger
from socket import socket, AF_INET, SOCK_STREAM, gethostname, gethostbyname


class SocketServer(object):
    """description of class"""
    def __init__(self, sock: socket = None, buffer_size: int = 1024) -> None:
        self.client = None

        if sock is None:
            self.sock = socket(AF_INET, SOCK_STREAM)
        else:
            self.sock = sock

        self.buffer_size = buffer_size

    def connect(self, ip_address: str, port: int) -> None:
        port_description = (ip_address, port)

        try:
            # Bind to the port description
            self.sock.bind(port_description)

            # Sets up and start TCP Listener
            self.sock.listen(2)

            # Wait for TCP connection to arrive [Returns client]
            Logger.console_log(message="Waiting for client...", status=Logger.LogStatus.EMPHASIS)
            self.client, client_address = self.sock.accept()
            Logger.console_log(message="Creating connection with client from " + str(client_address), status=Logger.LogStatus.SUCCESS)
        except Exception as err:
            Logger.console_log(message="Unable to send message due to error: " + str(err), status=Logger.LogStatus.FAIL)

    def send_message(self, message: str) -> None:
        self.client.send(message)

    def loop_listen(self) -> None:
        while True:
            data = self.client.recv(self.buffer_size).decode('utf-8')
            if data != '':
                Logger.console_log(message="Received {} of type {}".format(data, type(data)), status=Logger.LogStatus.SUCCESS)

    def end_connection(self) -> None:
        Logger.console_log(message="Ending the TCP Connection.", status=Logger.LogStatus.EMPHASIS)
        self.client.close()


def get_my_ip_address() -> str:
    return gethostbyname(gethostname())


if __name__ == "__main__":
    test_server = SocketServer()

    test_server.connect(ip_address=get_my_ip_address(), port=16000)

    test_server.loop_listen()

    test_server.end_connection()
