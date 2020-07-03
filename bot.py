from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        xpath = "//*[@id=\"DadosPaginacaoEstoque\"]/div[1]/div[1]/div/div[2]/a"
        link = self.driver.find_element_by_xpath(xpath).get_attribute("href")
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