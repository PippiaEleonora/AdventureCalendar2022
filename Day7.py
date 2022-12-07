class Grafo():
    def __init__(self, grafo: dict, files: dict, listFiles: list) -> None:
        self.grafo = grafo
        self.files = files
        self.listFiles = listFiles
    
    def value(self, folder:str):
        
        if folder in self.listFiles:
            return self.files[folder]
        if not self.grafo[folder]["Value"] == None:
            return self.grafo[folder]["Value"]
        else:
            val = 0
            for item in self.grafo[folder]["List"]:
                val += self.value(item)
            self.grafo[folder]["Value"] = val
            return val


if __name__ == "__main__":
    with open('input7.txt') as f:
        arrayRaw = f.readlines()
        
    path = []
    created_folders = []
    created_files = []
    adjacentList = {}
    Val_files = {}
    for line in arrayRaw:
        line = line.replace("\n", "")
        if "$ cd .." in line:
             path.pop()
             path.pop()
        elif "$ ls" in line:
            pass
        elif "$ cd" in line:
            folder = line.replace("$ cd ", "")
            path.append(folder)
            path.append("/")
            if not "".join(path) in created_folders:
                adjacentList.update({"".join(path): {"List": [], "Value": None}})
                created_folders.append("".join(path))
                
        else:
            if "dir" in line:
                dir = line.replace("dir ", "")
                adjacentList["".join(path)]["List"] += ["".join(path)+dir+"/"]
                if not "".join(path)+dir+"/" in created_folders:
                    adjacentList.update({"".join(path)+dir+"/": {"List": [], "Value": None}})
                    created_folders.append("".join(path)+dir+"/")
            else:
                file = line.split(" ")
                adjacentList["".join(path)]["List"] += ["".join(path)+"file_"+file[1]]
                if not "".join(path)+"file_"+file[1] in created_files:
                    Val_files.update({"".join(path)+"file_"+file[1]: int(file[0])})
                    created_files.append("".join(path)+"file_"+file[1])
    
    G = Grafo(adjacentList, Val_files, created_files)
    G.value(folder = '//')
    
    ValList = []
    for k in G.grafo.keys():
        ValList += [G.grafo[k]["Value"]]
    
    ValMin = [i for i in ValList if i<=100000 ]
    print(sum(ValMin))
    
    # Second part
    total_memory = G.grafo['//']["Value"]
    empty_space = 70000000 - total_memory
    need_to_empty = 30000000 - empty_space
    
    
    folder = min([i for i in ValList if i>=need_to_empty ])
    print(folder)
