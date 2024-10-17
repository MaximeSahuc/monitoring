from database import Database
import config as cfg

from agents.apache_agent import ApacheAgent
from agents.server_agent import ServerAgent


database = Database(
    host = cfg.DB_HOST,
    database_name = cfg.DATABASE_NAME,
    user = cfg.DB_USER,
    password = cfg.DB_PASS
)

monitoring_agents = [
    ApacheAgent(database=database, status_url=cfg.WEBSERV_APACHE2_STATUS_URL),
    ServerAgent(database=database, status_url=cfg.WEBSERV_SYSTEM_STATUS_URL),
]


def main():
    from time import sleep

    while True:
        for agent in monitoring_agents:
            agent.update()
        
        sleep(cfg.AGENT_REQUEST_INTERVAL)


if __name__ == '__main__':
    main()
