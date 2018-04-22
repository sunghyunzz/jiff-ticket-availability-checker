import json

import requests


def send_msg(url: str, channel: str, msg: str) -> bool:
    form = {
        'payload': json.dumps({
            'channel': channel if channel.startswith('#') else f'#{channel}',
            'username': 'JIFF Ticket Bot',
            'text': msg,
            'icon_emoji': ':film_projector:'
        })
    }

    r = requests.post(url, data=form)
    return r.status_code == 200
