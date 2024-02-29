import socket
import time
import sys

class SocketClient(object):
    def __init__(self, ip, port):
        """
        Initializes the SocketClient object with the provided IP address and port.

        Args:
            ip (str): The IP address of the server to connect to.
            port (int): The port number of the server to connect to.
        """
        self.ip = ip
        self.port = port
        # Attempt to create and connect the socket within a try-except block to handle connection refused errors.
        try:
            self.csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.csocket.connect((ip, port))
        except ConnectionRefusedError:
            print(f'Connection to {ip}:{port} refused.')
            sys.exit(1)

    def close(self):
        """
        Closes the client socket connection.
        """
        if self.csocket:
            self.csocket.close()
            print('Closed connection')

    def send(self):
        """
        Sends data to the server and receives a response.

        Returns:
            bytes: The response data received from the server.
        """
        try:
            print(f'Sending data to {self.ip}:{self.port}')
            self.csocket.send(b'ping')
            data = self.csocket.recv(1024)
            print('Received', data)
            return data
        except BrokenPipeError:
            print("Broken pipe error occurred. The server might have closed the connection.")
            sys.exit(1)

if __name__ == '__main__':
    sClient = None
    try:
        print('Starting client')
        sClient = SocketClient('localhost', 11500)
        while True:
            sClient.send()
            time.sleep(1)
    except KeyboardInterrupt:
        sClient.close()
        sys.exit(1)
