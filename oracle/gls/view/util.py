import json
import os
cwd = os.path.dirname(os.path.realpath(__file__))


def get_data_with_id(id):
	with open(cwd + "/guide.json") as json_file:  
	  	data = json.load(json_file)
	  	for step in data["steps"]:
		    if step["id"] == str(id):
	        	return step
