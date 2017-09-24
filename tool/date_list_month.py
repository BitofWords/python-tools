#!/usr/bin/env python3

import argparse
import calendar
import datetime

parser = argparse.ArgumentParser(
    description='Display date list of the month.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('year', help='year', type=int)
parser.add_argument('month', help='month', type=int)
parser.add_argument('prefix', help='prefix for output', nargs='?', default='')
parser.add_argument('suffix', help='suffix for output', nargs='?', default='')

args = parser.parse_args()

y = args.year
m = args.month
p = args.prefix
s = args.suffix

fmt = '%Y-%m-%d'

r = calendar.monthrange(y, m)

for d in range(r[1]):
    date = datetime.date(y, m, d + 1)
    print(p + date.strftime(fmt) + s)
