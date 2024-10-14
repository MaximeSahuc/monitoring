import requests
import mariadb

DB_HOST = "db"
DB_PORT = 3306
DB_USER = "root"
DB_PASS = "root"
DATABASE_NAME = "monitoring"


def log(message):
    with open("/var/log/pyagent/logs.txt", "a") as log_file:
        log_file.write(message)
        log_file.close()


def connect_db(database=None):
    try:
        if database:
            return mariadb.connect(
                host = DB_HOST,
                port = DB_PORT,
                user = DB_USER,
                password = DB_PASS,
                database = DATABASE_NAME
            )
        else:
            return mariadb.connect(
                host = DB_HOST,
                port = DB_PORT,
                user = DB_USER,
                password = DB_PASS,
            )
    except mariadb.Error as errdb:
        log("Error connecting to the database" + errdb)


def check_db():
    conn = connect_db()

    #  Create database
    with conn.cursor() as cursor:
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS `monitoring` COLLATE 'utf8mb4_general_ci';")
            conn.commit()
        except Exception as err:
            log(str(err))
            exit()
        finally:
            conn.close()
    
    #  Create table
    conn = connect_db(database=DATABASE_NAME)
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS `data_webserv` (
                `cpu` float NOT NULL,
                `ramGB` float NOT NULL,
                `disk_used` float NOT NULL,
                `disk_write_speed` float NOT NULL,
                `disk_read_speed` float NOT NULL,
                `dl_speed` float NOT NULL,
                `ul_speed` float NOT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4  COLLATE 'utf8mb4_general_ci';
                """
            )
            conn.commit()
        except Exception as err:
            error = True
            log(str(err))
            exit()
        finally:
            conn.close()


def add_data(data):
    conn = connect_db(database=DATABASE_NAME)
    try:
        with conn.cursor() as cursor:
            statement = "INSERT INTO data_webserv (cpu, ramGB, disk_used, disk_write_speed, disk_read_speed, dl_speed, ul_speed) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (
                data.get("cpu"),
                data.get("ramGB"),
                data.get("disk_used"),
                data.get("disk_write_speed"),
                data.get("disk_read_speed"),
                data.get("dl_speed"),
                data.get("ul_speed")
            )
            cursor.execute(statement, values)
            conn.commit()
            log("Successfully added entry to database")
    except mariadb.Error as erradddb:
        log("Error adding entry to database", str(erradddb))
        exit()
    finally:
        conn.close()

def request_api(url):
    try:
        response_API = requests.get(url,timeout=10)
        response_API.raise_for_status()
        return response_API.json()
    except requests.exceptions.RequestException as errr:
        log ("OOps: Something Else \n" + str(errr))
    except requests.exceptions.HTTPError as errh:
        log ("Http Error: \n" + str(errh))
    except requests.exceptions.ConnectionError as errc:
        log ("Error Connecting: \n" + str(errc))
    except requests.exceptions.Timeout as errt:
        log ("Timeout Error: \n" + str(errt))


def main():
    from time import sleep
    web_server_url='http://172.16.69.10:8081/status'
    sleep_time = 1 * 60  # 1 minute

    log("Starting monitoring agent")

    check_db()

    while True:
        api_data=request_api(web_server_url)

        if api_data:
            add_data(api_data)
        else:
            log("Error: no data received from server !")
        
        sleep(sleep_time)


if __name__ == "__main__":
    main()
