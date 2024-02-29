import threading
import socket
import json
import time
import random

class Server(threading.Thread):
    def __init__(self, host, port):
        """
        Initializes the Server object with the provided host and port.

        Args:
            host (str): The hostname or IP address on which the server will run.
            port (int): The port number on which the server will listen for incoming connections.
        """
        super().__init__()
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        """
        Runs the server and handles incoming client connections.
        """
        try:
            # Bind the socket to the host and port
            self.socket.bind((self.host, self.port))
            # Listen for incoming connections, with a backlog of 5
            self.socket.listen(5)
            print(f'Server started on {self.host}:{self.port}')

            while True:
                # Accept incoming connection
                client, address = self.socket.accept()
                # Set a timeout for the client connection (60 seconds)
                client.settimeout(60)
                # Start a new thread to handle the client
                threading.Thread(target=self.handle_client, args=(client, address)).start()

        except Exception as e:
            print(f"Server error: {e}")

        finally:
            # Close the server socket when done
            self.socket.close()
            print("Server stopped")

    def handle_client(self, client, address):
        """
        Handles communication with a client.

        Args:
            client (socket.socket): The client socket object.
            address (tuple): The address of the client.
        """
        try:
            print(f'Accepting connection from {address}, client {client}')

            while True:
                # Receive data from client
                data = client.recv(1024)
                if not data:
                    break

                # Process received data
                answer = {}
                answer['data'] = data.decode('ascii')
                answer['token'] = self._generate_token()
                answer['datetime'] = time.strftime('%Y-%m-%d %H:%M:%S')

                # Serialize data to JSON format
                serialised = json.dumps(answer)
                print(serialised)

                # Send serialized data back to client
                client.send(serialised.encode('ascii'))

        except socket.timeout:
            print(f"Connection with {address} timed out")
            client.close()

        except Exception as e:
            print(f"Error handling client {address}: {e}")
            client.close()

    def _generate_token(self, length=16):
        """
        Generates a random token of a specified length.

        Args:
            length (int): The length of the token.

        Returns:
            str: The randomly generated token.
        """
        if length <= 8 or length > 32:
            raise ValueError("Length must be between 8 and 32.")
        return 'token_' + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=length))

# Usage:
if __name__ == "__main__":
    # Create a new server instance and start it
    server = Server('localhost', 11500)
    server.start()
