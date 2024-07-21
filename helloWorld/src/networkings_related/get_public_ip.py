import requests


def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip_info = response.json()
        public_ip = ip_info['ip']
    except requests.RequestException:
        public_ip = None
    finally:
        return public_ip


print("Public IP Address: ", get_public_ip())
