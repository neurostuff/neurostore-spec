"""Dereference allOf statements so that base objects are documented"""

import json
import os
import re
from copy import deepcopy

nimads_dir = os.path.dirname(os.path.dirname(__file__))
nimads_file = nimads_dir + "/nimads.json"
with open(nimads_file, "r+") as nf:
    nidata = json.load(nf)

dereferenced_nidata = deepcopy(nidata)
objects = [
    "studyset",
    "study",
    "annotation",
    "noteCollection",
    "analysis",
    "image",
    "point",
    "condition",
]

for obj in objects:
    schema = nidata['components']['schemas'][obj]
    refs = [r['$ref'] for r in schema['allOf']]
    props = {}
    for ref in refs:
        ref_schema_key = ref.split("/")[-1]
        ref_schema = nidata['components']['schemas'][ref_schema_key]
        props.update(ref_schema['properties'])
    deref_schema = dereferenced_nidata['components']['schemas'][obj]
    deref_schema.pop("allOf")
    deref_schema['type'] = 'object'
    deref_schema['properties'] = props

for name, schema in nidata['components']['schemas'].items():
    if "Relationships" in name or "Base" in name:
        del dereferenced_nidata['components']['schemas'][name]
    

with open(nimads_dir + "/simple-nimads.json", "w+") as sn:
    json.dump(dereferenced_nidata, sn)

# changing the references to be in line with their new names
replaced_ref_nidata = json.loads(re.sub(r"#/components/schemas/([A-Za-z0-9]+)", r"\1.json", json.dumps(dereferenced_nidata)))  
## Splitting the files up (handle references by treating the entire object as a string)    
for name, schema in replaced_ref_nidata['components']['schemas'].items():
    with open(nimads_dir + f"/nimads/{name}.json", "w+") as sf:
        json.dump(schema, sf)
    

    


    
        
