print("Welcome")
import helpers
import json
data = helpers.Pods.describe("mypodjuz")
jsonop = json.dumps(data)
print(jsonop)

