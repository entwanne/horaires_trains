from .utils import grouper


def get_next_train(train, trains):
    trains = [t for t in trains if t.departure_time > train.arrival_time]
    if trains:
        return min(trains, key=lambda t: t.departure_time)


def get_prev_train(train, trains):
    trains = [t for t in trains if t.arrival_time < train.departure_time]
    if trains:
        return max(trains, key=lambda t: t.arrival_time)


def group_trains(trains, sorted_stops):
    trains_from_stop = {stop: [] for stop in sorted_stops}
    trains_to_stop = {stop: [] for stop in sorted_stops}

    with grouper() as g:
        for train in trains:
            g.add(train, train.departure_time)
            for (src, _), (dst, _) in train.iter_parts():
                trains_from_stop[src].append(train)
                trains_to_stop[dst].append(train)

        for stop in sorted_stops:
            for train in trains_from_stop[stop]:
                next_train = get_next_train(train, trains_from_stop[train.arrival])
                if next_train:
                    g.merge(train, next_train)

            for train in trains_to_stop[stop]:
                prev_train = get_prev_train(train, trains_to_stop[train.departure])
                if prev_train:
                    g.merge(prev_train, train)

        grouped_trains = {
            time: sorted(trains, key=lambda t: (t.arrival_time, t.departure_time))
            for time, trains in g.groups()
        }
        return [trains for _, trains in sorted(grouped_trains.items())]
