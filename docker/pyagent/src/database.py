
class Database:

    def __init__(self, host, user, password, port=3306):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    
    def print_host(self):
        print(self.host)