import json


def load(filename, nodename=None):
    if nodename is None: nodename = filename
    filename = 'monopsony/data/{}.json'.format(filename)
    with open(filename) as f:
        data = json.load(f)
    return data[nodename]
