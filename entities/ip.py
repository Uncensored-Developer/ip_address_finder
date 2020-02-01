import attr
from.base_entity import Entity


@attr.s(frozen=True)
class IPEntity(Entity):
    ip_address = attr.ib(default=None)
    continent = attr.ib(default=None)
    country = attr.ib(default=None)
    state = attr.ib(default=None)
    longitude = attr.ib(default=None)
    latitude = attr.ib(default=None)
