import argparse
import sys

from parse import load
from groups import grouper
from sort import get_sorted_stops


parser = argparse.ArgumentParser()

parser.add_argument('--input', '-i', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('--output', '-o', type=argparse.FileType('w'), default=sys.stdout)

args = parser.parse_args()
trains = list(load(args.input))


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


sorted_stops = get_sorted_stops(trains)
grouped_trains = group_trains(trains, sorted_stops)


def print_table(grouped_trains, f=sys.stdout):
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


print_table(grouped_trains, args.output)
