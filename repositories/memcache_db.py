from pymemcache.client.base import Client
import settings
from singleton import Singleton
from utils import json_deserializer, json_serializer
from entities.ip import IPEntity


class MemcacheRepo(metaclass=Singleton):

    def __init__(self):
        # instantiate the memchached client with the HOST and PORT
        self.__client = Client((settings.HOST, settings.PORT),
                               serializer=json_serializer, deserializer=json_deserializer)

    def save_to_cache(self, ip_entity: IPEntity) -> dict:
        ip = ip_entity.ip_address
        ip_details = {
            'continent': ip_entity.continent,
            'country': ip_entity.country,
            'state': ip_entity.state,
            'longitude': ip_entity.longitude,
            'latitude': ip_entity.latitude,
            'ip_address': ip_entity.ip_address
        }
        self.__client.set(ip, ip_details)
        return ip_details

    def fetch_from_cache(self, ip) -> dict:
        return self.__client.get(ip)
