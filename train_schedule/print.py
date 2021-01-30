import sys

from .parse import time_fmt
from .parse import dump_days


def print_table(sorted_stops, grouped_trains, filter_days=set(), f=sys.stdout,
                print_days=True):
    "Print a list of train groups as a HTML table"
    f.write('<table border="1"><thead>')
    f.write('<th>Train</th>')
    if print_days:
        f.write('<th>Jours</th>')
    for stop in sorted_stops:
        f.write(f'<th>{stop}</th>')
    f.write('</thead><tbody>')
    for group in grouped_trains:
        f.write('<tr/>'*5)
        for train in group:
            if not (train.days >= filter_days):
                continue
            f.write('<tr>')
            f.write(f'<th>{train.type} {train.id}</th>')
            if print_days:
                f.write(f'<th>{dump_days(train.days)}</th>')
            for stop in sorted_stops:
                time = train.stops.get(stop, '')
                if time:
                    time = time.strftime(time_fmt)
                f.write(f'<td>{time}</td>')
            f.write('</tr>')
    f.write('</tbody></table>')


def print_day_tables(sorted_stops, grouped_trains, day_groups, f=sys.stdout):
    "Print a list of train groups as HTML tables (with a table for each days set)"
    for day_group in day_groups:
        f.write(f'<h2>{dump_days(day_group, full=True)}</h2>')
        print_table(sorted_stops, grouped_trains, day_group, f, print_days=False)
        f.write('<hr/>')
