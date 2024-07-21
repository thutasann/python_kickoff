import subprocess


def get_hardware_info_macos():
    try:
        cpu_info = subprocess.check_output(
            'sysctl -n machdep.cpu.brand_string', shell=True, text=True).strip()

        mem_info = subprocess.check_output(
            'sysctl -n hw.memsize', shell=True, text=True).strip()
        mem_info = f"{int(mem_info) / (1024 ** 3):.2f} GB"

        return {
            "CPU": cpu_info,
            "RAM": mem_info
        }
    except subprocess.CalledProcessError as e:
        print(f"An error occured: {e}")
        return {}


hardware_info = get_hardware_info_macos()

for key, value in hardware_info.items():
    print(f"{key}: {value}")
