import json
from haralyzer import HarParser

filelist = []
_txt = open('PATH', 'w')

with open('sample.har', 'r') as f:
    har_parser = HarParser(json.loads(f.read()))


def WriteToFile(textToWrite):
    line = '{}\n'.format(textToWrite)
    _txt.write(line)


for page in har_parser.pages:
    for entry in page.entries:
        if entry.response.status == 200:
            _dataEntry = entry['response']['content'].get('text', '')
            _splitData = _dataEntry.split(',')
            for i in _splitData:
                # Replace "Data To Write" with the information we are looking for
                if i.__contains__('Data To Write'):
                    WriteToFile(i)
