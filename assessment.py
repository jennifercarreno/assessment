data_txt = "data.txt"
infile = open(data_txt, "r")

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

username_input = input('Enter Username: ')
password_input = input('Enter Password: ')

def display(username):
    # print(username)
    if username == andy["username"]:
        load_andy_data(password_input)
    if username == beth["username"]:
        load_beth_data(password_input)
    if username == cam["username"]:
        load_cam_data(password_input)

def load_andy_data(password):
    if password == andy["password"]:
        print("Name:", andy["name"])
        print("Balance:", andy["balance"])
    else: 
        print("Username and Password not found")

def load_beth_data(password):
    if password == beth["password"]:
        print("Name:", beth["name"])
        print("Balance:", beth["balance"])
    else: 
        print("Username and Password not found")

def load_cam_data(password):
    if password == cam["password"]:
        print("Name:", cam["name"])
        print("Balance:", cam["balance"])
    else: 
        print("Username and Password not found")

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

display(username_input)

infile.close()