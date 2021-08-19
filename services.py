#!/usr/bin/python3
import cgi

print("Content-type:text/html")
print("Access-Control-Allow-Origin: *")
print()

import json
import helpers
import subprocess
import deployments

data = cgi.FieldStorage()
verb = data.getvalue("verb")
deployname = data.getvalue("name")
imgname = data.getvalue("image")
conname = data.getvalue("container")
replicas = data.getvalue("replica")



if verb == "get":
    try:
       # print("Enter")
        data = helpers.Service.get_all()
        jsonop = json.dumps(data)
        print(jsonop)
    except Exception as e:
        print(e)
elif verb == "create":
    data = deployments.create(deployname,replicas,conname,imgname)
   # jsonop = json.dumps(data)
    print(data)
   # print(imgname)
    #print(verb)
