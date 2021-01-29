import csv
import datetime
import io
import sys

from .train import Train


time_fmt = '%H:%M'


def load(f=sys.stdin):
    reader = csv.reader(f)
    return map(load_train, reader)


def dump(trains, f=sys.stdout):
    writer = csv.writer(f)
    writer.writerows(map(dump_train, trains))


def load_train(row):
    train_type, train_id, days, *stops = row
    stops = zip(stops[::2], stops[1::2])
    stops = {
        stop: datetime.datetime.strptime(time, time_fmt).time()
        for stop, time in stops
    }
    return Train(train_type, train_id, days, **stops)


def dump_train(train):
    row = [train.type, train.id, train.days]
    stops = ((stop, time.strftime(time_fmt)) for stop, time in train)
    return row + [item for pair in stops for item in pair]
