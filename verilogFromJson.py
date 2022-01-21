import json

with open("portDataNew","r") as f:
    jsonDict=json.load(f)
f.close()
def sizeFormat(size):
    if size==1:
        return ""
    strSize=f"[{size-1}:0]"
    return strSize
with open("outputVerilog.sv","w") as outputFile:
    outputFile.writelines("// Code Generated from Excel\n")
    outputFile.writelines(f"`timescale {jsonDict['timescale']}\n\n")
    outputFile.writelines(f"module {jsonDict['module name']} (\n")
    index=1
    for key, value in jsonDict["allPortInfo"].items():
        portName=key
        portDirection=value["direction"]
        size=sizeFormat(value["size"])
        type=value["type"]
        outputLine=f"\t{portDirection}\t{type}\t{size}\t{portName},\n"
        if index==len(jsonDict["allPortInfo"]):
            outputLine=outputLine.replace(",","")
        outputFile.writelines(outputLine)
        index+=1
    outputFile.writelines(");\n\n")
    outputFile.writelines("endmodule")