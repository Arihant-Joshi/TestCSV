#!/usr/local/opt/python/libexec/bin/python

import json
import os.path

jsonPath = "./Data.json"
data = dict([])
if(os.path.isfile(jsonPath)):
	with open(jsonPath, "r") as f:
		data = json.loads(f.read())

data["key2"] = "val2"

with open(jsonPath,"w") as f:
	f.write(json.dumps(data,indent=4))