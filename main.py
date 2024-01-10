
import sys

def addAlias(file, alias, command):
    newAlias = "\nalias " + alias + "=" + "\"" + command+ "\""
    file.write(newAlias)
    file.close()

    pass

def removeAlias(file, alias):
    zshrcFile = open(file, "r")
    splitZshrc = zshrcFile.read().splitlines()
    filteredZshrc = [x for x in splitZshrc if x.count("alias " + alias)!=1]
    filteredContent = "\n".join(filteredZshrc)
    
    zshrcFile.close()
    zshrcFile = open(file, "w")
    zshrcFile.write(filteredContent)
    zshrcFile.close()
    pass




if __name__ == "__main__":
    if sys.argv.__len__() == 1:
        zshrcFile = open("/Users/home/.zshrc", "r")
        splitZshrc = zshrcFile.read().splitlines()
        for line in splitZshrc:
            if "alias" in line:
                if "#" not in line:
                    replacedLineAlias = line.replace("alias", "")
                    replacedLineEquals = replacedLineAlias.replace("=", "  ")
                    print(replacedLineEquals)
        zshrcFile.close()
    elif sys.argv.__len__() >= 2:
        if sys.argv[1] == "add":
            zshrcFile = open("/Users/home/.zshrc", "a")
            print("Add")
            addAlias(zshrcFile, sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "remove":
            file = "/Users/home/.zshrc"
            print("Remove")
            removeAlias(file, sys.argv[2])
        else:
            print("Invalid argument: Valid arguments are 'add' and 'remove'")
    sys.exit(1)
    pass

