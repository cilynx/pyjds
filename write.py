#!/usr/bin/env python

import pyjds
import sys

jds = pyjds.JDS()

print(jds.write(sys.argv[1], int(sys.argv[2]), debug=True))
print(jds.read(sys.argv[1], 1, debug=True))
