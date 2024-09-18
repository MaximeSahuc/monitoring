import psutil

#CPU usage
CPU_usage=psutil.cpu_percent()

print(CPU_usage)

#RAM usage
RAM_used=psutil.virtual_memory()[2]
RAM_used_GB=psutil.virtual_memory()[3]/1000000000

print(RAM_used,"%")
print(RAM_used_GB,"GB") 