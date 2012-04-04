#!/usr/bin/python

import sys


REASON_PHRASES = {403: "Forbidden",
                  502: "Bad Gateway",
                  503: "Service Unavailable",
                  504: "Gateway Timeout"}


input_file = sys.argv[1]
html_file = open(input_file, 'r')
html = html_file.read()
html = html.replace("\n", "")

status_code = int(input_file.partition('.')[0])
reason_phrase = REASON_PHRASES[status_code]

sys.stdout.write("HTTP/1.1 %d %s\r\n" % (status_code, reason_phrase))
sys.stdout.write("Content-Type: text/html; charset=UTF-8\r\n")
sys.stdout.write("Content-Length: %d\r\n" % len(html))
sys.stdout.write("\r\n")
sys.stdout.write(html)
sys.stdout.flush()
