#!/usr/bin/python

import argparse
import os
import sys


REASON_PHRASES = {
    400: "Bad Request",
    403: "Forbidden",
    451: "Unavailable",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
}


def status_from_file(f):
    filepath = f.name
    filename = os.path.basename(filepath)
    status_code_str = filename.split(".", 1)[0]
    return int(status_code_str)


def compress_markup(content):
    return content.replace("\n", "")


def write_http_response(stream, status_code, content):
    reason_phrase = REASON_PHRASES[status_code]
    stream.write("HTTP/1.1 %d %s\r\n" % (status_code, reason_phrase))
    stream.write("Content-Type: text/html; charset=UTF-8\r\n")
    stream.write("Content-Length: %d\r\n" % len(content))
    stream.write("\r\n")
    stream.write(content)


def main():
    parser = argparse.ArgumentParser(description="generate an http response")
    parser.add_argument("--no-compress",
                        action="store_false",
                        dest="compress",
                        default=True)
    parser.add_argument("file", type=open)
    args = parser.parse_args()

    status_code = status_from_file(args.file)
    content = args.file.read()
    if args.compress:
        content = compress_markup(content)
    write_http_response(sys.stdout, status_code, content)


if __name__ == "__main__":
    sys.exit(main())
