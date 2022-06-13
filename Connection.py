import socket


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Pour que cela fonctionne sur votre machine, cette adresse doit être égale à l'adresse ipv4 de la machine qui exécute le serveur.
        # Vous pouvez trouver cette adresse en tapant ipconfig dans CMD et en copiant l'adresse ipv4. Encore une fois, cette adresse doit être celle du serveur
        # adresse ipv4 du serveur. Ce champ sera le même pour tous vos clients.
        
        self.host =  '192.168.31.183'
        self.port = 5050
        self.addr = (self.host, self.port)
        self.id = self.connect()

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            self.client.send(str.encode(data))
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)

