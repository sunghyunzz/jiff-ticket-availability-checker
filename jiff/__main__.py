from datetime import datetime
from typing import Optional

import click

from jiff import get_nr_of_seats, get_schedule
from jiff.slack import send_msg


def handle_slack(
    slack_url: Optional[str],
    slack_channel: Optional[str],
    msg: str
) -> None:
    if slack_url and slack_channel:
        sent = send_msg(
            slack_url,
            slack_channel,
            msg
        )
        if sent:
            click.echo('Just sent Slack message!')
        else:
            click.echo('Sending Slack message failed!')
    elif slack_url and not slack_channel:
        click.echo('Slack URL is provided but channel is not given.')
    elif not slack_url and slack_channel:
        click.echo('Slack channel is provided but URL is not given.')


@click.command()
@click.argument('code')
@click.argument('date')
@click.option('--slack-url', help='Your Slack incoming webhook URL.')
@click.option('--slack-channel', help='Your Slack channel for webhook.')
def fetch(
    code: str,
    date: str,
    slack_url: Optional[str],
    slack_channel: Optional[str]
) -> None:
    try:
        sch_date = datetime.strptime(date, '%Y-%m-%d').date()
        sch = get_schedule(
            code,
            sch_date
        )
        if sch:
            left, total = get_nr_of_seats(sch.id)
            msg = f'<{sch.title}>({code}): {left} / {total}'

            click.echo(msg)
            if left > 0:
                handle_slack(slack_url, slack_channel, msg)
        else:
            click.echo('Schedule code or date are incorrect.')
    except ValueError:
        click.echo('Invalid date format is provided.')
        click.echo('Expected format is 2018-05-04')


if __name__ == '__main__':
    fetch()
