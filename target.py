from collections import defaultdict
import json


class Parser(defaultdict):
    def __init__(self, d=None):
        super(Parser, self).__init__(Parser)
        if d:
            for k, v in d.items():
                self[k] = v

    def __setitem__(self, key, value):
        if "." in key:
            first_key, other_key = key.split(".", 1)
            Parser.__setitem__(self[first_key], other_key, value)
        else:
            super(Parser, self).__setitem__(key, value)
