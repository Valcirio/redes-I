import threading
import socket
import customtkinter as ctk

class Server(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("CTk example")
        self.grid_columnconfigure(0, weight=1)
        self.clients = []

        self.roomInput = ctk.CTkEntry(self, width=40)
        self.roomInput.grid(row=0, column=1, padx=20, pady=(0, 20), sticky='ew')

        self.roomBtn = ctk.CTkButton(self, text="Entrar", command=self.initRoom)
        self.roomBtn.grid(row=1, column=1, padx=20, pady=(0, 20), sticky='ew')

    def initRoom(self):

        server = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        num = int(self.roomInput.get())

        try:
            server.bind(('localhost', num))
            server.listen()
            print('aguardando...')
        except:
            return print('\nNão foi possível criar o servidor\n')

        while True:
            client, address = server.accept()
            print(address)
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
