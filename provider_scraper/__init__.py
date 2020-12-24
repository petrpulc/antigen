from logging import info

from provider_scraper import reservatic


def scrape(url, geojson_feature, up_to):
    if 'scraped' not in geojson_feature:
        geojson_feature['scraped'] = set()
    if 'tests' not in geojson_feature:
        geojson_feature['tests'] = []

    if 'reservatic.com' in url:
        reservatic.scrape(url, geojson_feature, up_to)
    else:
        info("Provider %s not handled", url.split('/')[2])
