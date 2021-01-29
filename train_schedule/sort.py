import datetime


def diff_time(t1, t2):
    t1 = datetime.datetime.combine(datetime.date.min, t1)
    t2 = datetime.datetime.combine(datetime.date.min, t2)
    # t2 in the next day
    if t2 < t1:
        t2 += datetime.timedelta(days=1)
    return (t2 - t1).total_seconds()


def compute_distances(trains):
    distances_to = {} # stop -> (max_dist, n_stops, src)
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
    def set_absolute_dist(stop):
        dist, n, src = distances[stop]

        if src is not None:
            d, i, src = set_absolute_dist(src)
            dist += d
            n += i
            distances[stop] = dist, n, src

        return dist, n, src

    for stop in list(distances):
        set_absolute_dist(stop)


def get_sorted_stops(trains):
    distances_to, distances_from = compute_distances(trains)
    normalize_distances(distances_to)
    normalize_distances(distances_from)

    def sort_key(key):
        dist1, n1, _ = distances_to[key]
        dist2, n2, _, = distances_from[key]
        return dist1 - dist2, n1 - n2

    return sorted(distances_to, key=sort_key)
