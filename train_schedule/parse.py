import csv
import datetime
import sys

from .train import Train


time_fmt = '%H:%M'
day_names = ('L', 'Ma', 'Me', 'J', 'V', 'S', 'D')
day_full_names = (
    'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche',
)
days_mapping = {name: i for i, name in enumerate(day_names)}


def load(f=sys.stdin):
    "Load trains from a CSV file"
    reader = csv.reader(f)
    return map(load_train, reader)


def dump(trains, f=sys.stdout):
    "Dump trains to a CSV file"
    writer = csv.writer(f)
    writer.writerows(map(dump_train, trains))


def load_train(row):
    """
    Load train from a row

    load_train(['T', '#1', 'SD', 'viridian', '12:30', 'pewter', '13:00', 'cerulean', '14:00'])
    => Train('T', '#1', {5, 6}, viridian=time(12, 30), pewter=time(13, 0), cerulean=time(14, 0))
    """
    train_type, train_id, days, *stops = row
    days = {i for d, i in days_mapping.items() if d in days}
    stops = zip(stops[::2], stops[1::2])
    stops = {
        stop: datetime.datetime.strptime(time, time_fmt).time()
        for stop, time in stops
    }
    return Train(train_type, train_id, days, **stops)


def dump_days(days, full=False):
    "Get printable format for days set"
    if full:
        return ', '.join(day_full_names[i] for i in sorted(days))
    else:
        return ''.join(day_names[i] for i in sorted(days))


def dump_train(train):
    """
    Dump a row from a train

    dump_train(Train('T', '#1', {5, 6}, viridian=time(12, 30), pewter=time(13, 0), cerulean=time(14, 0)))
    => ['T', '#1', 'SD', 'viridian', '12:30', 'pewter', '13:00', 'cerulean', '14:00']
    """
    row = [train.type, train.id, dump_days(train.days)]
    stops = ((stop, time.strftime(time_fmt)) for stop, time in train)
    return row + [item for pair in stops for item in pair]
