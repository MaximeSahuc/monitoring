import psutil
import time

#CPU usage
CPU_usage=psutil.cpu_percent(interval=1)

#print("CPU:",CPU_usage,"%")

#RAM usage
RAM_used=psutil.virtual_memory()[2]
RAM_used_GB=psutil.virtual_memory()[3]/1000000000

#print("RAM:",RAM_used,"%") 

#Disk usage
disk_command=psutil.disk_usage("/")

disk_total=(disk_command.total)/1000000000
disk_used= (disk_command.free)/1000000000
disk_free= (disk_command.used)/1000000000
disk_usage_pourcent=(disk_used/disk_total)*100

#print("Disk:",disk_usage_pourcent,"%")

#Network usage
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

print("Donwload:",net_in,"MB/s")
print("Upload:",net_out,"MB/s")