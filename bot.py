from selenium import webdriver


class NikeBot:

    URL = ""

    PATH_EDGE = "./edgedriver_win64/msedgedriver.exe"

    PATH_CHROME = "./chromedriver_win32/chromedriver.exe"

    def __init__(self, driver, url):
        if driver:
            if driver == "edge":
                self.driver = webdriver.Edge(self.PATH_EDGE)
            elif driver == "chrome":
                self.driver = webdriver.Edge(self.PATH_CHROME)
            else:
                print(driver + " is not a supported webdriver please choose an other one")
            self.URL = url
        else:
            print("A driver wasn't selected\nusage: var = NikeBot(\"edge\") or var = NikeBot(\"chrome\")")

    def open_url(self):
        if self.URL:
            self.driver.get(self.URL)
        else:
            print("An url must be passed to the object parameters")

    def click(self, xpath):
        elem = self.driver.find_element_by_xpath(xpath)
        if elem:
            elem.click()
            return elem
        else:
            print("Element not found")
            return False
