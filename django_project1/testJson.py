import json

json_string = '{"1":"red","2":"blue","3":"black","4":"brown"}'

parsed_json = json.loads(json_string)

print(parsed_json['1'])
print(parsed_json)