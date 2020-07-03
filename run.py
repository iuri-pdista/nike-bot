from time import sleep

from bot import NikeBot
import sys


def send_help(e):
    print("Usage:\n python script.py -b <browser_name> -e <email> -p <password> ")
    print("\n or python script.py --browser <browser_name> --email <email> --password <password>")
    print(e)
    exit(1)


def initialize_script():

    browser_name = ""
    email_param = ""
    pwd_param = ""

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
            except Exception as e:
                send_help(e)

            i += 1

        if browser_name == "":
            send_help("")
        else:
            return browser_name, email_param, pwd_param
    else:
        print("You didn't pass any arguments")
        send_help("")


[browser, email, password] = initialize_script()

if email == "" or password == "":
    send_help("")

bot = NikeBot(browser)
bot.driver.get("https://www.nike.com.br/Snkrs")
bot.click_login()
#  need to reconfigure the email and pwd as parameters
bot.login("iuricorrea05@gmail.com", "t2mYQk2Mx6Dq9_-")
awns = input("\n \nType yes or y when login is completed. If you want to close the script type anything different: ")
if awns == "yes" or awns == "y":
    bot.open_url()
    bot.get_product()
    bot.get_size("43", "43")
    #  need to pass the sizes as parameters
    bot.click_buy()
else:
    exit(0)