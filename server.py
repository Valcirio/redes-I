import threading
import socket
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

HOST = socket.gethostbyname(socket.gethostname())

class Server(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("350x250")
        self.title("CTk example")
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(0, weight=1)
        self.clients = []

        self.labelRoom = ctk.CTkLabel(self, text='Criar Sala', width=100)
        self.labelRoom.place(x=120, y=40)

        self.roomInput = ctk.CTkEntry(self, width=250, height=30)
        self.roomInput.place(x=50, y=100)

        self.roomBtn = ctk.CTkButton(self, text="Entrar", width=250, height=30, command=self.initRoom)
        self.roomBtn.place(x=50, y=140)

        self.labelInfo = ctk.CTkLabel(self, text='A sala é uma porta, recebendo apenas números.')
        self.labelInfo.place(x=50, y=170)

        self.exInfo = ctk.CTkLabel(self, text='Ex: 7777.')
        self.exInfo.place(x=50, y=190)

        self.hostInfo = ctk.CTkLabel(self, text='O host para acesso se encontra no prompt.')
        self.hostInfo.place(x=50, y=210)

    def initRoom(self):

        server = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        num = int(self.roomInput.get())

        try:
            server.bind((HOST, num))
            server.listen()
            print(f'Host de acesso: {HOST}')
            print('aguardando usuários...')
        except:
            CTkMessagebox(title="Erro", message="Não foi possível criar o servidor.", icon="cancel")
            return print('\nNão foi possível criar o servidor\n')

        while True:
            client, address = server.accept()
            print(f'O cliente com o endereço {address} entrou!')
            self.clients.append(client)

            thread = threading.Thread(target=self.treatement, args=[client])
            thread.start()

    def treatement(self, client):
        while True:
            try:
                msg = client.recv(2048)
                self.broadcast(msg, client)
            except:
                self.deleteClient(client)
                break

    def broadcast(self, msg, client):
        for clientItem in self.clients:
            if clientItem != client:
                try:
                    clientItem.send(msg)
                except:
                    self.deleteClient(clientItem)


    def deleteClient(self, client):
        self.clients.remove(client)

if __name__ == '__main__':
    server = Server()
    server.mainloop()
