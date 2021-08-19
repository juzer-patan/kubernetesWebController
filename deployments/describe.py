
import cgi
import subprocess
import json

data = cgi.FieldStorage()
verb = data.getvalue("verb")
deployname = data.getvalue("deployname")

cmd="curl -s --cacert ca.crt --cert adminfinalcert.crt  --key adminfinal.key https://172.31.33.38:6443/apis/apps/v1/namespaces/default/deployments?fieldSelector=metadata.name={}".format(deployname)
op = subprocess.getoutput(cmd)
data = json.loads(op)
print(data['items'][0])

