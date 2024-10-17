from database import Database
import config as cfg

from agents.apache_agent import ApacheAgent
from agents.server_agent import ServerAgent


def main():
    database = Database(
        host = cfg.DB_HOST,
        database_name = cfg.DATABASE_NAME,
        user = cfg.DB_USER,
        password = cfg.DB_PASS
    )

    apache_agent = ApacheAgent(database=database)
    apache_agent.get_data()
    apache_agent.insert_data()



    server_agent = ServerAgent(database=database)
    data = server_agent.get_data()

    server_agent.insert_data(data=data)


if __name__ == '__main__':
    main()
