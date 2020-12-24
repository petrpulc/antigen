import json
import re

import dateparser
import requests
from bs4 import BeautifulSoup


def __flatten_ymd(ymd):
    for y in sorted(int(i) for i in ymd):
        for m in sorted(int(i) for i in ymd[str(y)]):
            for d in sorted(int(i) for i in ymd[str(y)][str(m)]):
                yield f'{y}-{m}-{d}'


def __scrape_reservation_page(url, geojson_feature, up_to):
    base_url = url.split('?')[0]
    if base_url in geojson_feature['scraped']:
        return
    geojson_feature['scraped'].add(base_url)

    reservation_page = requests.get(url).content

    form_data = re.search(b"new ReservationForm\\([^,]+, (.*?), '(\\d+)', '(\\d+)'", reservation_page, re.DOTALL)
    if not form_data:
        return

    ymd = json.loads(form_data.group(1))
    provider_id = form_data.group(2).decode()
    event_id = form_data.group(3).decode()

    slots = []

    for date in __flatten_ymd(ymd):
        if dateparser.parse(date) > up_to:
            break
        date_data = requests.get(
            f'https://reservatic.com/public_services/{provider_id}/public_operations/{event_id}/hours?date={date}').json()
        for entry in date_data:
            slots.append({'datetime': dateparser.parse(entry['starts_at']).replace(tzinfo=None),
                          'capacity': entry['free_people']})

    test_details = re.search(b'<tbody>\n.*\n.*\n<td>([^<]*)</td>\n<td>([^<]*)', reservation_page, re.MULTILINE)
    geojson_feature['tests'].append({'type': test_details.group(1).decode(),
                                     'price': test_details.group(2).decode(),
                                     'slots': slots})


def __scrape_signpost(url, geojson_feature, up_to):
    signpost_page_soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    for row in signpost_page_soup.find('table').find('tbody').find_all('tr'):
        __scrape_reservation_page('https://reservatic.com' + row.find('td').find('a')['href'], geojson_feature, up_to)


def scrape(url, geojson_feature, up_to):
    if 'new_reservation' in url:
        __scrape_reservation_page(url, geojson_feature, up_to)
    else:
        __scrape_signpost(url, geojson_feature, up_to)
