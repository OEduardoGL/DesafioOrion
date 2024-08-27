import csv
import json
import os


source_file = "./samples/"

target_folder = "./converted/"

data = {}

with open(source_file, 'r', encoding= "utf-8") as csvfile:
    csvRead = csv.DictReader(csvfile)
    k = 0

    for rows in csvRead:
        data[k] = rows
        k = k+1

    file_ = os.path.basename(source_file) + "_converted.json"

with open(target_folder+file_, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))