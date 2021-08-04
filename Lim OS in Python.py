import os
import time
from sys import exit
from getpass import getuser

username = ""
def initialize():
    global username
    os.system("cls")
    username = getuser()
    
def get_formatted_time():
    return time.strftime('%H:%M:%S', time.localtime(time.time()))

def help(args):
    print("help:")
    if len(args) == 0:
        print("""When you send command, you cannot send \"/\" in your command.
/help    Get help.
/info    Get information.
/echo    Output something.
/clear   Clear or delete command data.
/mkdir   Create a directory.
/listdir List all directories in this path.
/cd      Change your path.
/editer  Edit a file.
/run     Run a script.
You can try to send "help help" to learn more.""")
    else:
        if args[0] == "help":
            print("/help <command>     Get that command's help.")
        elif args[0] == "info":
            print("/info               Get information.")
        elif args[0] == "echo":
            print("/echo <text>        Output that text.")
        elif args[0] == "clear":
            print("""/clear <type>       Clear something.
<type>:command      Delete command area things.
<type>:all          Delete all data (be careful!).""")
        elif args[0] == "mkdir":
            print("""/mkdir <dirName>    Create a directory.
The directory name cannot include \" \", \";\" or \"/\".""")
        elif args[0] == "listdir":
            print("/listdir            List all directories in this path.")
        elif args[0] == "cd":
            print("/cd <path/dir>      Change your path.")
        elif args[0] == "editor":
            print("""Sorry the help of editer is too long.
/editer help        Get its help.""")
        elif args[0] == "run":
            print("/run <filename>     Run a script.")
        else:
            print("Sorry, didn't found that command.")

def info():
    print("info:")
    print("""Lim OS v1.2.000 by Markchai
Lim OS in Python v0.1.0 by Scratcher-wrj
CC BY-NC 4.0
""")

def echo(args):
    print("\n" + args[0])

def clear(args):
    if len(args) == 0:
        os.system("cls")
    else:
        if args[0] == "command":
            os.system("cls")
            print("Commands has been clear.")
        elif args[0] == "all":
            yesorno = input("Delete all data? (Y/N) ")
            if yesorno.lower() == "y":
                print("Deleting all data...")
                os.system("cls")
        else:
            print("Err!")


initialize()
while True:
    command = input("Enter command or enter \"exit\" to exit: ")
    print("\r[{} {}] {}".format(get_formatted_time(), username, command))
    print("[{} SYSTEM] ".format(get_formatted_time()), end="")

    splitted_command = command.split()
    command_name = splitted_command.pop(0)
    if command_name == "help":
        help(splitted_command)
    elif command_name == "info":
        info()
    elif command_name == "echo":
        echo(splitted_command)
    elif command_name == "clear":
        clear(splitted_command)
    elif command_name == "exit":
        if input("Are you sure to exit Lim OS? (Enter \"Y\" to exit)").lower() == "y":
            exit()
    else:
        print("Unknown command. Enter \"help\" for help.")
