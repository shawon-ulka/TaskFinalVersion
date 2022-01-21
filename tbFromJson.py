import json

with open("portDataNew","r") as f:
    allInfoDict=json.load(f)
f.close()
def sizeString(size):
    if size==1:
        return ""
    sizeString=f"[{size-1}:0]"
    return sizeString
with open("testBench.sv","w") as f:
    f.writelines("//TestBench Generation\n\n")
    f.writelines(f"module tb_{allInfoDict['module name']};//TestBench code start\n\n")
    allPortInfo=allInfoDict["allPortInfo"]
    index=1

    for key,value in allPortInfo.items():
        portInfo=allPortInfo[key]

        if portInfo["type"]=="wire" and portInfo["direction"]=="input":
            size=sizeString(portInfo['size'])
            outputLine=f"\treg {size} {key};\n"
        elif portInfo["type"]=="reg" and portInfo["direction"]=="output":
            size=sizeString(portInfo['size'])
            outputLine=f"\twire {size} {key};\n"
        elif portInfo["type"]=="wire" and portInfo["direction"]=="inout":
            size=sizeString(portInfo['size'])
            outputLine=f"\treg {size} {key};\n"
        if index==len(allPortInfo):
            outputLine=outputLine.replace(";","")
        f.writelines(outputLine)
        index+=1
    f.writelines("\nendmodule//TestBench code end")

f.close()