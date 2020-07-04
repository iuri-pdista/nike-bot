import sys
from colorama import Fore
from bot import NikeBot
from os import system
from time import sleep
from sys import platform


def show_logo():
    logo = """\n\n
                 .........                   .........                     
               @@@@@@@@@@@@                @@@@@@@@@@@@                   
               @@@@@@@@@@@@                @@@@@@@@@@@@                   
               @@@@@@@@@@@@                @@@@@@@@@@@@                   
               @@@@@@@@@@@@                @@@@@@@@@@@@                   
                                                                          
                                                                          
                                                          %          
               (@                                    @@@@&                
              @@                          ,@@@@@@@@&                      
            @@@@               .@@@@@@@@@@@@@&                            
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                  
           @@@@@@@@@@@@@@@@@@@@@@&                                        
           @@@@@@@@@@@@@@@@@                                              
            @@@@@@@@@%  \n
       ███▄    █  ██▓ ██ ▄█▀▓█████     ▄▄▄▄    ▒█████  ▄▄▄█████▓
       ██ ▀█   █ ▓██▒ ██▄█▒ ▓█   ▀    ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
      ▓██  ▀█ ██▒▒██▒▓███▄░ ▒███      ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
      ▓██▒  ▐▌██▒░██░▓██ █▄ ▒▓█  ▄    ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
      ▒██░   ▓██░░██░▒██▒ █▄░▒████▒   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
      ░ ▒░   ▒ ▒ ░▓  ▒ ▒▒ ▓▒░░ ▒░ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
      ░ ░░   ░ ▒░ ▒ ░░ ░▒ ▒░ ░ ░  ░   ▒░▒   ░   ░ ▒ ▒░     ░    
         ░   ░ ░  ▒ ░░ ░░ ░    ░       ░    ░ ░ ░ ░ ▒    ░      
               ░  ░  ░  ░      ░  ░    ░          ░ ░           
                                            ░       
                                               
    [*] Script made by: guiguat and iuri-pdista\n
    """
    print(Fore.RED + logo)


def send_help(e):
    message = """
usage: python run.py [-b | --browser <browser name>] [-e | --email <email>] 
[-p | --password <password>] [-s | --size <size1>,<size2>] optional => [-n | --name <snkr name>]
        
    """
    print(Fore.RED + message)
    print(Fore.MAGENTA + e + Fore.RED)
    exit(1)


def initialize_script():
    browser_name = ""
    email_param = ""
    pwd_param = ""
    size_param = ""
    name_param = ""

    if len(sys.argv) > 1:
        i = 0
        while i < len(sys.argv):

            try:
                if sys.argv[i] == "-b" or sys.argv[i] == "--browser":
                    browser_name = sys.argv[i + 1] if sys.argv[i + 1] else ""

                elif sys.argv[i] == "-e" or sys.argv[i] == "--email":
                    email_param = sys.argv[i + 1] if sys.argv[i + 1] else ""

                elif sys.argv[i] == "-p" or sys.argv[i] == "--password":
                    pwd_param = sys.argv[i + 1] if sys.argv[i + 1] else ""

                elif sys.argv[i] == "-s" or sys.argv[i] == "--size":
                    size_param = sys.argv[i + 1] if sys.argv[i + 1] else ""

                elif sys.argv[i] == "-n" or sys.argv[i] == "--name":
                    name_param = sys.argv[i + 1] if sys.argv[i + 1] else ""

            except Exception as e:
                send_help(e)

            i += 1

        if browser_name == "" or email_param == "" or pwd_param == "" or size_param == "":
            send_help("")
        else:
            return browser_name, email_param, pwd_param, size_param, name_param
    else:
        send_help("[*] You didn't pass any arguments")


[browser, email, password, size, name] = initialize_script()
size = str(size).strip().split(",")

if email == "" or password == "":
    send_help("")

bot = NikeBot(browser)

if platform == "win32":
    system("cls")
else:
    system("clear")

show_logo()
bot.driver.get("https://www.nike.com.br/Snkrs")
bot.click_login()
bot.login(email, password)
bot.open_url()

if name != "":
    bot.alt_get_product(name)
else:
    bot.get_product()

bot.set_size(size[0], size[1])
bot.login_checker(email, password)
bot.click_buy()
bot.checkout()
bot.finish()
final_msg = ">>>OUR JOB HERE IS DONE, PLEASE CONFIRM YOUR DATA, FINISH THE PURCHASE MANUALLY AND \n ENJOY YOUR SNKRS :)"
print(Fore.BLUE + final_msg + Fore.RESET)
