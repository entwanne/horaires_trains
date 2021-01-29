import datetime


def diff_time(t1, t2):
    t1 = datetime.datetime.combine(datetime.date.min, t1)
    t2 = datetime.datetime.combine(datetime.date.min, t2)
    # t2 in the next day
    if t2 < t1:
        t2 += datetime.timedelta(days=1)
    return (t2 - t1).total_seconds()


def compute_distances(trains):
    distances = {} # stop -> (max_dist, n_stops, src)
    default = (0, 0, None)

    for train in trains:
        for (src, time_src), (dst, time_dst) in train.iter_parts():
            dist = diff_time(time_src, time_dst)
            distances.setdefault(src, default)
            old_dist, _, _ = distances.get(dst, default)

            if dist > old_dist:
                distances[dst] = dist, 1, src

    return distances


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
    distances = compute_distances(trains)
    normalize_distances(distances)
    return sorted(distances, key=distances.get)
