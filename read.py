#!/usr/bin/env python

import pyjds
import sys

jds = pyjds.JDS()

count = 0
if len(sys.argv) > 2:
    count += int(sys.argv[2])

print(jds.read(sys.argv[1], count, debug=True))
