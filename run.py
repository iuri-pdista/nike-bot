from bot import NikeBot
import sys


def send_help():
    print("Usage:\n python script.py -b <browser_name> or python script.py --browser <browser_name> ")
    exit(1)


def initialize_script():

    browser_name = ""

    if len(sys.argv) > 1:

        i = 0
        while i < len(sys.argv):

            try:
                if sys.argv[i] == "-b" or sys.argv[i] == "--browser":
                    browser_name = sys.argv[i + 1] if sys.argv[i + 1] else ""
            except:
                send_help()

            i += 1

        if browser_name == "":
            send_help()
        else:
            return browser_name
    else:
        print("You didn't pass any arguments")
        send_help()
        exit(1)


browser = initialize_script()

bot = NikeBot(browser)

bot.open_url()
bot.get_product()
bot.get_size("43", "43")
bot.click_login()
bot.login("teste@teste.com.br", "iuri1234556662")
