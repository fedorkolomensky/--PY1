import json

INPUT_FILE = "output.csv"

def csv_to_list_dict(filename) -> list[dict]:
    with open(filename) as f:
        list = []
        for line in f:
            list.append(line)
    headers = [element.split(',') for element in list]
    dict_full = []
    index = 0
    for num_list in range(1, len(headers)):
        dict = {}
        for i in headers[0]:
            dict[i.rstrip()] = headers[num_list][index].rstrip()
            index+=1
        dict_full.append(dict)
        index = 0
    return dict_full

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
