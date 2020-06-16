class Server:
    def __init__(self):
        self.users = dict()

    def __setitem__(self, key, value):
        self.users[key] = value

    def __getitem__(self, item):
        return self.users[item]

    def __delitem__(self, item):
        del(self.users[item])


class Client:
    def __init__(self, server, user):
        server[user] = []
        self.user = user
        self.server = server

    def receive_mail(self):
        em = self.server[self.user]
        self.server[self.user] = []
        return em

    def send_mail(self, server, user, message):
        if user in server:
            server[user].append(message)
        else:
            server[user] = [message]


server1 = Server()
us1 = Client(server1, "Extroot")
us2 = Client(server1, "Russia9")
us1.send_mail(server1, "Russia9", "Xd")
us1.send_mail(server1, "Russia9", "LoL")
print(us2.receive_mail())
print(us2.receive_mail())
us2.send_mail(server1, "Extroot", "123")
print(us1.receive_mail())