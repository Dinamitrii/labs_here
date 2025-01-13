import psutil
# bytes to GB ==> multiply by (1024**3)
# bytes to MB ==> multiply by (1024**2)
def get_system_info():

# For CPU Usage
    cpu_usage = psutil.cpu_percent()
    print(f"CPU Usage: {cpu_usage}%")

# Memory Usage
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")
    print(f"Memory Total: {memory.total / (1024 ** 3):.2f}GB")
    print(f"Memory Used: {memory.used / (1024 ** 3):.2f}GB")
    print(f"Memory Free: {memory.free / (1024 ** 3):.2f}GB")
    print(f"Memory Available: {memory.available / (1024 ** 3):.2f}GB")

# Disk Usage
    disk = psutil.disk_usage("/")
    print(f"Disk Usage: {disk.percent}%")
    print(f"Disk Total: {disk.total / (1024 ** 3):.2f}GB")
    print(f"Disk Used: {disk.used / (1024 ** 3):.2f}GB")
    print(f"Disk Free: {disk.free / (1024 ** 3):.2f}GB")

# Network Usage
    network = psutil.net_io_counters()
    print(f"Network Usage: {network.bytes_sent / (1024 ** 2):.2f}MB")
    print(f"Network Usage: {network.bytes_recv / (1024 ** 2):.2f}MB")

get_system_info()
