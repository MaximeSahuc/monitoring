from agents.agent_base import AgentBase

class ServerAgent(AgentBase):

    def __init__(self, database, status_url):
        AgentBase.__init__(
            self,
            agent_name = "Web Server",
            db_table = "web_server",
            database = database,
        )
        self.web_server_url = status_url


    def create_db_table(self):
        statement = f"""
            CREATE TABLE IF NOT EXISTS `{self.db_table}` (
            `time` TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
            `cpu` float NOT NULL,
            `ramGB` float NOT NULL,
            `disk_used` float NOT NULL,
            `disk_write_speed` float NOT NULL,
            `disk_read_speed` float NOT NULL,
            `dl_speed` float NOT NULL,
            `ul_speed` float NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4  COLLATE 'utf8mb4_general_ci';
        """

        self.database.exec(
            statement = statement,
            database_name = self.database.database_name,
        )


    def get_data(self):
        import requests

        response = requests.get(
            self.web_server_url,
            timeout = 10
        )

        if response.status_code != 200:
            self.log("Received invalid HTTP status: " + response.status_code)

        return response.json()


    def insert_data(self, data):
        statement = f"""INSERT INTO {self.db_table} (
            cpu,
            ramGB,
            disk_used,
            disk_write_speed,
            disk_read_speed,
            dl_speed,
            ul_speed
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            data.get("cpu"),
            data.get("ramGB"),
            data.get("disk_used"),
            data.get("disk_write_speed"),
            data.get("disk_read_speed"),
            data.get("dl_speed"),
            data.get("ul_speed"),
        )

        self.database.insert_data(
            database_name = self.database.database_name,
            statement = statement,
            values = values,
        )
