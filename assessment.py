data_txt = "data.txt"
infile = open(data_txt, "r")
line1=infile.readline(0)
print(line1)

for line in infile:
    if "aman" in line:
        andy = line.split(',')
        print(andy)
    elif "betho" in line:
        beth = line.split(',')
        print(beth)
    elif "camcam" in line:
        cam = line.split(',')
        print(cam)



andy = {
    "username" : andy[0],
    "password" : andy[1],
    "name" : andy[2],
    "balance" : andy[3]
}

beth = {
    "username" : beth[0],
    "password" : beth[1],
    "name" : beth[2],
    "balance" : beth[3]
}

cam = {
    "username" : cam[0],
    "password" : cam[1],
    "name" : cam[2],
    "balance" : cam[3]
}



infile.close()