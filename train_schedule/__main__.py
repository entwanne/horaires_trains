import argparse
import sys

from . import parse
from .group import get_day_groups
from .group import group_trains
from .print import print_day_tables
from .sort import get_sorted_stops


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('--output', '-o', type=argparse.FileType('w'), default=sys.stdout)
    return parser.parse_args()


def main():
    args = get_args()
    trains = list(parse.load(args.input))
    day_groups = get_day_groups(trains)
    sorted_stops = get_sorted_stops(trains)
    grouped_trains = group_trains(trains, sorted_stops)
    print_day_tables(sorted_stops, grouped_trains, day_groups, args.output)


if __name__ == '__main__':
    main()
