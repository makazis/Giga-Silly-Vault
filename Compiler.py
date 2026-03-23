import os
total=""
path1="Theory D&D"
path2="Wendigoon D&D/HFY Power Armor"
data={}
for root,dirs,files in os.walk(path1):
    for file in files:
        if file.endswith(".md"):
            path=os.path.join(root,file)
            print(path)
            with open(path,"r",encoding="UTF-8") as fs:
                data[file]=f"\nFile: {path}\n\n{fs.read()}\n"
                #total+=f"\nFile: {path}\n\n{fs.read()}\n"
for key in sorted(list(data.keys())):
    total+=data[key]
    print(key)
with open("total.txt","w",encoding="UTF-8") as f:
    f.write(total)