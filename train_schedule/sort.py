import datetime


def diff_time(t1, t2):
    "Compute difference between two time objects"
    t1 = datetime.datetime.combine(datetime.date.min, t1)
    t2 = datetime.datetime.combine(datetime.date.min, t2)
    # t2 in the next day
    if t2 < t1:
        t2 += datetime.timedelta(days=1)
    return (t2 - t1).total_seconds()


def compute_distances(trains):
    """
    Compute minimal distances to neighboring stops (previous & next)
    for all stops
    Return two distances dicts (minimal distances to stop & from stop)

    compute_distances([
        Train(viridian=time(10), pewter=time(20)),
        Train(viridian=time(10), pewter=time(30)),
        Train(pewter=time(50), cerulean=time(80)),
    ])
    => (
        {
            'viridian': (0, 0, None),
            'pewter': (10, 1, 'viridian'),
            'cerulean': (30, 1, 'pewter'),
        },
        {
            'cerulean': (0, 0, None),
            'pewter': (30, 1, 'cerulean'),
            'viridian': (10, 1, 'pewter'),
        },
    )
    """
    # {stop: (min_dist, n_stops, src/dst)}
    # stop = current stop
    # min_dist = minimal distance from/to other stop
    # n_stops = number of stop along the way (1 for neighboring stops)
    # src/dst = origin/target stop (None if not defined)
    distances_to = {}
    distances_from = {}
    default = (0, 0, None)

    for train in trains:
        for (src, time_src), (dst, time_dst) in train.iter_parts():
            dist = diff_time(time_src, time_dst)
            distances_to.setdefault(src, default)
            distances_from.setdefault(dst, default)

            old_dist, _, _ = distances_to.get(dst, default)
            if not old_dist or dist < old_dist:
                distances_to[dst] = dist, 1, src

            old_dist, _, _ = distances_from.get(src, default)
            if not old_dist or dist < old_dist:
                distances_from[src] = dist, 1, dst

    return distances_to, distances_from


def normalize_distances(distances):
    """
    Normalize a distances dict
    Re-compute the distances to make them absolute from departure.arrival

    normalize_distances({
        'viridian': (0, 0, None),
        'pewter': (10, 1, 'viridian'),
        'cerulean': (30, 1, 'pewter'),
    })
    => {
        'viridian': (0, 0, None),
        'pewter': (10, 1, None),
        'cerulean': (40, 2, None),
    }
    """
    def set_absolute_dist(stop):
        # Walk recursively through stops to update min_dist & n_stops
        dist, n, src = distances[stop]

        if src is not None:
            d, i, src = set_absolute_dist(src)
            dist += d
            n += i
            distances[stop] = dist, n, src

        return dist, n, src

    for stop in list(distances):
        set_absolute_dist(stop)

    return distances


def get_sorted_stops(trains):
    """
    Get a sorted list of all stops by computing distances

    get_sorted_stops([
        Train(viridian=time(10), pewter=time(20)),
        Train(viridian=time(10), pewter=time(30)),
        Train(pewter=time(50), cerulean=time(80)),
    ])
    => ['viridian', 'pewter', 'cerulean']
    """
    distances_to, distances_from = compute_distances(trains)
    normalize_distances(distances_to)
    normalize_distances(distances_from)

    def sort_key(key):
        # Stops are sorted by closest from departure & furthest from arrival
        dist1, n1, _ = distances_to[key]
        dist2, n2, _, = distances_from[key]
        return dist1 - dist2, n1 - n2

    return sorted(distances_to, key=sort_key)
