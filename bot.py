from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class NikeBot:
    URL = "https://www.nike.com.br/Snkrs#estoque"

    PATH_EDGE = "./edgedriver_win64/msedgedriver.exe"

    PATH_CHROME = "./chromedriver_win32/chromedriver.exe"

    def __init__(self, driver):
        if driver:
            if driver == "edge":
                self.driver = webdriver.Edge(self.PATH_EDGE)
            elif driver == "chrome":
                self.driver = webdriver.Chrome(self.PATH_CHROME)
            else:
                print(driver + " is not a supported webdriver please choose an other one")
        else:
            print("A driver wasn't selected\nusage: var = NikeBot(\"edge\", url) or var = NikeBot(\"chrome\", url)")

    def open_url(self):
        try:
            self.driver.get(self.URL)
            self.driver.refresh()
        except Exception as e:
            print("Please use a valid browser")
            print(e)
            exit(1)

    def get_product(self):
        link_xpath = "//*[@id=\"DadosPaginacaoEstoque\"]/div[1]/div[1]/div/div[2]/a"
        name_xpath = "//*[@id=\"DadosPaginacaoEstoque\"]/div/div[1]/div/a/img"
        link = self.driver.find_element_by_xpath(link_xpath).get_attribute("href")
        name = self.driver.find_element_by_xpath(name_xpath).get_attribute("alt")
        print(f'Selected product: {name}')
        self.driver.get(link)

    def get_size(self, size_option1, size_option2):

        try:
            elem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, f'tamanho__id{size_option1}'))
            )
            self.driver.execute_script("arguments[0].checked = true;", elem)
            self.driver.execute_script("arguments[0].click();", elem)
            print(f'selected shoe size: {size_option1}')

        except:

            try:
                elem = WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located((By.ID, f'tamanho__id{size_option2}'))
                )
                self.driver.execute_script("arguments[0].checked = true;", elem)
                self.driver.execute_script("arguments[0].click();", elem)
                print(f'selected shoe size: {size_option2}')

            except Exception as error:
                print("invalid shoe size")
                print(error)
                self.driver.quit()

    def click_login(self):
        xpath = "/html/body/header/div[1]/div/div/div[2]/span[1]/span[3]/a"
        elem = WebDriverWait(self.driver, 5).until(  # wait for email field to load
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        self.driver.execute_script("arguments[0].click()", elem)

    def login(self, email, password):
        popup_open_test = False
        email_input_name = "emailAddress"
        pwd_input_name = "password"
        try:
            #  get fields from the form
            email_input_elem = WebDriverWait(self.driver, 10).until(  # wait for email field to load
                EC.presence_of_element_located((By.NAME, email_input_name))
            )
            pwd_input_elem = WebDriverWait(self.driver, 3).until(  # wait for email field to load
                EC.presence_of_element_located((By.NAME, pwd_input_name))
            )
            #  insert email and password
            self.driver.execute_script("arguments[0].value = arguments[1].toString()", email_input_elem, email)
            self.driver.execute_script("arguments[0].value = arguments[1].toString()", pwd_input_elem, password)
            sleep(2)
            pwd_input_elem.send_keys(Keys.ENTER)

        except Exception as error:
            print("email and/or password fields not found")
            print(error)
            self.driver.quit()
            self.driver.quit()
        try:
            popup_btn_xpath = "/html/body/div[7]/div/div[2]/input"
            popup_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, popup_btn_xpath))
            )
            self.driver.execute_script("arguments[0].click()", popup_btn)
            self.login(email, password)
        except Exception as error:
            print("The login popup did not open")
            print(error)

    def click_buy(self):
        try:
            elem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "btn-comprar"))
            )
            self.driver.execute_script("arguments[0].click()", elem)
        except Exception as error:
            print("error trying to login")
            print(error)
        if self.driver.current_url != "https://www.nike.com.br/Carrinho":
            self.click_buy()
