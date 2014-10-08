import json

def test():
    filename = 'properties.json'
    with open(filename) as f:
        data = json.load(f)
    props = data['properties']
    for d in props:
        print(d)  
    print(props['Short Line R.R.'])    

if __name__ == '__main__':
    test()