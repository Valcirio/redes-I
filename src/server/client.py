import threading
import socket
import customtkinter as ctk

# def main():
#     client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)

#     try:
#         client.connect(('localhost', 7777))
#     except:
#         return print('\nNão foi possível se conectar\n')

#     username = input('\nUsuário:')
#     # connection, address = server.accept()

#     thread1 = threading.Thread(target=receiveMSG, args=[client])
#     thread2 = threading.Thread(target=sendMSG, args=[client, username])

#     thread1.start()
#     thread2.start()

# def receiveMSG(client):
#     while True:
#         try:
#             msg = client.recv(2048).decode('utf-8')
#             print(msg+'\n')
#         except:
#             print('\nNão foi possivel permanecer conectado pelo servidor\n')
#             print('\nEnter to continue\n')
#             client.close()
#             break

# def sendMSG(client, username):
#     while True:
#         try:
#             msg = input('\nMsg:')
#             client.send(f'<{username}>: {msg} //'.encode('utf-8'))
#         except:
#             return

# main()

class Client(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("CTk example")
        self.grid_columnconfigure(0, weight=1)
        
        self.userInput = ctk.CTkEntry(self, width=40)
        self.userInput.grid(row=0, column=1, padx=20, pady=(0, 20), sticky='ew')
        self.roomInput = ctk.CTkEntry(self, width=40)
        self.roomInput.grid(row=1, column=1, padx=20, pady=(0, 20), sticky='ew')
        self.roomBtn = ctk.CTkButton(self, text="Entrar", command=self.enterRoom)
        self.roomBtn.grid(row=2, column=1, padx=20, pady=(0, 20), sticky='ew')

    def enterRoom(self):
        client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        username = self.userInput.get()
        num = int(self.roomInput.get())

        try:
            client.connect(('localhost', num))
        except:
            return print('\nNão foi possível se conectar\n')
    
        thread1 = threading.Thread(target=self.receiveMSG, args=[client])
        thread2 = threading.Thread(target=self.sendMSG, args=[client, username])

        thread1.start()
        thread2.start()

    def receiveMSG(self, client):
        while True:
            try:
                msg = client.recv(2048).decode('utf-8')
                print(msg+'\n')
            except:
                print('\nNão foi possivel permanecer conectado pelo servidor\n')
                print('\nEnter to continue\n')
                client.close()
                break

    def sendMSG(self, client, username):
        while True:
            try:
                msg = input('\nMsg:')
                client.send(f'<{username}>: {msg} //'.encode('utf-8'))
            except:
                return
            
if __name__ == '__main__':
    client = Client()
    client.mainloop()
