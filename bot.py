from time import sleep

from selenium import webdriver


class NikeBot:

    URL = "https://www.nike.com.br/Snkrs#estoque"

    PATH_EDGE = "./edgedriver_win64/msedgedriver.exe"

    PATH_CHROME = "./chromedriver_win32/chromedriver.exe"

    def __init__(self, driver):
        if driver:
            if driver == "edge":
                self.driver = webdriver.Edge(self.PATH_EDGE)
            elif driver == "chrome":
                self.driver = webdriver.Edge(self.PATH_CHROME)
            else:
                print(driver + " is not a supported webdriver please choose an other one")
        else:
            print("A driver wasn't selected\nusage: var = NikeBot(\"edge\", url) or var = NikeBot(\"chrome\", url)")

    def open_url(self):
        try:
            self.driver.get(self.URL)
        except:
            print("Please use a valid browser")
            exit(1)

    def click(self, xpath):
        elem = self.driver.find_element_by_xpath(xpath)
        if elem:
            elem.click()
            return elem
        else:
            print("Element not found")
            return False

    def get_product(self):
        xpath = "//*[@id=\"DadosPaginacaoEstoque\"]/div[1]/div[1]/div/div[2]/a"
        link = self.driver.find_element_by_xpath(xpath).get_attribute("href")
        self.driver.get(link)
    #  later remember to do this 
    # def get_number(self):
    

    def login_checker (self):
        #there is two ways of doing it
        # FIRST
        #xpath = "//*[@id=\"header\"]/div[1]/div/div/div[2]/span[1]/span[3]"
        #ClassPicker = self.driver.find_element_by_xpath(xpath).get_attribute("class")
        #if "nao_logado" in ClassPicker:
        #    print ("You are not logged in")
        #    return False
        #else:
        #    return True  
        #
        # SECOND
        xpath = "//*[@id=\"header\"]/div[1]/div/div/div[2]/span[1]/span[1]"
        try:
            self.driver.find_element_by_xpath(xpath)
            print ("You are logged in")
        except:
            xpath_to_login = "//*[@id=\"anchor-acessar\"]"
            xpath_to_login.click()
            print ("Please Login")


