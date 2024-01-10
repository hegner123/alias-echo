if __name__ == "__main__":
    zshrcFile = open("/Users/home/.zshrc", "r")
    splitZshrc = zshrcFile.read().splitlines()
    for line in splitZshrc:
        if "alias" in line:
            if "#" not in line:
                replacedLineAlias = line.replace("alias", "")
                replacedLineEquals = replacedLineAlias.replace("=", "  ")
                print(replacedLineEquals)
    zshrcFile.close()
    

    pass
