import mariadb


class Database:

    def __init__(self, host, database_name, user, password, port=3306):
        self.host = host
        self.database_name = database_name
        self.port = port
        self.user = user
        self.password = password

    
    def log(message):
        with open("/var/log/pyagent/logs.txt", "a") as log_file:
            log_file.write(message)
            log_file.close()


    def connect(self, database_name=None):
        try:
            if database_name:
                return mariadb.connect(
                    host = self.host,
                    port = self.port,
                    user = self.user,
                    password = self.password,
                    database = database_name
                )
            else:
                return mariadb.connect(
                    host = self.host,
                    port = self.port,
                    user = self.user,
                    password = self.password,
                    database = database_name
                )
        except mariadb.Error as errdb:
            Database.log("Error connecting to the database" + errdb)
    

    def insert_data(self, database_name, statement, values):
        connection = self.connect(database_name=database_name)

        try:
            with connection.cursor() as cursor:
                cursor.execute(statement, values)
                connection.commit()
        except mariadb.Error as erradddb:
            Database.log("Error adding entry to database", str(erradddb))
        finally:
            connection.close()
    

    def exec(self, statement, database_name=None):
        connection = self.connect(database_name=database_name)

        try:
            with connection.cursor() as cursor:
                cursor.execute(statement)
                connection.commit()
        except mariadb.Error as erradddb:
            Database.log("Error adding entry to database", str(erradddb))
        finally:
            connection.close()
