import json

def test_properties():
    filename = 'data/properties.json'
    with open(filename) as f:
        data = json.load(f)
    props = data['properties']
    print(props[14])

if __name__ == '__main__':
    test_properties()