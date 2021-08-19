#!/usr/bin/python3
import cgi

print("Content-type:text/html")
print("Access-Control-Allow-Origin: *")
print()

import json
import subprocess

data = cgi.FieldStorage()
#verb = data.getvalue("verb")

deploycmd="curl -s --cacert ca.crt --cert adminfinalcert.crt  --key adminfinal.key https://172.31.33.38:6443/apis/apps/v1/namespaces/default/deployments"
podcmd="curl -s --cacert ca.crt --cert adminfinalcert.crt  --key adminfinal.key https://172.31.33.38:6443/api/v1/namespaces/default/pods"
svccmd="curl -s --cacert ca.crt --cert adminfinalcert.crt  --key adminfinal.key https://172.31.33.38:6443/api/v1/namespaces/default/services"
rscmd = "curl -s --cacert ca.crt --cert adminfinalcert.crt  --key adminfinal.key https://172.31.33.38:6443/apis/apps/v1/namespaces/default/replicasets/"
pvccmd = "curl -s --cacert ca.crt --cert adminfinalcert.crt  --key adminfinal.key https://172.31.33.38:6443/api/v1/persistentvolumeclaims"
deployop = subprocess.getoutput(deploycmd)
podop = subprocess.getoutput(podcmd)
svcop = subprocess.getoutput(svccmd)
rsop = subprocess.getoutput(rscmd)
pvcop = subprocess.getoutput(pvccmd)

deploydata = json.loads(deployop)
poddata = json.loads(podop)
svcdata = json.loads(svcop)
rsdata = json.loads(rsop)
pvcdata = json.loads(pvcop)

op={
    "pod" : len(poddata['items']),
    "deploy" : len(deploydata['items']) ,
    "svc" : len(svcdata['items']) ,
    "rs" : len(rsdata['items']) ,
    "pvc" : len(pvcdata['items']) }

jsonop = json.dumps(op)
print(jsonop)
#print(len(poddata['items']))
