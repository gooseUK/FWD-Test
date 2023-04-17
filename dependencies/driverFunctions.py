from dependencies.driverDependencies import *

class SearchType(Enum):
    ID = "id"
    CLASS = "class"
    CSS = "css"
    XPATH = "xpath"
    NAME = "name"

class DriverFunctions:
    
    global driver
    
    def __init__(self):
        pass

    def InitDriver(self):
        options = Options()
        options.headless = True
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.WaitTillPageLoad()
        
    def GetUrl(self):
        self.WaitTillPageLoad()
        sleep(5)
        return self.driver.current_url

    def InputText(self, search, text):
        search.send_keys(text)

    def WaitTillPageLoad(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def WaitTillLoad(self, input, typeOfSearch):
        self.WaitTillPageLoad()
        if(typeOfSearch == SearchType.ID):
            elementExists = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, input)))
            search = self.driver.find_element(By.ID, input)
            return search

        if(typeOfSearch == SearchType.XPATH):
            elementExists = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, input)))
            search = self.driver.find_element(By.XPATH, input)
            return search
            
        if(typeOfSearch == SearchType.CLASS):
            elementExists = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, input)))
            search = self.driver.find_element(By.CLASS_NAME, input)
            return search

        if(typeOfSearch == SearchType.CSS):
            elementExists = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, input)))
            search = self.driver.find_element(By.CSS_SELECTOR, input)
            return search

        if(typeOfSearch == SearchType.NAME):
            elementExists = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, input)))
            search = self.driver.find_element(By.NAME, input)
            return search

    def GoToPage(self, website):
        self.WaitTillPageLoad()
        self.driver.get(website)
        self.WaitTillPageLoad()
        
    def CloseDriver(self):
        self.WaitTillPageLoad()
        self.driver.close()

    def GetElementsGroup(self, input, typeOfSearch):
        self.WaitTillPageLoad()
        if(typeOfSearch == SearchType.CLASS):
            elementExists = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, input)))
            return self.driver.find_elements(By.CLASS_NAME, input)