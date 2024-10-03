import requests
import json
import mariadb


def connect_db():
    try:
        conn=mariadb.connect(
            host="localhost",
            port="3306",
            user="user",
            password="user"
        )
    except mariadb.Error as errdb:
        print("Error connecting to the database",errdb)


def add_data():
    try:
        cursor=mariadb.cursor()
        statement="INSERT INTO <table> (cpu, ramGB, disk_used, disk_write_speed, disk_read_speed, dl_speed, ul_speed) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (
            data["cpu"],
            data["ramGB"],
            data["disk_used"],
            data["disk_write_speed"],
            data["disk_read_speed"],
            data["dl_speed"],
            data["ul_speed"]
        )
        cursor.execute(statement,values)
        mariadb.commit()
        print("Successfully added entry to database")
    except mariadb.Error as erradddb:
        print("Error adding entry to database", erradddb)



try:
    response_API = requests.get('http://127.0.0.1:8081/status')
    response_API.raise_for_status()
    print(response_API.json())
except requests.exceptions.RequestException as errr:
    print ("OOps: Something Else",errr)
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)


data=json.load(response_API)
connect_db()
add_data(data)

