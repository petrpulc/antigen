import json
import re

with open('providers.json') as infile:
    data = json.load(infile)

for provider in data:
    if 'lat' not in provider:
        print(provider['address'])
        wgs84 = input('WGS84: ')
        parsed = re.match(r'(\d+.\d+)N, (\d+.\d+)E', wgs84)
        provider['lat'] = float(parsed.group(1))
        provider['lon'] = float(parsed.group(2))

with open('providers.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
