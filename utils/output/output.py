# -*- coding: utf-8 -*-
from utils.output.json import Json
from utils.output.stdout import Stdout
from utils.output.db import DB

class Output():
    
    def __init__(self, output_type, data, output_file=None, conf_db=None):
        if output_type == 'JSON' : 
            Json(output_file).store(data)
        elif output_type == 'STDOUT' :
            Stdout().store(data)            
        else:
            raise ValueError