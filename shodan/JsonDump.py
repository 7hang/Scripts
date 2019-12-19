import json

filename = 'result.json'

with open(filename) as f:
    while True:
        pop_data = f.readline()
        if pop_data:
            d = json.loads(pop_data)
            ip = d['ip_str']
            port = d['port']
            print('http://' + ("%s")%(ip)+ ":" + ("%s")%(port))
        else:
            break



