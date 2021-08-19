import deployments
import services


print("\t\t\t\t\t\t\Welcome to your Kubernetes Cluster")
print("-----------MENU--------------")

print("1.Depoyments\n2.Service\n3.PVC\n4.Replication Controller\n5.Replica Set")
ch = int(input("Enter your choice : "))
if ch == 1 :
    deploy_ch = input("What do you want to do in deployments...get all deployments,describe a deployment or create a new deployment?  : ") 
    if deploy_ch in ("get","GET") : 
        data = deployments.get_all()
        if not data : 
            print("Empty list")
        else : 
            print("NAME","\t","READY","\t","UP-TO-DATE","\t","AVAILABLE")
            for val in data :
                 
                print(val['metadata']['name'],"\t",val['status']['replicas'],"/",val['status']['readyReplicas'],"\t",val['status']['updatedReplicas'],"\t",val['status']['availableReplicas'])
        
    elif deploy_ch in ("create","Create") :   
        data = deployments.create()
    elif deploy_ch in ("delete","Delete") :   
        data = deployments.delete()
        if data['status'] == "Success" : 
            print(data['details']['name']," Deleted Successfully")
        else : 
            print(data['details']['name'],data['reason'])
    if deploy_ch in ("describe","Describe") : 
        deployname=input("Enter the name of the deployment : ")
        data = deployments.describe(deployname)
        if not data : 
            print("Empty list")
        else : 
            print("Name :",data['metadata']['name'])
            print("Namespace :",data['metadata']['namespace'])
            print("uid :",data['metadata']['uid'])
            print("Created at :",data['metadata']['creationTimestamp'])
            print("Labels :",data['spec']['template']['metadata']['labels'])
            print("Container Name :",data['spec']['template']['spec']['containers'][0]['name'])
            print("Container Image :",data['spec']['template']['spec']['containers'][0]['image'])
            print("Desired Replicas :",data['status']['replicas'])
            print("Ready Replicas :",data['status']['readyReplicas'])
            print("Up-to-date Replicas :",data['status']['updatedReplicas'])
            print("Available Replicas :",data['status']['availableReplicas'])
            print("Strategy :",data['spec']['strategy']['type'])


if ch == 2 :
    service_ch = input("What do you want to do in services...get all deployments,describe a deployment or create a new deployment?  : ") 
    if service_ch in ("get","GET") : 
        data = services.get_all()
        if not data : 
            print("Empty list")
        else : 
            print("NAME","\t","TYPE","\t","CLUSTERIP","\t","PORTS","\t","PROTOCOL")
            for val in data :
                 
                print(val['metadata']['name'],"\t",val['spec']['type'],"\t",val['spec']['clusterIP'],"\t",val['spec']['ports'][0]['port'],":" if val['spec']['type'] == "NodePort"  else  "",val['spec']['ports'][0]['nodePort'] if val['spec']['type'] == "NodePort"  else  " ","\t",val['spec']['ports'][0]['protocol'])
        
