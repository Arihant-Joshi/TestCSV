#!/usr/local/opt/python/libexec/bin/python

import json
import os.path
import sys

args = sys.argv()

jsonPath = "./Data.json"
data = dict([])
if(os.path.isfile(jsonPath)):
	with open(jsonPath, "r") as f:
		data = json.loads(f.read())

if(args[1] == "workspace"):
	resource_group = args[2]
	region = args[3]
	environment_name = args[4]
	db_private_subnet = args[5]
	db_public_subnet = args[6]

	if(resource_group not in data):
		data[resource_group] = dict([])

	data[resource_group]["region"] = region
	data[resource_group]["WS Name"] = environment_name
	data[resource_group]["db_private_subnet"] = environment_name
	data[resource_group]["db_public_subnet"] = environment_name
else:
	resource_group = args[2]
	region = args[3]
	environment_name = args[4]
	vm_machine_type = args[5]
	os_version = args[6]

	if(resource_group not in data):
		data[resource_group] = dict([])

	data[resource_group]["region"] = region
	data[resource_group]["VM Name"] = environment_name
	data[resource_group]["VM Type"] = vm_machine_type
	data[resource_group]["OS Version"] = os_version


with open(jsonPath,"w") as f:
	f.write(json.dumps(data,indent=4))