from datetime import datetime

import click

import jiff


@click.command()
@click.argument('code')
@click.argument('date')
def fetch(code: str, date: str) -> None:
    try:
        sch_date = datetime.strptime(date, '%Y-%m-%d').date()
        sch = jiff.get_schedule(
            code,
            sch_date
        )
        if sch:
            left, total = jiff.get_nr_of_seats(sch.id)
            click.echo(f'<{sch.title}>({code}): {left} / {total}')
        else:
            click.echo('Schedule code or date are incorrect.')
    except ValueError:
        click.echo('Invalid date format is provided.')
        click.echo('Expected format is 2018-05-04')


if __name__ == '__main__':
    fetch()
