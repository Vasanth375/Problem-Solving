path = "/home/./..//ab"

# #path = "/../"

dirOrFiles = []
path = path.split("/")
for elem in path:
    # if elem is ".." then move back to previous path
    if dirOrFiles and elem == "..":
        dirOrFiles.pop()

    # if elem is directory or file name then add it to the list
    elif elem not in [".", "", ".."]:
        dirOrFiles.append(elem)
        
print("/" + "/".join(dirOrFiles))