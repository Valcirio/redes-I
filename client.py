import threading
import socket
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox 

class Client(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.title("App de Conversa")
        self.resizable(width=False, height=False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
        
        self.labelUser = ctk.CTkLabel(self, text='Usuário:')
        self.labelUser.place(x=130, y=60)

        self.userInput = ctk.CTkEntry(self, width=250, height=30)
        self.userInput.place(x=130, y=80)

        self.labelHost = ctk.CTkLabel(self, text='Host:')
        self.labelHost.place(x=130, y=120)

        self.hostInput = ctk.CTkEntry(self, width=250, height=30)
        self.hostInput.place(x=130, y=140)

        self.labelRoom = ctk.CTkLabel(self, text='Sala:')
        self.labelRoom.place(x=130, y=180)

        self.roomInput = ctk.CTkEntry(self, width=250, height=30)
        self.roomInput.place(x=130, y=200)

        self.roomBtn = ctk.CTkButton(self, text="Entrar", width=250, height=30, command=self.enterRoom)
        self.roomBtn.place(x=130, y=250)


    def enterRoom(self):
        self.client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        self.username = self.userInput.get()
        num = int(self.roomInput.get())
        host = self.hostInput.get()

        try:
            self.client.connect((host, num))
        except:
            CTkMessagebox(title="Error", message="Não foi possível se conectar!", icon="cancel")
            return print('\nNão foi possível se conectar\n')

        janela2 = ctk.CTkToplevel()
        janela2.focus()
        janela2.title("Chat")
        janela2.geometry('400x600')

        self.containerText = ctk.CTkTextbox(janela2, width=360, height=500)
        self.containerText.place(x=20, y=20)

        self.containerMSG = ctk.CTkEntry(janela2, width=200, height=30)
        self.containerMSG.place(x=20, y=530)
        self.msgBtn = ctk.CTkButton(janela2, command=self.sendMSG, text="Insert Text", width=100, height=30)
        self.msgBtn.place(x=280, y=530)

        thread1 = threading.Thread(target=self.receiveMSG, args=[self.client])

        thread1.start()
        

    def receiveMSG(self, client):
        while True:
            try:
                msg = client.recv(2048).decode('utf-8')
                self.containerText.insert("insert", '\n'+msg)
            except:
                print('\nNão foi possivel permanecer conectado pelo servidor\n')
                print('\nEnter to continue\n')
                client.close()
                break
            
    def sendMSG(self):
        msg = self.containerMSG.get()
        self.containerText.insert("insert", '\n'+'Você:'+msg)
        self.client.send(f'{self.username}: {msg}'.encode('utf-8'))

            
if __name__ == '__main__':
    client = Client()
    client.mainloop()
