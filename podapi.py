#!/usr/bin/python3
import cgi

print("Content-type:text/html")
print("Access-Control-Allow-Origin: *")
print()

import json
import subprocess
import helpers
import pods

data = cgi.FieldStorage()
verb = data.getvalue("verb")
podname = data.getvalue("podname")
imgname = data.getvalue("image")
conname = data.getvalue("container")
#replicas = data.getvalue("replica")



if verb == "get":
   # print("Enter")
    try:
        data = helpers.Pods.get_all()
        jsonop = json.dumps(data)
        print(jsonop)
    except Exception as e: 
        print(e)
elif verb == "create":
    data = helpers.Pods.create(podname,conname,imgname)
   # jsonop = json.dumps(data)
    print(data)
   # print(imgname)
    #print(verb)
elif verb == "describe":
    try:
        data = helpers.Pods.describe(podname)
       # jsonop = json.dumps(data)
       # jsonop = json.dumps(data,indent=4, sort_keys=True)
        print(data)
       # print("Exit")
    except Exception as e: 
        print(e)
        print("Here")
elif verb == "delete":
    try:
        data = helpers.Pods.delete(podname)
       # jsonop = json.dumps(data)
       # jsonop = json.dumps(data,indent=4, sort_keys=True)
        if "deleted" in data:
            op = { "status" : "OK" } 
            print(json.dumps(op))
       # print("Exit")
    except Exception as e: 
        print(e)
        print("Here")
