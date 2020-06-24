import ast
import os
from datetime import date
from datetime import datetime
global user
user=''
ldict={}
ndict={}
def snup():

    uname = input('Enter a UserName: ')
    pwd= input('Enter a password: ')
    ldict[uname] = pwd
    with open('login.txt', 'r') as file:
        contents=file.read()
        ndict = ast.literal_eval(contents)
    if (uname in ndict.keys()):
        print('UserName Already Exists! Please SignUp with another UserName')
        print("_" * 15 + "\n")
        return 0
    ndict[uname]=pwd
    with open('login.txt','w') as file:
        file.write(str(ndict))
    print('SignUp Successful! Please Login to Continue')
    print("_" * 15 + "\n")
    #with open('login.txt', 'r') as file:
        #print(file.read())
def login():
    uname=input('Enter username: ')
    pwd=input('Enter password: ')
    with open('login.txt', 'r') as file:
        contents=file.read()
        ndict = ast.literal_eval(contents)
    if (uname not in ndict.keys()):
        print('Invalid Username!')
        print("_" * 15 + "\n")
        return 0,0
    elif (ndict[uname] == pwd):
        print('Login Successful!')
        with open('logs.txt', 'a') as f:
            f.write('--LOGIN--'+"\n"+'By: {0}\nDate: {1}\nTime: {2}\n'.format(uname,date.today(),datetime.now().time())+"\n")
        user=uname
        return 1,user
        print("_" * 15 + "\n")
    else:
        print('Wrong Password!Please Try again')
        print("_" * 15 + "\n")
        return 0,0
def change():
    uname=input('Enter username: ')
    pwd=input('Enter Old Password: ')
    with open('login.txt', 'r') as file:
        contents=file.read()
        ndict = ast.literal_eval(contents)
    if (uname not in ndict.keys()):
        print('Invalid Username! Please Try Again')
        print("_" * 15 + "\n")
    elif (ndict[uname] == pwd):
        npwd=input('Enter new password: ')
        ndict[uname]=npwd
        with open('login.txt', 'w') as file:
            file.write(str(ndict))
        print('Password Changed Successfully! Please Login Again to Continue!')
        print("_" * 15 + "\n")

    else:
        print('Wrong Password!')
        print("_" * 15 + "\n")
