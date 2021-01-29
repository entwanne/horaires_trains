import sys

from .parse import time_fmt
from .parse import dump_days


def print_table(sorted_stops, grouped_trains, f=sys.stdout):
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
            f.write(f'<th>{train.type} {train.id}</th><th>{dump_days(train.days)}</th>')
            for stop in sorted_stops:
                time = train.stops.get(stop, '')
                if time:
                    time = time.strftime(time_fmt)
                f.write(f'<td>{time}</td>')
            f.write('</tr>')
    f.write('</tbody></table>')
