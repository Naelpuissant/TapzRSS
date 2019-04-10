# -*- coding: utf-8 -*-
import json

class Stdout():

    def store(self, data):
        print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))