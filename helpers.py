import subprocess
import json
class Deployments:
    def get_all():
        cmd="curl -s --cacert ca.crt --cert adminfinalcert.crt  --key adminfinal.key https://172.31.33.38:6443/apis/apps/v1/namespaces/default/deployments"
        op = subprocess.getoutput(cmd)
        data = json.loads(op)
        return data['items']
    def create(deployname,replicas,conname,imgname,labels=None) :
        if labels is None :
            labels = { 'deploy' : deployname }
        cmd="""curl --cacert ca.crt --cert adminfinalcert.crt --key adminfinal.key -X POST -H 'Content-Type: application/yaml'  --data '
            apiVersion: apps/v1
            kind: Deployment
            metadata:
              name: {0}
            spec:
              replicas: {1}
              selector:
                matchLabels:
                  app : {0} 
              template:
                metadata:
                  labels:
                   app : {0}
                spec:
                  containers:
                  - name: {2}
                    image: {2}
            ' https://172.31.33.38:6443/apis/apps/v1/namespaces/default/deployments""".format(deployname,replicas,conname,imgname)

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
class Pods: 
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
        data = json.loads(op)
        print(data)

    def describe_kube(name): 
        cmd= "sudo kubectl describe pod {}".format(name)
        op = subprocess.getoutput(cmd)
        #data = json.loads(op)
        return op
    def describe(name): 
        cmd="sudo kubectl describe pod {}".format(name)
        op = subprocess.getoutput(cmd)
       # data = json.loads(op)
        return op
    def delete(name): 
        cmd="sudo kubectl delete pod {}".format(name)
        op = subprocess.getoutput(cmd)
       # data = json.loads(op)
        return op
        
class Service: 
    def get_all():
        cmd="curl -s --cacert ca.crt --cert adminfinalcert.crt  --key adminfinal.key https://172.31.33.38:6443/api/v1/namespaces/default/services"
        op = subprocess.getoutput(cmd)
        data = json.loads(op)
        return data['items']

