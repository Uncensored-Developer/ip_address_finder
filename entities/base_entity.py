import attr


class Entity:
    """
    Base class for all entities.
    """

    def replace(self, **kwargs):
        """Return new instance of this entity with updated field."""
        return attr.assoc(self, **kwargs)

    def as_dict(self):
        """Return class attributes in a dictionary."""
        return attr.asdict(self)
