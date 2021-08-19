import subprocess
import json
def get_all():     
    podcmd="curl -s --cacert ca.crt --cert adminfinalcert.crt  --key adminfinal.key https://172.31.33.38:6443/api/v1/namespaces/default/pods"
    op = subprocess.getoutput(podcmd)
    data = json.loads(op)
    return data['items']
    
def create(podname,conname,image): 
    import os
    labels={ "pod" : podname}
    cmd="""curl --cacert ca.crt --cert adminfinalcert.crt --key adminfinal.key -X POST -H 'Content-Type: application/yaml' -H 'Authorization: Bearer <JWT_TOKEN>' --data '
    apiVersion: v1
    kind: Pod
    metadata:
      name: {0}
      labels: 
        {3}
    spec:
      containers:
      - name: {1}
        image: {2}
    ' https://172.31.33.38:6443/api/v1/namespaces/default/pods""".format(podname,conname,imgname,labels)
    output = subprocess.getoutput(cmd)
    print(output)
