import psutil

#CPU usage
CPU_usage=psutil.cpu_percent(interval=1)

print(CPU_usage,"%")

#RAM usage
RAM_used=psutil.virtual_memory()[2]
RAM_used_GB=psutil.virtual_memory()[3]/1000000000

print(RAM_used,"%")
print(RAM_used_GB,"GB") 

#Disk usage
disk_command=psutil.disk_usage("/")

disk_total= disk_command.total
disk_used= disk_command.free
disk_free= disk_command.used

print(disk_total)
print(disk_used)
print(disk_free)

#Network usage
