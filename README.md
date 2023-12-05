# Projeto de Redes I

## Sobre o Projeto

Foi desenvolvido um aplicativo de mensagens, onde o usuário pode criar uma sala de bate papo, enviar a porta para os múltiplos clientes, e conversarem através de um chat. 

## Bibliotecas

- CustomTkiner
- Socket
- Thread

## Protocolo

![Diagrama](./protocolo.png)

## App do Servidor

1. O usuário cria a Porta, como é pedido no aplicativo

2. Retorna um feedback de conexão

    1. Caso seja conexão positiva:

    Retorna o feedback positivo no terminal, e printa o host, para ser compartilhado para o cliente se conectar

    2. Em caso negativo:

    Retorna apenas uma mensagem de feedback de conexão: Não foi possível criar o servidor.

3. Quando um cliente se conecta, ele vai para um dicionário de clientes.

3. O servidor fica em Loop para receber as mensagens vindas dos clientes conectados.

4. O Thread possui um papel importante para o servidor, pois permite múltiplos acessos de clientes.

5. Caso receba uma mensagem, ele encaminha para a função de tratamento, onde ele envia para os clientes da lista, exceto o cliente que enviou a mensagem.

6. Se não conseguir enviar uma mensagem para um cliente, ele remove o cliente do dicionário.

## App do Cliente

1. O cliente se conecta ao Host e a Porta, como é pedido no aplicativo

2. Retorna um feedback de conexão

    1. Caso seja conexão positiva:

    Retorna o feedback positivo e abre uma outra aba, sendo ela o chat.

    2. Em caso negativo:

    Retorna apenas uma mensagem de feedback de conexão:


3. O cliente pode então digitar e enviar uma mensagem para os clientes que estam conectados à mesma porta.

5. O Thread possui um papel importante para o cliente, pois permite o envio das mensagens do servidor em paralelo com o recebimento de mensagens do servidor.