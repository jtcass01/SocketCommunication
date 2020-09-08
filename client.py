from socket import socket, AF_INET, SOCK_STREAM, gethostname, gethostbyname
from utilities.Logger import Logger


class Client(object):
    """description of class"""
    def __init__(self, sock=None, buffer_size=1024):
        if sock is None:
            self.sock = socket(AF_INET, SOCK_STREAM)
        else:
            self.sock = sock
        self.buffer_size = buffer_size

    def connect(self, ip_address: str, port: int) -> None:
        port_description = (ip_address, port)

        Logger.console_log(message="Attempting to bind to port with description: " + str(port_description), status=Logger.LogStatus.EMPHASIS)

        # Bind to the port description
        try:
            self.sock.connect(port_description)
            Logger.console_log(message="Successfully created connection with server @ address {} through port {}".format(ip_address, port), status=Logger.LogStatus.SUCCESS)
        except Exception as err:
            Logger.console_log(message="Unable to send message due to error: " + str(err), status=Logger.LogStatus.FAIL)

    def send_message(self, message: str) -> None:
        self.sock.send(message.encode())

    def prompt_for_message(self) -> None:
        Logger.console_log(message="", status=Logger.LogStatus.COMMUNICATION)
        message = input('What would you like to send to the server?')
        self.send_message(message=message)

    def end_connection(self) -> None:
        Logger.console_log(message="Ending the TCP Connection.", status=Logger.LogStatus.EMPHASIS)
        self.sock.close()

    def menu(self) -> None:
        Logger.console_log(message="==== MENU ====", status=Logger.LogStatus.COMMUNICATION)
        Logger.console_log(message="1) send a message", status=Logger.LogStatus.COMMUNICATION)
        Logger.console_log(message="0) end connection", status=Logger.LogStatus.COMMUNICATION)

        response = int(input("What would you like to do: "))

        if response == 1:
            self.prompt_for_message()
        elif response == 0:
            self.end_connection()
        else:
            Logger.console_log(message="Invalid menu selection.  Please try again...", status=Logger.LogStatus.FAIL)

        return response


def get_my_ip_address() -> str:
    return gethostbyname(gethostname())


if __name__ == "__main__":
    test_client = Client()

    print(gethostname())

    test_client.connect(ip_address=get_my_ip_address(), port=16000)

    response = 1
    while response != 0:
        response = test_client.menu()
