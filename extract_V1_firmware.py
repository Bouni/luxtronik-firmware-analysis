#!/usr/bin/env python3

import gzip
import io
import os
import sys


def extract(filename, dirname):
    print("Extract file", filename)
    print("to directory", dirname)

    print("Press enter to continue or CTRL-C to abort")
    input()

    os.makedirs(dirname, exist_ok=True)

    with open(filename, "rb") as fd:
        content = fd.read()

    while len(content) > 0:
        # Read header
        header = content[0:0x100]

        # Dissect
        lengths = [116, 12, 16, 12, 24, 60, 16]
        headers = []

        for i in lengths:
            headers.append(header[0:i])
            header = header[i:]

        zero = b"\00"

        header = headers[0].rstrip(zero)
        filelength = int(headers[1].rstrip(zero), 16)
        md5sum = headers[2]
        permissions = int(headers[3].rstrip(zero), 16)
        timestamp = int(headers[4].rstrip(zero), 16)
        filename = headers[5].rstrip(zero)
        magic_string = headers[6].rstrip(zero)

        assert magic_string == b"wpreg0120071958"

        print("\nname 1: ", header.decode("utf8"))
        print("name 2: ", filename.decode("utf8"))
        print("timestamp: ", timestamp)
        print("permissions: ", bin(permissions))

        with open(dirname + header.decode("utf8"), "wb") as fd:
            fd.write(content[0x100 : 0x100 + filelength])

        # Now, one could set the time stamp and the permissions.

        content = content[filelength + 0x100 :]

    os.chdir(dirname)

    print('\nExtracting "appl.archive" to %sarchive/' % dirname)

    dirname = b"archive/"

    os.makedirs(dirname, exist_ok=True)

    with gzip.open("appl.archive") as fd:
        content = fd.read()

    idx = 0

    content = content[idx:]

    while len(content) > 0:
        length = int.from_bytes(content[0:3], byteorder="big")
        permissions = int.from_bytes(content[3:6], byteorder="big")
        filenamelength = int(content[6])

        filename = content[7 : 7 + filenamelength].rstrip(zero)

        print()
        print('name: "%s"' % filename.decode("utf8"))
        print("permissions: ", bin(permissions))

        content = content[7 + filenamelength :]

        os.makedirs(dirname + os.path.dirname(filename), exist_ok=True)

        with open(dirname + filename, "wb") as fd:
            fd.write(content[:length])

        # Now, one could set the permissions.

        content = content[length:]


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) > 0:
        filename = args[0]
    else:
        filename = "wpreg.V1.88.3"

    if len(args) > 1:
        dirname = args[1]
        if dirname[-1] != "/":
            dirname += "/"
    else:
        dirname = "firmware/"

    extract(filename, dirname)
