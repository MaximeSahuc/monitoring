import psutil
import time
from flask import *

def get_data():
    ##CPU usage
    CPU_usage=psutil.cpu_percent(interval=1)

    #print("CPU:",CPU_usage,"%")

    ##RAM usage
    RAM_used=psutil.virtual_memory()[2]
    RAM_used_GB=round(psutil.virtual_memory()[3]/1000000000,3)

    #print("RAM:",RAM_used,"%") 

    #Disk usage
    disk_command=psutil.disk_usage("/")

    disk_total=(disk_command.total)/1000000000
    disk_used= (disk_command.used)/1000000000
    disk_free= (disk_command.free)/1000000000
    disk_usage_pourcent=round((disk_used/disk_total)*100,2)

    #print("Disk used:",disk_usage_pourcent,"%")

    ## Disk IO
    disk="nvme1n1"
    IO=psutil.disk_io_counters(perdisk=True, nowrap=True)[disk]
    read1=IO.read_bytes
    write1=IO.write_bytes

    time.sleep(1)

    IO=psutil.disk_io_counters(perdisk=True, nowrap=True)[disk]
    read2=IO.read_bytes
    write2=IO.write_bytes

    read=round((read2-read1)/1024/1024, 3)
    write=round((write2-write1)/1024/1024, 3)

    #print("Read speed:",read,"MB/s")
    #print("Write speed:",write,"MB/s")

    ## Network usage
    interface="eno1"

    net=psutil.net_io_counters(pernic=True, nowrap=True)[interface]
    sent1=net.bytes_sent
    rcv1=net.bytes_recv

    time.sleep(1)

    net=psutil.net_io_counters(pernic=True, nowrap=True)[interface]
    sent2=net.bytes_sent
    rcv2=net.bytes_recv

    net_in=round((rcv2-rcv1)/1024/1024, 3)
    net_out=round((sent2-sent1)/1024/1024, 3)

    #print("Donwload:",net_in,"MB/s")
    #print("Upload:",net_out,"MB/s")

    rawdata = {
    "cpu" : CPU_usage,
    "ramGB" : RAM_used_GB,
    "disk_used" : disk_usage_pourcent,
    "disk_write_speed" : write,
    "disk_read_speed" : read,
    "dl_speed" : net_in,
    "ul_speed" : net_out
    }

    return rawdata


app = Flask(__name__)

@app.route("/status", methods=['GET'])
def api():
    data = get_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=8081)