
class AgentBase:

    def __init__(self, agent_name, db_table, database):
        self.name = agent_name + " agent"
        self.db_table = db_table
        self.database = database
        self.log_prefix = f"[{self.name}] "
        self.log("Init")
        self.create_db_table()
    

    def create_db_table(self):
        self.log("Creating DB table")
        return


    def get_data(self):
        return


    def insert_data(self):
        return
    

    def update(self):
        self.log("Requesting new data")
        data = self.get_data()
        self.insert_data(data)


    def log(self, text):
        print(self.log_prefix + text)