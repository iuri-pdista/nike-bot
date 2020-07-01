from bot import NikeBot
import sys


def send_help():
    print("Usage:\n python script.py -b <browser_name> or python script.py --browser <browser_name> ")


def initialize_script():
    if len(sys.argv) > 1:
        i = 0
        while i < len(sys.argv):
            if sys.argv[i] == "-b" or sys.argv[i] == "--browser":
                return sys.argv[i + 1] if sys.argv[i + 1] else "chrome"
            else:
                send_help()
            i += 1
    else:
        send_help()
        exit()


browser = initialize_script()

bot = NikeBot(browser)

bot.open_url()
bot.get_product()
