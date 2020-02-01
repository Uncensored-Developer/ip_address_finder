import requests
import settings


def get_ip_detials(ip_address: str):
    access_key = settings.IPSTACK_ACCESS_KEY
    url = 'http://api.ipstack.com/{ip}?access_key={key}'.format(ip=ip_address, key=access_key)
    r = requests.get(url)
    return r.json()
