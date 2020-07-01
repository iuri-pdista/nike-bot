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
    
    def get_size(self, Size_option1, Size_option2):
        try:
            Size_option1 = self.driver.find_element_by_id("tamanho__id" + Size_option1)
            Size_option1.get_attribute("disabled") != "disabled" 
            Size_option1.click()
        except:
            Size_option2 = self.driver.find_element_by_id("tamanho__id" + Size_option2)
            Size_option2.get_attribute("disabled") != "disabled"
            Size_option1.click()
        else:
            print ("The values you selected are not available")
            #we need to think what to do when the sizes are not available, because exitting and running the script all again is not a possibility

    def login_checker (self):
        #there is two ways of doing it
        # FIRST
        #xpath = "//*[@id=\"header\"]/div[1]/div/div/div[2]/span[1]/span[3]"
        #ClassPicker = self.driver.find_element_by_xpath(xpath).get_attribute("class")
        #if "nao_logado" in ClassPicker:
        #    print ("You are not logged in")
        #    xpath_to_login = "//*[@id=\"anchor-acessar\"]"
        #    xpath_to_login.click()
        #    print ("Please Login")
        #else:
        #    return True  
        #
        # SECOND
        xpath = "//*[@id=\"header\"]/div[1]/div/div/div[2]/span[1]/span[1]"
        try:
            self.driver.find_element_by_xpath(xpath)
            print ("You are logged in")
            return True
        except:
            xpath_to_login = "//*[@id=\"anchor-acessar\"]"
            xpath_to_login.click()
            print ("Please Login")
    def add_to_cart (self):
        xpath = "//*[@id=\"btn-comprar\"]"              
        click(xpath)
    def finalize(self):
        xpath_cart = "//*[@id=\"carrinho\"]/div[3]/div[5]/a"
        xpath_identification = "//*[@id=\"seguir-pagamento\"]"
        xpath_payment = "//*[@id=\"confirmar-pagamento\"]"
        click(xpath_cart)
        #we need to insert a little pause to the page load
        click(xpath_identification)
        #same
        #we need to create exceptions to check if the fields are filled
        click(xpath_payment)
        
