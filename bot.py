from selenium import webdriver
    

   class NikeBot():
     def _init_(self):
       self.driver = webdriver.chrome()
        
     def click(self , XPath): 
        elem = self.driver.get_element_by_xpath(XPath)
        if (elem):
            elem.click()
            return elem
        else 
            print ("Element not found")
            return False              
    
    #go to snkrs page 
    click(self, '//*[@id="header"]/div[1]/div/div/div[1]/ul/li[4]/a')
    
    #go to stock
    click(self, '//*[@id="estoque-tab"]')
