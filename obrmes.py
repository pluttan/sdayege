import json


def conv_to_dict(string):
    string=str(string)
    string = string\
        .replace("'", '"')\
        .replace("None", "null")\
        .replace("False", "false")\
        .replace("True", "true")\
        .replace("<", '"')\
        .replace(">", '"')
    file = open('json.tmp/new.json', "w")
    file.write(string)
    file.close()
    with open('json.tmp/new.json') as json_file:
        try: return json.load(json_file)
        except:return "err"
