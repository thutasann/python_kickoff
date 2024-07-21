import platform
import psutil


def get_system_info():
    info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3))} GB"
    }
    return info


system_info = get_system_info()

for key, value in system_info.items():
    print(f"{key}: {value}")
