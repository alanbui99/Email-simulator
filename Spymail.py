# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 20:25:13 2019

@author: Bui Thang
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:30:57 2019

@author: Phil & Alan
"""
from ciphers import *
def adduser(email, password): # a function (3)
    with open("userlist.txt","a+") as userlist:    
        userlist.write(email + " " + password + "\n")
    userlist.close()
    #userlist.insert(numusers, email)
    #userdict[email] = password
print("Welcome to SPyMail!")
print("-------------------")

numusers = 0 # accumulator (1)
nummessages = 0

userlist = [] # a list (2)
userdict = {}

logoff = False



new = input("Returning user? (Y/N): ")
new = new.lower()

if new == "y":

    user = input("Username: ") # accept user input (4)
    password = input("Password: ")
    with open("userlist.txt",'r') as userlist:
        data = userlist.readlines()
    listemail = []
    listpassword = []
    for i in range(len(data)):
        pair = data[i].rstrip('\n').split(' ')
        listemail.append(pair[0])
        listpassword.append(pair[1])
    accDict = {}
    for i in range(len(listemail)):
        accDict[listemail[i]] = listpassword[i]
        
    if user in accDict.keys() and password == accDict[user]:
        print("\nWelcome!")
    else:
        print("\nIncorrect username or/and password\nAccess denied")
        logoff = True
        
elif new == "n":
    user = input("Set username: ") 
    password = input("Set password: ")   
    if user.endswith('@spymail.com'):
        with open("userlist.txt",'r') as userlist:
            data = userlist.readlines()
        data = str(data)
        
        if data.find(user) == -1: # a Boolean expression (5)
            #numusers = numusers + 1
            adduser(user, password)
            #numusers = numusers + 1
            print("\nWelcome!")
        else:
            print("\nUsername already existed.")
    else:
        print('\nUsername must end with "@spymail.com".\nPlease try again!')
        logoff = True
else:
    print("Error: wrong key")
    logoff = True

while logoff == False:
    
    command = input("\nCommands -> (Send) (Read) (Contacts) (Change password) (Logoff): ")
    command = command.lower() # string manipulation (6)
    main_menu = False
    while not main_menu:
        # a selection statement (7)
        if command == "send":        
            recipient = input("To: ")
            if recipient in accDict.keys():
                subject = input("Subject: ")
                text = input("Message: ")
                
                confirm = input("Send message? (Y/N) ")
                confirm = confirm.lower()
                
                if confirm == "y":
                    # file I/O (8)
                    message = open("mailbox.txt", "a+")
                    
                    text = scramble2Encrypt(text)
                    message.write(user + "," + recipient + "," + subject + "," + text + '\n')
                    
                    message.close()
                    
                    #nummessages = nummessages + 1
                    print("Message sent")
                    break
                else:
                    print("Draft deleted")
                    break
            else:
                print("Recipient not found")
                main_menu = True
        
        elif command == "read":
            try:
                message = open("mailbox.txt", "r")
                for line in message:
                
                    print('\n')
                    
                    mail = line.split(",")
                    # only check user's mail
                    if mail[0] == user or mail[1] == user:
                        print("From:", mail[0]) # sender
                        print("To:", mail[1]) # recipient
                        print("Subject:", mail[2])
                        decrypted = scramble2Decrypt(mail[3])
                        print("Message:", decrypted)
                    
                message.close()
                break
            except FileNotFoundError:
                print("No message")
                break
            
        elif command == "contacts":
            with open("userlist.txt",'r') as userlist:
                data = userlist.readlines()
            accountlist = []
            for i in range(len(data)):
                acc = data[i].split(' ')[0]
                accountlist.append(acc)
            for acc in accountlist:
                print(acc)
            break
        
        elif command == "change password":
            curpass = input("Current password: ")
            with open("userlist.txt",'r') as userlist:
                data = userlist.readlines()
            data = str(data)
            userend= data.find(user) +len(user)
            ruser = data[data.find(user):userend]
            rpassword = data[userend+1:userend+len(curpass)+1]
            if rpassword == curpass:
                newpass = input("New password: ")
                with open("userlist.txt", "r") as f:
                    lines = f.readlines()
                with open("userlist.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != user + " " + curpass:
                            f.write(line)
                f.close()
                adduser(user,newpass)
                print("Password successfully changed")
                break
                
            else:
                print("\nIncorrect current password")
                main_menu = True
        
        elif command == "logoff":
            logoff = True
            print("Bye!")
            break
        
        else:
            print("Invalid command\n")
            break
            