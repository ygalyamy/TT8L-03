from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
granted = False
def grant():
    global granted
    granted = True
def login (username,password):
    file = open("user_details","r")
    for i in file:
        a,b = i.split(",")
        b = b.strip
        if(a==username and b==password):
            success=True
            break
    file.close()
    if(success):
        print("Login Sucessfull!!")
        grant()
    else:
        print("wrong username or password")
def register (username,password):
    file = open("user_details.txt","a")
    file.write("\n"+username+","+password)
    file.close()
def access(option):
    global name
    if (option=="login"):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login(username,password)
    else:
        print("Enter your username and password to register")
        name = input("Enter your username: ")
        password = input("Enter your password: ")
        register(username,password)
def begin ():
    global option
    print ("Welcome to PaperTrail!")
    option = input ("Login or Register (login,reg):")
    if(option!="login" and option!="reg"):
        begin()
begin()
access(option)
if(granted):
    print("Welcome to PaperTrail!")
    print("# User Details #")
    print("Username:",name)

def webpage():
    return render_template("webpage.html")

if __name__ == '__main__':
    app.run(debug=True)

