from entities.ip import IPEntity


class SaveToMemcacheInteracor:

    def __init__(self, memcache_repo=None, ip_validator=None):
        self.memcache_repo = memcache_repo
        self.ip_validator = ip_validator

    def set_params(self, ip_address, continent, country, state, longitude, latitude):
        self.ip_address = ip_address
        self.continent = continent
        self.country = country
        self.state = state
        self.longitude = longitude
        self.latitude = latitude
        return self

    def execute(self):
        ip_entity = IPEntity(
            ip_address=self.ip_address,
            continent=self.continent,
            country=self.country,
            state=self.state,
            longitude=self.longitude,
            latitude=self.latitude
        )
        result_dict = self.memcache_repo.save_to_cache(ip_entity)
        ip_entity = IPEntity()
        return ip_entity.replace(result_dict)


class FetchFromMemcacheInteractor:

    def __init__(self, memcache_repo=None):
        self.memcache_repo = memcache_repo

    def set_params(self, ip):
        self.ip = ip
        return self

    def execute(self):
        result_dict = self.memcache_repo.fetch_from_cache(self.ip)
        ip_entity = IPEntity()
        return ip_entity.replace(result_dict)
