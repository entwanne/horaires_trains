from .utils import grouper


def get_day_groups(trains):
    """
    Get a list of all distinctive sets of days

    get_day_groups([
        Train(days={1, 2, 3}),
        Train(days={0, 1}),
        Train(days={4}),
    ])
    => [{0}, {1}, {2, 3}, {4}]
    """
    day_sets = {frozenset(train.days) for train in trains}
    all_days = frozenset.union(*day_sets)
    groups = {all_days}

    for day_set in day_sets:
        couples = ((group & day_set, group - day_set) for group in groups)
        groups = {group for couple in couples for group in couple if group}

    return sorted(groups, key=tuple)


def get_next_train(train, trains):
    "Get direct/earliest connection after a train"
    trains = [t for t in trains if t.departure_time > train.arrival_time]
    if trains:
        return min(trains, key=lambda t: t.departure_time)


def get_prev_train(train, trains):
    "Get direct/latest connection before a train"
    trains = [t for t in trains if t.arrival_time < train.departure_time]
    if trains:
        return max(trains, key=lambda t: t.arrival_time)


def group_trains(trains, sorted_stops):
    """
    Group trains by connections
    All trains that are connected belong to a same group
    Return sorted groups as lists of trains

    group_trains([
        Train('T', '#1', viridian=time(12, 30), pewter=time(13, 0)),
        Train('T', '#2', viridian=time(16, 0), pewter=time(16, 30)),
        Train('T', '#3', pewter=time(13, 30), cerulean=time(14, 30)),
        Train('T', '#4', pewter=time(17, 0), cerulean=time(18, 0)),
    ], ['viridian', 'pewter', 'cerulean'])
    => [
        [Train('T', '#1', ...), Train('T', '#3', ...)],
        [Train('T', '#2', ...), Train('T', '#4', ...)],
    ]
    """
    trains_from_stop = {stop: [] for stop in sorted_stops}
    trains_to_stop = {stop: [] for stop in sorted_stops}

    with grouper() as g:
        for train in trains:
            # Groups are associated to a departure time
            # when merged, groups get associated to earlier departure times
            g.add(train, train.departure_time)
            trains_from_stop[train.departure].append(train)
            trains_to_stop[train.arrival].append(train)

        for stop in sorted_stops:
            # Connect each train with next one
            for train in trains_from_stop[stop]:
                next_train = get_next_train(train, trains_from_stop[train.arrival])
                if next_train:
                    g.merge(train, next_train)

            # Connect each train with previous one
            for train in trains_to_stop[stop]:
                prev_train = get_prev_train(train, trains_to_stop[train.departure])
                if prev_train:
                    g.merge(prev_train, train)

        # Sort trains in groups by time of arrival & departure
        grouped_trains = {
            time: sorted(trains, key=lambda t: (t.departure_time, t.arrival_time))
            for time, trains in g.groups()
        }
        # Sort groups by departure time of the first train
        return [trains for _, trains in sorted(grouped_trains.items())]
