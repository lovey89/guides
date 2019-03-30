#!/usr/bin/env python3

import sys
import csv
import json

file_name = sys.argv[1]
json_file = open(file_name)

json_string = json_file.read()

j = json.loads(json_string)

headers = set()

for element in j:
    keys = element.keys()
    headers.update(keys)

header_list = list(headers)

f = csv.writer(open('output.csv', 'w+'))

f.writerow(['sep=,'])
f.writerow(list(header_list))

for element in j:
    data = [element.get(header, '') for header in header_list]
    f.writerow(data)
