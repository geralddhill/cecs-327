import socket

MAX_BYTES_TO_RECIEVE = 1024  

def main():
    # Server credentials and settings
    server_ip = input("Input IP address for server: ")
    server_port = int(input("Input the port number: "))
    
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((server_ip, server_port))
    


    message = input("Input a message (exit to exit): ")

    while message.lower() != "exit":
        tcp_socket.send(bytearray(str(message), encoding='utf-8'))
        server_response = tcp_socket.recv(MAX_BYTES_TO_RECIEVE)

        # Do something with the server response
        decode = server_response.decode('utf-8')
        print("Server: ", decode)
        
        message = input("Input a message: ")

    tcp_socket.close() # Close the socket when done

main()