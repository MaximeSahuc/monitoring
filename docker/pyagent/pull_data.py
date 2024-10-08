import requests
import mariadb


def connect_db():
    try:
        conn=mariadb.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="root",
            database="monitoring"
        )
        return conn
    except mariadb.Error as errdb:
        print("Error connecting to the database",errdb)

 def check_db():
     conn=connect_db()
    try:
        with conn.cursor() as cursor:
            statement="""CREATE TABLE IF NOT EXISTS `data_webserv` (
  `cpu` float NOT NULL,
  `ramGB` float NOT NULL,
  `disk_used` float NOT NULL,
  `disk_write_speed` float NOT NULL,
  `disk_read_speed` float NOT NULL,
  `dl_speed` float NOT NULL,
  `ul_speed` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;"""
            cursor.execute(statement)
            conn.commit()
    except mariadb.Error as errcrdb:
        print("Error creating table",errcrdb)
    finally:
        conn.close()


def add_data(data):
    conn=connect_db()
    try:
        with conn.cursor() as cursor:
            statement="INSERT INTO data_webserv (cpu, ramGB, disk_used, disk_write_speed, disk_read_speed, dl_speed, ul_speed) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (
                data.get("cpu"),
                data.get("ramGB"),
                data.get("disk_used"),
                data.get("disk_write_speed"),
                data.get("disk_read_speed"),
                data.get("dl_speed"),
                data.get("ul_speed")
            )
            cursor.execute(statement,values)
            conn.commit()
            print("Successfully added entry to database")
    except mariadb.Error as erradddb:
        print("Error adding entry to database", erradddb)
    finally:
        conn.close()

def request_api(url):
    try:
        response_API = requests.get(url,timeout=10)
        response_API.raise_for_status()
        return response_API.json()
    except requests.exceptions.RequestException as errr:
        print ("OOps: Something Else",errr)
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)


url='http://127.0.0.1:8081/status'

api_data=request_api(url)

if api_data:
    check_db()
    add_data(api_data)


