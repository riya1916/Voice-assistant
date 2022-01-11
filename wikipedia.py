from selenium import webdriver


class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe')

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element('//*[@id="search-form"]/fieldset/button')
        enter.click()

# assist=infow()
# assist.get_info("black hole")
