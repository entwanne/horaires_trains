import datetime

from data import aller


def diff_time(t1, t2):
    return (datetime.datetime.combine(datetime.date.min, t2) - datetime.datetime.combine(datetime.date.min, t1)).total_seconds()

graph = {}
for train in aller:
    (src, time_src), *stops = train
    for dst, time_dst in stops:
        subgraph = graph.setdefault(src, {})
        subgraph[dst] = max(diff_time(time_src, time_dst), subgraph.get(dst, 0))
        src, time_src = dst, time_dst

all_dests = set.union(*(set(g.keys()) for g in graph.values()))
all_stops = graph.keys() | all_dests
departure, = all_stops - all_dests

points = {}

def set_points(src, point=0):
    points[src] = max(point, points.get(src, 0))
    for stop, dist in graph.get(src, {}).items():
        set_points(stop, point+dist)

set_points(departure)
sorted_stops = sorted(all_stops, key=points.get)

trains_from_stop = {stop: [] for stop in sorted_stops}
trains_to_stop = {stop: [] for stop in sorted_stops}
for train in aller:
    (src, _), *stops = train
    for dst, _ in stops:
        trains_from_stop[src].append(train)
        trains_to_stop[dst].append(train)
        src = dst

from groups import grouper

with grouper() as g:
    for i, train in enumerate(aller):
        g.add(train, train.departure_time)

    for stop in sorted_stops:
        for train in trains_from_stop.get(stop, ()):
            next_trains = [t for t in trains_from_stop[train.arrival] if t.departure_time > train.arrival_time]
            if next_trains:
                next_train = min(next_trains, key=lambda t: t.departure_time)
                g.merge(train, next_train)
        for train in trains_to_stop.get(stop, ()):
            prev_trains = [t for t in trains_to_stop[train.departure] if t.arrival_time < train.departure_time]
            if prev_trains:
                prev_train = max(prev_trains, key=lambda t: t.arrival_time)
                g.merge(prev_train, train)

    grouped_trains = {
        time: sorted(trains, key=lambda t: (t.arrival_time, t.departure_time))
        for time, trains in g.groups()
    }
    grouped_trains = [trains for _, trains in sorted(grouped_trains.items())]

with open('/tmp/fiche.html', 'w') as f:
    f.write('<table border="1"><thead>')
    f.write('<th>Train</th><th>Jours</th>')
    for stop in sorted_stops:
        f.write(f'<th>{stop}</th>')
    f.write('</thead><tbody>')
    for group in grouped_trains:
        f.write('<tr/>'*5)
        for train in group:
            #if 'L' not in train.days: continue
            f.write('<tr>')
            f.write(f'<th>{train.type} {train.id}</th><th>{train.days}</th>')
            for stop in sorted_stops:
                time = train.stops.get(stop, '')
                if time:
                    time = time.strftime('%H:%M')
                f.write(f'<td>{time}</td>')
            f.write('</tr>')
    f.write('</tbody></table>')
