#!/usr/bin/env python3

import argparse
import json
import pprint
from logging import warning

import dateparser
from geopy.distance import lonlat, distance

from provider_scraper import scrape


def find_in_range(lat, lon, max_range):
    with open('providers.geojson', 'r') as geojson:
        features = json.load(geojson)['features']

    if not features:
        raise ValueError('Empty list of providers')

    for feature in features:
        feature['distance'] = distance(lonlat(*feature['geometry']['coordinates']),
                                       (lat, lon)).km

    features = sorted(features, key=lambda i: i['distance'])
    if features[0]['distance'] > max_range:
        warning('No provider within range, returning the closes one.')
        return [features[0]]
    return [i for i in features if i['distance'] <= max_range]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find nearest free testing capacity')
    parser.add_argument('--lat', type=float, default=50.0877, help='Latitude [degrees]')
    parser.add_argument('--lon', type=float, default=14.4212, help='Longitude [degrees]')
    parser.add_argument('--range', '-r', type=float, default=20, help='Range [km]')
    parser.add_argument('--antigen_only', action='store_true', help='Scrape antigen url only')
    parser.add_argument('--up_to', type=dateparser.parse, default='next week',
                        help='Date limit for scraping (default: next week)')
    args = parser.parse_args()

    providers_in_range = find_in_range(args.lat, args.lon, args.range)
    for provider in providers_in_range:
        url = provider['properties']['url_link']
        if not args.antigen_only and url:
            scrape(url, provider, args.up_to)
        url = provider['properties']['url_link_antigen']
        if url:
            scrape(url, provider, args.up_to)

    pprint.pprint(providers_in_range)
