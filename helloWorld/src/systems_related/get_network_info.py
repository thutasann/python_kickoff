
import psutil


def get_network_info():
    interfaces = psutil.net_if_addrs()
    network_info = {}
    for interface, addrs in interfaces.items():
        network_info[interface] = [
            addr.address for addr in addrs if addr.family == psutil.AF_LINK]
    return network_info


network_info = get_network_info()
for interface, addrs in network_info.items():
    print(f"{interface}: {', '.join(addrs)}")
