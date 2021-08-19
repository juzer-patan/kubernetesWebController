import os
import cgi
import subprocess
import json

data = cgi.FieldStorage()
verb = data.getvalue("verb")
describedeployname = data.getvalue("describedeploy")
describedeployname = data.getvalue("describedeploy")
describedeployname = data.getvalue("describedeploy")

def describe(deployname): 
    cmd="curl -s --cacert ca.crt --cert adminfinalcert.crt  --key adminfinal.key https://172.31.33.38:6443/apis/apps/v1/namespaces/default/deployments?fieldSelector=metadata.name={}".format(deployname)
    op = subprocess.getoutput(cmd)
    data = json.loads(op)
    return data['items'][0]
def get_all(): 
    cmd="curl -s --cacert ca.crt --cert adminfinalcert.crt  --key adminfinal.key https://172.31.33.38:6443/apis/apps/v1/namespaces/default/deployments"
    op = subprocess.getoutput(cmd)
    data = json.loads(op)
    return data['items']
def create() : 
    deployname=input("Enter the name of the deployment : ")
    replicas=input("Enter the number of replicas : ")
    conname=input("Enter the name of the container : ")
    imgname=input("Enter the name of the image : ")
    volch = input("Do you want to mount any volumes?")

    labels={}
    while(True) :
        ch=int(input("To stop adding labels press 1 : "))
        if(ch==1):
            break
        key = input("Enter the key : ")
        value = input("Enter the value : ")
        labels[key]=value
    if(volch not in ("Yes","yes")):
        cmd="""curl --cacert ca.crt --cert adminfinalcert.crt --key adminfinal.key -X POST -H 'Content-Type: application/yaml'  --data '
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: {0}
        spec:
          replicas: {1}
          selector:
            matchLabels:
              {2}
          template:
            metadata:
              labels:
                {2}
            spec:
              containers:
              - name: {3}
                image: {4}
        ' https://172.31.33.38:6443/apis/apps/v1/namespaces/default/deployments""".format(deployname,replicas,labels,conname,imgname)
        
    op = subprocess.getoutput(cmd)
    print(op)
def delete(): 
    deployname=input("Enter the name of the deployment : ")
    cmd="""curl -s --cacert ca.crt --cert adminfinalcert.crt --key adminfinal.key -X DELETE -H 'Content-Type: application/yaml'  --data '
    gracePeriodSeconds: 0
    orphanDependents: false
    ' https://172.31.33.38:6443/apis/apps/v1/namespaces/default/deployments/{}""".format(deployname)
    op = subprocess.getoutput(cmd)
    data = json.loads(op)
    return data
#name = input("Enter the name of the deployment : ")
#get(name)
