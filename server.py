import socket
import signal

MAX_BYTES_TO_RECIEVE = 1024

def timeout_handler(signum, frame):
    raise TimeoutError

def main():
    signal.signal(signal.SIGALRM, timeout_handler)

    SERVER_ADDRESS = socket.gethostname()
    SERVER_PORT = 12345


    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((SERVER_ADDRESS, SERVER_PORT))
    tcp_socket.listen(5)
    # signal.alarm(10)
    print("Waiting for connection")
    incoming_socket, incoming_address = tcp_socket.accept()
    # try:
    #     incoming_socket, incoming_address = tcp_socket.accept()
    # except TimeoutError:
    #     print("Couldn't find client in time.")
    #     return


    while True:
        signal.alarm(10)
        decode = ""
        try:
            while not decode:
                data = incoming_socket.recv(MAX_BYTES_TO_RECIEVE)
                decode = data.decode('utf-8')
        except TimeoutError:
            print("Client timed out.")
            break

        signal.alarm(0)
        print("Client:", decode)
        incoming_socket.send(bytearray(decode.upper(), encoding="utf-8"))

    incoming_socket.close()
    print("Server: Closing socket")

main()