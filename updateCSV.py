import json
import os.path

jsonPath = "./Data.json"
data = dict([])
if(os.path.isfile(jsonPath)):
	with f as open(jsonPath, "r"):
		data = json.loads(f.read())

data["key1"] = "val1"

with f as open(jsonPath,"w"):
	f.write(json.dumps(data,indent=4))