import sys
from base64 import b64encode, b64decode


if sys.version_info >= (3,0):
    def to_base_64(string):
        return b64encode(str.encode(string)).decode()

    def from_base_64(string):
        return b64decode(str.encode(string)).decode()
else:
    import re
    def to_base_64(string):
        return re.sub('[=$]+', '', b64encode(string).decode())

    def from_base_64(string):
        needs_padding = 4 - len(string) % 4
        if needs_padding:
            string = string + b'=' * needs_padding
        return b64decode(string).decode()
