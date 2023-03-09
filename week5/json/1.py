import json


with open('A:\proga\sem2\week4\json\sampledata.json') as a:
   data = json.load(a)


print("Interface status")
print("=" * 80)
print("DN", " " * 40, "Description ", "speed", " " * 10, "MTU")
print("-" * 41, "-" * 12, "-" * 13, "\t", "-" * 4)
for i in data["imdata"]:
    string=str(i["l1PhysIf"]["attributes"]["dn"])

    if(len(string)==42):
        print("{}              {}          {}".format(i["l1PhysIf"]["attributes"]["dn"],i["l1PhysIf"]["attributes"]["speed"], i["l1PhysIf"]["attributes"]["mtu"]))
    else:
        print("{}               {}          {}".format(i["l1PhysIf"]["attributes"]["dn"],i["l1PhysIf"]["attributes"]["speed"], i["l1PhysIf"]["attributes"]["mtu"]))

