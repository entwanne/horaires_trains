import argparse
import sys

from . import parse
from .group import get_day_groups
from .group import group_trains
from .print import print_table
from .print import print_day_tables
from .sort import get_sorted_stops


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('--output', '-o', type=argparse.FileType('w'), default=sys.stdout)
    parser.add_argument('--format', '-f', choices=('md', 'html'), default=None)
    parser.add_argument('--unify-days', '-u', action='store_true')
    args = parser.parse_args()
    if args.format is None:
        args.format = 'html' if args.output.name.endswith('.html') else 'md'
    return args


def main():
    args = get_args()
    trains = list(parse.load(args.input))
    sorted_stops = get_sorted_stops(trains)
    grouped_trains = group_trains(trains, sorted_stops)
    if not args.unify_days:
        day_groups = get_day_groups(trains)
    if args.unify_days:
        print_table(sorted_stops, grouped_trains, format=args.format, file=args.output)
    else:
        print_day_tables(sorted_stops, grouped_trains, day_groups, format=args.format, file=args.output)


if __name__ == '__main__':
    main()
