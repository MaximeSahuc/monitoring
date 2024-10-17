from agents.agent_base import AgentBase

class ApacheAgent(AgentBase):

    def __init__(self, database, status_url):
        AgentBase.__init__(
            self,
            agent_name = "Apache2",
            db_table = "apache2",
            database = database,
        )
        self.status_url = status_url


    def create_db_table(self):
        statement = f"""
            CREATE TABLE IF NOT EXISTS `{self.db_table}` (
            `time` TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
            `uptime` varchar(50) NOT NULL,
            `load_1` float NOT NULL,
            `load_5` float NOT NULL,
            `load_15` float NOT NULL,
            `cpu_load` float NOT NULL,
            `req_per_sec` float NOT NULL,
            `bytes_per_sec` float NOT NULL,
            `duration_per_req` float NOT NULL,
            `busy_workers` int NOT NULL,
            `idle_workders` int NOT NULL,
            `processes` int NOT NULL,
            `conn_total` int NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4  COLLATE 'utf8mb4_general_ci';
        """

        self.database.exec(
            statement = statement,
            database_name = self.database.database_name,
        )


    def _parse_raw_data(self, data):
        lines = data.splitlines()
        parsed_data = {}

        for index, line in enumerate(lines):
            if index == 0:
                continue

            split = line.split(": ")

            if len(split) != 2:
                print("Invalid split")

            key, value = split

            parsed_data.update(
                {key: value}
            )

        return parsed_data


    def get_data(self):
        import requests

        response = requests.get(
            self.status_url,
            timeout = 10
        )

        if response.status_code != 200:
            self.log("Received invalid HTTP status: " + response.status_code)

        parsed_data = self._parse_raw_data(response.text)

        return parsed_data


    def insert_data(self, data):
        statement = f"""INSERT INTO `{self.db_table}` (
            `uptime`,
            `load_1`,
            `load_5`,
            `load_15`,
            `cpu_load`,
            `req_per_sec`,
            `bytes_per_sec`,
            `duration_per_req`,
            `busy_workers`,
            `idle_workders`,
            `processes`,
            `conn_total`
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        values = (
            data.get("ServerUptime"),
            data.get("Load1"),
            data.get("Load5"),
            data.get("Load15"),
            data.get("CPULoad"),
            data.get("ReqPerSec"),
            data.get("BytesPerSec"),
            data.get("DurationPerReq"),
            data.get("BusyWorkers"),
            data.get("IdleWorkers"),
            data.get("Processes"),
            data.get("ConnsTotal"),
        )

        self.database.insert_data(
            database_name = self.database.database_name,
            statement = statement,
            values = values,
        )
