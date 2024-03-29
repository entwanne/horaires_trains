import sys

from .parse import time_fmt
from .parse import dump_days


def iter_table(sorted_stops, grouped_trains, filter_days=set(), *, print_days=True):
    header = ['Train']
    if print_days:
        header.append('Jours')
    header.extend(sorted_stops)
    yield header

    for group in grouped_trains:
        yield
        for train in group:
            if not (train.days >= filter_days):
                continue
            row = [f'{train.type} {train.id}']
            if print_days:
                row.append(dump_days(train.days))
            stops = (train.stops.get(stop) for stop in sorted_stops)
            row.extend(time.strftime(time_fmt) if time else '' for time in stops)
            yield row


def print_html_table(*args, file=sys.stdout, **kwargs):
    "Print a list of train groups as a HTML table"
    table = iter_table(*args, **kwargs)
    file.write('<table border="1"><thead>')

    header = next(table)
    file.write(''.join(f'<th>{col}</th>' for col in header))

    file.write('</thead><tbody>')

    split = True
    for row in table:
        if row:
            split = False
            file.write('<tr>')
            head, *row = row
            file.write(f'<th>{head}</th>')
            file.write(''.join(f'<td>{col}</td>' for col in row))
            file.write('</tr>')
        elif not split:
            split = True
            file.write('<tr/>' * 5)

    file.write('</tbody></table>')


def print_html_title(title, file=sys.stdout):
    file.write(f'<h2>{title}</h2>')


def print_html_sep(file=sys.stdout):
    file.write('<hr/>')


def print_md_table(*args, file=sys.stdout, **kwargs):
    header, *rows = list(iter_table(*args, **kwargs))

    col_sizes = [len(col) for col in header]
    for row in rows:
        if row:
            col_sizes = [max(len(col), col_size) for col, col_size in zip(row, col_sizes)]

    def _print_row(row):
        print(' | '.join(col.center(col_size) for col, col_size in zip(row, col_sizes)), file=file)

    def _print_split(c=' '):
        print(f'{c}|{c}'.join(c * col_size for col_size in col_sizes), file=file)

    _print_row(header)
    _print_split('-')

    split = True
    for row in rows:
        if row:
            split = False
            _print_row(row)
        elif not split:
            split = True
            _print_split()
    print(file=file)


def print_md_title(title, file=sys.stdout):
    print(f'## {title}', file=file)
    print(file=file)


def print_md_sep(file=sys.stdout):
    print('-'*80, file=file)
    print(file=file)


def _dispatch_format(funcs):
    def wrapper(*args, format='html', **kwargs):
        return funcs[format](*args, **kwargs)
    return wrapper


print_table = _dispatch_format({
    'html': print_html_table,
    'md': print_md_table,
})
print_title = _dispatch_format({
    'html': print_html_title,
    'md': print_md_title,
})
print_sep = _dispatch_format({
    'html': print_html_sep,
    'md': print_md_sep,
})


def print_day_tables(sorted_stops, grouped_trains, day_groups, **kwargs):
    "Print a list of train groups as HTML tables (with a table for each days set)"
    for day_group in day_groups:
        print_title(dump_days(day_group, full=True), **kwargs)
        print_table(sorted_stops, grouped_trains, filter_days=day_group, print_days=False, **kwargs)
        print_sep(**kwargs)
