import json
import xmltodict
import dicttoxml
import yaml
import sys
import argparse
from avro.schema import make_avsc_object
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

def json_to_dict(js: json):
    obj = json.loads(json.dumps(js))
    return obj

def dict_to_json(d):
    s = json.dumps(d)
    return json.loads(s)

def dict_to_xml(d):
    xml = dicttoxml.dicttoxml(d)
    return xml.decode('utf-8')

def xml_to_dict(x):
    return xmltodict.parse(x)

def dict_to_yaml(d):
    return yaml.dump(d)

def dict_to_avro(d):
    schema_dict = {
        'namespace': 'example.avro',
        'name': 'example',
        'type': 'record',
        'fields': []
    }
    for key in d.keys():
        field = {
            'name': key,
            'type': ['null', type(d[key]).__name__]
        }
        schema_dict['fields'].append(field)
    schema = make_avsc_object(schema_dict)
    writer = DataFileWriter(open('example.avro', 'wb'), DatumWriter(), schema)
    writer.append(d)
    writer.close()
    return sys.getsizeof(open('example.avro', 'rb').read())

def read_json(filename):
    with open(filename) as f:
        js = json.load(f)
    return js

class Solver:
    def __init__(self, data):
        self.d = data

    def get_dict_memory(self):
        return sys.getsizeof(self.d)

    def get_xml_memory(self):
        return sys.getsizeof(dict_to_xml(self.d))

    def get_json_memory(self):
        return sys.getsizeof(dict_to_json(self.d))

    def get_yaml_memory(self):
        return sys.getsizeof(dict_to_yaml(self.d))

    def get_avro_memory(self):
        return dict_to_avro(self.d)

argparser = argparse.ArgumentParser()
argparser.add_argument(
    '--file',
    required=True,
    help='path to json file for testing'
)
argparser.add_argument(
    '--test_type',
    required=True,
    help='type which you want to test ("native", "xml", "json", "avro", "yaml")'
)
args = argparser.parse_args()
filename = args.file
test_type = args.test_type
s = Solver(json_to_dict(read_json(filename)))
if test_type == "native":
    print(s.get_dict_memory())
elif test_type == "json":
    print(s.get_json_memory())
elif test_type == "xml":
    print(s.get_xml_memory())
elif test_type == "yaml":
    print(s.get_yaml_memory())
elif test_type == "avro":
    print(s.get_avro_memory())
else:
    print("Sorry, this test_type is not supported now")
