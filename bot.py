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
