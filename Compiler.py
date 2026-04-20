import os
total=""
path1="Theory D&D"
path2="Wendigoon D&D/HFY Power Armor"
path3="Theory D&D/Things/Magic"
path4="D&D Knowledge"
data={}
for root,dirs,files in os.walk(path1):
    for file in files:
        if file.endswith(".md"):
            path=os.path.join(root,file)
            with open(path,"r",encoding="UTF-8") as fs:
                if file in data:
                    data[str(os.path.join(root,file))]=f"\nFile: {path}\n\n{fs.read()}\n"
                else:
                    data[file]=f"\nFile: {path}\n\n{fs.read()}\n"
                #total+=f"\nFile: {path}\n\n{fs.read()}\n"
relevant_tags=[
    #"#Magic",
    #"#God",
    #"#Cryptid",
    #"#Theory",
    #" "
    "Masquerade",
    "The Family Buisness"
]
c=0
for key in sorted(list(data.keys())):
    for tag in relevant_tags:
        if tag in data[key]:# or 1:
            total+=data[key]
            print(key)
            c+=1
            break
print(c)
with open("total.md","w",encoding="UTF-8") as f:
    f.write(total)