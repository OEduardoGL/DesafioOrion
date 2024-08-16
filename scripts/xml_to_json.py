import os
from bs4 import BeautifulSoup
import json 


source_file = "./samples/xml_sample.xml"

target_folder = "./converted/"


with open(source_file, 'r', encoding="utf-8") as xml_file:
    xml = BeautifulSoup(xml_file, features='xml')
    
    data = {}

    for tag in xml.find_all():
        if not tag.name in data:
            data[tag.name] = []
        lista = {k: v for k, v in tag.attrs.items()}
        data[tag.name].append(lista)

file_ = os.path.basename(source_file) + "_converted.json"

with open(target_folder+file_, 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4)