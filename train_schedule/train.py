from .utils import cls_repr


class Train:
    """
    Representation of a train with multiple stops
    """

    def __init__(self, type, id, days=frozenset(), **stops):
        if len(stops) < 2:
            raise ValueError('At least 2 stops are needed')
        self.type = type
        self.id = id
        self.days = days
        self.stops = stops

    def __repr__(self):
        return cls_repr(type(self), self.type, self.id, self.days, **self.stops)

    def __iter__(self):
        "Iterate over all (stop, stop_time) couples"
        return iter(self.stops.items())

    def iter_parts(self):
        "Iterable over all segments of the trip (couples of stop items)"
        it = iter(self)
        src_item = next(it)
        for dst_item in it:
            yield src_item, dst_item
            src_item = dst_item

    @property
    def departure(self):
        return next(iter(self.stops.keys()))

    @property
    def departure_time(self):
        return next(iter(self.stops.values()))

    @property
    def arrival(self):
        return next(reversed(self.stops.keys()))

    @property
    def arrival_time(self):
        return next(reversed(self.stops.values()))
