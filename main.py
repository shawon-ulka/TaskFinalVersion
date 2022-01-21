from sortData import sortData
import json
import re
with open("task.sv") as f:
    lines=f.readlines()
f.close()

impData=[]
dictOfJson={}
for eachLine in lines:
    if eachLine.startswith("module"):
        module_name=eachLine.split()[1]
        only_name=module_name.split("(")[0]
        dictOfJson["module name"]=only_name
        brac_splited=eachLine.split("(")[1]
        splited=re.split('[,;]+', brac_splited)
        for elem in splited:
            elem=elem.strip()
            elem=elem.replace(")","")
            if elem=="" or elem=="\n":
                continue
            impData.append(elem)
        continue
    if eachLine.startswith("`timescale"):
        timesacle=eachLine.split()[1]
        dictOfJson["timescale"]=timesacle
    if eachLine.startswith("endmodule"):
        continue
    eachLine=eachLine.strip()
    if eachLine=="" or eachLine=="\n":
        continue
    splitted=re.split('[,;]+', eachLine)
    for elem in splitted:
        elem=elem.strip()
        elem=elem.replace(")","")
        if elem=="" or elem=="\n":
            continue
        impData.append(elem)

allPortInfo=sortData(impData)
dictOfJson["allPortInfo"]=allPortInfo
portData=json.dumps(dictOfJson,indent=4)
with open("jsonData","w") as f:
    f.write(portData)
f.close()