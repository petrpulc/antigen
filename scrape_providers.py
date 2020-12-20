#!/usr/bin/env python3
import json

import requests
from bs4 import BeautifulSoup

base_url = 'https://crs.uzis.cz'
table_translation = {'Adresa': 'address',
                     'Upřesnění polohy': 'position',
                     'Telefon': 'phone',
                     'Poznámka': 'note',
                     'Způsob rezervace': 'reservation',
                     'Odkaz na rezervační systém': 'reservation_url'}


def scrape_antigen_providers():
    provider_list = []

    provider_list_page = requests.get(f"{base_url}/Antigen")
    provider_list_soup = BeautifulSoup(provider_list_page.content, 'html.parser')
    for provider_item in provider_list_soup.find_all('a', {'class': 'list__link'}):
        provider_url = f"{base_url}{provider_item['href']}"
        provider_page = requests.get(provider_url)
        provider_soup = BeautifulSoup(provider_page.content, 'html.parser')
        provider_dict = {'uzis_url': provider_url,
                         'name': provider_soup.find('h1').text}
        table = provider_soup.find('div', {'class': 'info'}).find('table')
        for row in table.find_all('tr'):
            cols = row.find_all('td')
            if cols[0].text not in table_translation:
                continue
            key = table_translation[cols[0].text]
            if '_url' in key:
                try:
                    provider_dict[key] = cols[1].find('a')['href']
                except TypeError:
                    pass
            else:
                provider_dict[key] = cols[1].text.strip()
        provider_list.append(provider_dict)
    return provider_list


if __name__ == '__main__':
    providers = scrape_antigen_providers()
    with open('providers.json', 'w') as json_file:
        json.dump(providers, json_file)