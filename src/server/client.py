import threading
import socket

def main():
    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777))
    except:
        return print('\nNão foi possível se conectar\n')

    username = input('\nUsuário:')
    # connection, address = server.accept()

    thread1 = threading.Thread(target=receiveMSG, args=[client])
    thread2 = threading.Thread(target=sendMSG, args=[client, username])

    thread1.start()
    thread2.start()

def receiveMSG(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg+'\n')
        except:
            print('\nNão foi possivel permanecer conectado pelo servidor\n')
            print('\nEnter to continue\n')
            client.close()
            break

def sendMSG(client, username):
    while True:
        try:
            msg = input('\nMsg:')
            client.send(f'<{username}>: {msg} //'.encode('utf-8'))
        except:
            return

main()

        