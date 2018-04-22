import re
from datetime import date
from typing import Optional, Tuple, Union

import requests

BASE_URL = 'https://www.xticket.co.kr/MPTicketing/InfoWS'
SCHEDULE_INFO_URL = f'{BASE_URL}/RIA.asmx/GetScheduleCodeShort'
NR_OF_SEATS_URL = f'{BASE_URL}/INFO.asmx/GetAreaMapHTML'

COUNT_REGEX = re.compile('<count>(\d+)</count>')
TOTAL_COUNT_REGEX = re.compile('<totalCount>(\d+)</totalCount>')

SCHEDULE_ID_REGEX = re.compile('<sId>(\d+)</sId>')
TITLE_KR_REGEX = re.compile('<ttK>(.+)</ttK>')


class Schedule:

    def __init__(self, title: str, _id: str) -> None:
        self.title = title
        self.id = _id


def get_schedule(
    schedule_code: Union[int, str],
    schedule_date: date
) -> Optional[Schedule]:
    form = {
        'companyCd': 'SP0010',
        'storeCd': '01',
        'planCompanyCd': 'PN0037',
        'playYMD': schedule_date.strftime('%Y%m%d'),
        'scheCd': str(schedule_code)
    }
    r = requests.post(SCHEDULE_INFO_URL, data=form)
    raw_text = r.text

    try:
        return Schedule(
            TITLE_KR_REGEX.search(raw_text).group(1),
            SCHEDULE_ID_REGEX.search(raw_text).group(1)
        )
    except AttributeError:
        return None


def get_nr_of_seats(schedule_id: str) -> Tuple[int, int]:
    form = {
        'scheduleId': schedule_id,
        'storeCd': '01',
        'riaType': 'G'
    }
    r = requests.post(NR_OF_SEATS_URL, data=form)

    left_nr_of_seats = int(COUNT_REGEX.search(r.text).group(1))
    total_nr_of_seats = int(TOTAL_COUNT_REGEX.search(r.text).group(1))

    return left_nr_of_seats, total_nr_of_seats
