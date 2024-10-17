from agents.agent_base import AgentBase

class ApacheAgent(AgentBase):

    def __init__(self, database):
        AgentBase.__init__(
            self,
            agent_name = "Apache2",
            db_table = "apache2",
            database = database,
        )



    def create_db_table(self):
        return


    def get_data(self):
        self.log("Get data")


    def insert_data(self):
        self.log("insert data")