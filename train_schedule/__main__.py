import argparse
import sys

from . import parse
from .group import group_trains
from .print import print_table
from .sort import get_sorted_stops


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('--output', '-o', type=argparse.FileType('w'), default=sys.stdout)
    return parser.parse_args()


def main():
    args = get_args()
    trains = list(parse.load(args.input))
    sorted_stops = get_sorted_stops(trains)
    grouped_trains = group_trains(trains, sorted_stops)
    print_table(sorted_stops, grouped_trains, args.output)


if __name__ == '__main__':
    main()
