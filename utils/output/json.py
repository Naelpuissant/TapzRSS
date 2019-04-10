# -*- coding: utf-8 -*-
import json

class Json():

    def __init__(self, output_file):
        self.output_file = output_file

    def store(self, data):
        with open(self.output_file, 'w', encoding='UTF8') as f:
            f.write(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))