#!/usr/bin/python3

#Requirement : The server sends data according to the users wish and
# if nothing is enetered the program exits

#i.e server -> client then client displays the message

import socket

def main():
    i = 1
    servsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servsocket.bind(("0.0.0.0", 1235))

    servsocket.listen()
    (clientsocket, (ip, port)) = servsocket.accept()

    while i != 1:
        print("Condition 1")
        data = clientsocket.recv(2048)
        print(data)
        clientsocket.send(data)
    else:
        print("Condition 2")
        while True:
            text = input("Enter the text you want to send :")
            if text == '':
                print("Nothing entered...exiting")
                return False
                break
            else:
                res = bytes(text, 'utf-8')
                clientsocket.send(res)

if __name__ == '__main__':
    main()
