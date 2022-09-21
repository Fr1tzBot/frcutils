#!/usr/bin/env python
from sys import argv
argv = argv[1:]
line = "".join(argv)
line = line.replace('      <span class="glyphicon glyphicon-info-sign"></span> aka <em id="team-name">', '')
line = line.replace('</em><br>', '')
line = line.replace("&amp;", "\n")
line = line.replace('/', "\n")
line = line.replace('&', "\n")
line = line.replace(";", "\n")
print(line)
