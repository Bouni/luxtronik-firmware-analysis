#!/usr/bin/env python3
import requests
import struct
import sys


def decode_string(s):
    s_decoded = s.decode("utf16")
    assert s_decoded.find("\0") == len(s_decoded) - 1
    s_decoded = s_decoded[: len(s_decoded) - 1]
    return s_decoded


def read_language_file(filename):
    with open(filename, "br") as f:
        c = f.read()
    return parse_language_data(c)


def read_language_file_remote(url):
    response = requests.get(url)
    c = response.content
    return parse_language_data(c)


def get_languages():
    # Available languages
    languages = {
        "de": "Deutsch",
        "en": "English",
        "fr": "Français",
        "nor": "Norsk",
        "cz": "Čeština",
        "it": "Italiano",
        "ned": "Nederlands",
        "sve": "Svenska",
        "pol": "Polski",
        "mag": "Magyarul",
        "dan": "Dansk",
        "p": "Português",
        "lt": "Lietuviskai",
        "ee": "Eesti",
        "slo": "Slovenščina",
        "sk": "Slovenčina",
        "lv": "Latviešu valoda",
        "suo": "Suomi",
        "tr": "Türkçe",
        "es": "Español",
        "ro": "Română",
    }
    return languages


def parse_language_data(data):
    # Read header
    field1 = data[0:4]
    assert field1 == b"\x12\x5a\x45\x89"

    # Not sure what these are
    # field2 = data[4:8]
    # field3 = data[8:12]

    # Number of strings in this file
    field4 = data[12:16]
    num_fields = struct.unpack("i", field4)[0]
    print("There are %d strings in this file." % num_fields)

    start_idx = list(struct.unpack("i" * num_fields, data[16 : 16 + 4 * num_fields]))

    payload = data[16 + 4 * num_fields :]

    # Add the end index
    start_idx.append(len(payload) // 2)

    # Extract strings
    strings = list()

    for i in range(num_fields):
        string = decode_string(payload[2 * start_idx[i] : 2 * start_idx[i + 1]])
        strings.append(string)

    return strings


if __name__ == "__main__":
    if len(sys.argv) < 2 or (len(sys.argv) == 2 and sys.argv[1] == "-r"):
        print("Usage:")
        print("%s [language_file]" % sys.argv[0])
        print("or")
        print("%s -r http://url_to_heat_pump/[language_file]\n" % sys.argv[0])
        print("Typically available languages:")
        langs = get_languages()
        for i in langs.keys():
            print("lang_%-3s .. %s" % (i, langs[i]))
        sys.exit(0)

    if sys.argv[1] != "-r":
        filename = sys.argv[1]
        strings = read_language_file(sys.argv[1])
    else:
        url = sys.argv[2]
        strings = read_language_file_remote(sys.argv[2])

    for i, s in enumerate(strings):
        print("%4d: %s" % (i, s))
