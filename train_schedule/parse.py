import csv
import datetime
import io
import sys

from .train import Train


time_fmt = '%H:%M'
day_names = ('L', 'Ma', 'Me', 'J', 'V', 'S', 'D')
day_full_names = (
    'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche',
)
days_mapping = {name: i for i, name in enumerate(day_names)}

def load(f=sys.stdin):
    reader = csv.reader(f)
    return map(load_train, reader)


def dump(trains, f=sys.stdout):
    writer = csv.writer(f)
    writer.writerows(map(dump_train, trains))


def load_train(row):
    train_type, train_id, days, *stops = row
    days = {i for d, i in days_mapping.items() if d in days}
    stops = zip(stops[::2], stops[1::2])
    stops = {
        stop: datetime.datetime.strptime(time, time_fmt).time()
        for stop, time in stops
    }
    return Train(train_type, train_id, days, **stops)


def dump_days(days, full=False):
    if full:
        return ', '.join(day_full_names[i] for i in sorted(days))
    else:
        return ''.join(day_names[i] for i in sorted(days))


def dump_train(train):
    row = [train.type, train.id, dump_days(train.days)]
    stops = ((stop, time.strftime(time_fmt)) for stop, time in train)
    return row + [item for pair in stops for item in pair]
