import os
import time
from sys import exit
from getpass import getuser

username = ""
currently_path = "limos"
def initialize():
    """初始化"""
    global username
    # 清空终端内容
    os.system("cls")

    # 获取登录了Windows的用户名
    username = getuser()

    # 创建用于存放 Lim OS 文件的文件夹
    if not os.path.exists("limos"):
        os.mkdir("limos")
    
def get_formatted_time():
    """返回格式化的时间 (HH:MM:SS)"""
    return time.strftime('%H:%M:%S', time.localtime(time.time()))

def help(args):
    """help命令"""
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
The directory name cannot include '\\', '/', ':', '*', '?', '"', '<', '>' or '|'.""")
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
    """info命令"""
    print("info:")
    print("""Lim OS v1.2.000 by Markchai
Lim OS in Python v0.1.1 by Scratcher-wrj
CC BY-NC 4.0
""")

def echo(args):
    """echo命令"""
    print("\n" + args[0])

def clear(args):
    """clear命令"""
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

def mkdir(args):
    """mkdir命令"""
    global currently_path
    if len(args) == 1 and not (("\\" in args[0]) or ("/" in args[0]) or ("." in args[0]) or (":" in args[0]) or ("*" in args[0]) or ("?" in args[0]) or ("<" in args[0]) or (">" in args[0]) or ("|" in args[0]) or ("\"" in args[0])):
        print("Creating directory \"{}\"...".format(args[0]))
        if os.path.exists(os.path.join(currently_path, args[0])):
            print("Directory \"{}\" already exists.".format(args[0]))
        else:
            os.mkdir(os.path.join(currently_path, args[0]))
    else:
        print("Err! Enter \"help mkdir\" to learn more.")

def listdir():
    """listdir命令"""
    global currently_path
    print("All directories in this path:")
    for filename in os.listdir(currently_path):
        print(filename)

def cd(args):
    global currently_path
    if len(args) == 1:
        if os.path.exists(os.path.join(currently_path, args[0])):
            currently_path = os.path.join(currently_path, args[0])
            print("Successful! Currently path: " + currently_path)
        else:
            print("File {} does not exist.")
    else:
        print("Err! Enter \"help cd\" to learn more.")


initialize()
while True:
    command = input("Enter command (or enter \"exit\" to exit): ")
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
    elif command_name == "mkdir":
        mkdir(splitted_command)
    elif command_name == "listdir":
        listdir()
    elif command_name == "cd":
        cd(splitted_command)
    elif command_name == "exit":
        if input("Are you sure to exit Lim OS? (Enter \"Y\" to exit)").lower() == "y":
            exit()
    else:
        print("Unknown command. Enter \"help\" for help.")
