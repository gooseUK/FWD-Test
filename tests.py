from dependencies.driverFunctions import DriverFunctions, SearchType
from dependencies.dependencies import *
from dependencies.Assertions import Assertions

class Tests:

    global driver
    global start_url
    global test
    
    def __init__(self):
        self.test = Assertions()
        self.driver = DriverFunctions()
        self.start_url = r'https://futureworkdesign-dev.azurewebsites.net/'

    def LoginRoutine(self, username = username_1, password = password_1):
        
        #Check if logout required
        self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/')
        if(self.driver.GetUrl() == 'https://futureworkdesign-dev.azurewebsites.net/conversations'):
            self.LogoutRoutine()
        
        self.driver.GoToPage(self.start_url)
        search = self.driver.WaitTillLoad('page-navigation-button--sessions', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('email_address', SearchType.ID)
        self.driver.InputText(search, username)
        
        search = self.driver.WaitTillLoad('password', SearchType.ID)
        self.driver.InputText(search, password)
        
        search = self.driver.WaitTillLoad('page-form-button--submit', SearchType.ID)
        search.click()

    def LogoutRoutine(self):  
        try:
            self.driver.WaitTillPageLoad()          
            self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/')
            search = self.driver.WaitTillLoad('page-navigation-button--sessions', SearchType.ID)
            search.click()
        except Exception as e:
            self.test.CleanupFailure(e, 'Logout Routine')

    def RemoveConversation(self, id, user=username_1, password=password_1):

        response = ''
        if(id != ''):
            try:
                self.driver.InitDriver()
                self.LoginRoutine(user, password)
                sleep(3)
                token = self.driver.driver.execute_script("return window.localStorage.getItem('userDetails');")
                sleep(3)
                token = json.loads(token)['token']
                sleep(3)
                url = "https://dluchapi.azurewebsites.net/api/conversation"
                payload = {"conversationId": id}
                headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}    
                response = requests.delete(url, data=json.dumps(payload), headers=headers)
                response = response.json()
                response = response['statusCode']
                self.LogoutRoutine()
                self.driver.CloseDriver()
            except Exception as e:
                self.test.CleanupFailure(e, 'Remove Conversation')

            if(response == 200):
                print('\033[96m' + '[database] Conversation Removed' + '\033[0m')
            else:
                print('\033[96m' + '[database] Conversation Removal has failed' + '\033[0m')

    def ClearAllConversations(self, user, password):
        if(user != '' and password != ''):
            self.driver.InitDriver()
            self.LoginRoutine(user, password)
            sleep(3)
            token = self.driver.driver.execute_script("return window.localStorage.getItem('userDetails');")
            sleep(3)
            token = json.loads(token)['token']
            sleep(3)
            url = "https://dluchapi.azurewebsites.net/api/conversations"
            payload = {}
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}    
            response = requests.get(url, data=json.dumps(payload), headers=headers)
            response = response.json()
            responseStatus = response['statusCode']
            responseConversations = response['content']['conversations']

            deleteSuccess = 0
            conversationIdsLength = 0

            if(responseStatus == 200):
                print('\033[96m' + '[database] Conversations pulled correctly' + '\033[0m')

                conversationIds = []

                for conversation in responseConversations:
                    conversationIds.append(conversation['id'])

                conversationIdsLength = len(conversationIds)

                url = "https://dluchapi.azurewebsites.net/api/conversation"

                i = 1

                for conversationId in conversationIds:
                    payload = {"conversationId": conversationId}
                    print('\033[96m' + '[Mass Cleanup] Deleting conversation ' + str(i) + '/' + str(len(conversationIds))  + '\033[0m')
                    response = requests.delete(url, data=json.dumps(payload), headers=headers)
                    response = response.json()
                    responseStatus = response['statusCode']
                    if(responseStatus == 200):
                        print('\033[96m' + '[database] Conversation Removed' + '\033[0m')
                        deleteSuccess = deleteSuccess + 1      
                    else:
                        print('\033[96m' + '[database] Conversation Removal has failed' + '\033[0m')

                    i = i + 1

            else:
                print('\033[96m' + '[database] Conversations retrieval has failed' + '\033[0m')

            print('\033[96m' + '[Mass Cleanup] Successful deletions: ' + str(deleteSuccess) + '/' + str(conversationIdsLength) + '\033[0m')
            self.LogoutRoutine()
            self.driver.CloseDriver()

    def MassCleanup(self):
        self.ClearAllConversations(username_1, password_1)
        self.ClearAllConversations(username_2, password_2)
        self.ClearAllConversations(username_3, password_3)
        print('\033[96m' + '[Mass Cleanup] Finished' + '\033[0m')

    def NotYetImplemented(self, testTag):
        print('\033[93m' + '[warning] ' + testTag + ' not yet implemented' + '\033[0m')

    def FilloutQuestionaire(self):
        #select through questionaire first page
        sleep(5)
        search = self.driver.WaitTillLoad('util--question-0-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-1-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-2-response-4', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-3-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-4-response-4', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-5-response-4', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-6-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('page-form-button--button', SearchType.ID)
        search.click()
        
        #select through questionaire second page
        search = self.driver.WaitTillLoad('util--question-0-response-0', SearchType.ID)
        search.click()
        #util--question-0-response-0
        search = self.driver.WaitTillLoad('util--question-1-response-4', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-2-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-3-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-4-response-4', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-5-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-6-response-4', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('page-form-button--button', SearchType.ID)
        search.click()
        
        #select through questionaire third page
        search = self.driver.WaitTillLoad('util--question-0-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-1-response-4', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-2-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-3-response-4', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-4-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-5-response-4', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-6-response-4', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('page-form-button--button', SearchType.ID)
        search.click()
        
        #select through questionaire fourth page
        search = self.driver.WaitTillLoad('util--question-0-response-4', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-1-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-2-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-3-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-4-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-5-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-6-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('page-form-button--button', SearchType.ID)
        search.click()
        
        #select through questionaire fifth page
        search = self.driver.WaitTillLoad('util--question-0-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-1-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-2-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-3-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-4-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-5-response-4', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('util--question-6-response-0', SearchType.ID)
        search.click()
        
        search = self.driver.WaitTillLoad('page-form-button--button', SearchType.ID)
        search.click()

    def FilloutNewConversation(self, user=username_2):
        sleep(1)
        self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/conversations/new')
        sleep(1)    
        search = self.driver.WaitTillLoad('email_address', SearchType.ID)
        search.send_keys(user)
        search = self.driver.WaitTillLoad('page-form-button--complete', SearchType.ID)
        search.click()

        search = self.driver.WaitTillLoad('forename', SearchType.ID)
        search.send_keys('OtherTest')

        search = self.driver.WaitTillLoad('surname', SearchType.ID)
        search.send_keys('User')

        search = self.driver.WaitTillLoad('email_address', SearchType.ID)
        search.send_keys(user)

        search = self.driver.WaitTillLoad('content', SearchType.ID)
        search.send_keys('Test message to user')

        search = self.driver.WaitTillLoad('employee', SearchType.ID)
        search.click()

        search = self.driver.WaitTillLoad('page-form-button--submit', SearchType.ID)
        search.click()
        sleep(3)

    def StartQuestionaire(self, id):
        self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/conversations')
        search = self.driver.WaitTillLoad('//*[@id=\"cell-4-' + id + '\"]/a', SearchType.XPATH)
        search.click()

        search = self.driver.WaitTillLoad('//*[@id="util--question-0-response-4"]', SearchType.XPATH)
        search.click()

        search = self.driver.WaitTillLoad('page-form-button--submit-guided', SearchType.ID)
        search.click()

        search = self.driver.WaitTillLoad('page-navigation-button--start', SearchType.ID)
        search.click()

    def DeleteAccount(self, email):
        try:
            self.driver.InitDriver()
            self.LoginRoutine(username_admin, password_admin)
            sleep(3)
            token = self.driver.driver.execute_script("return window.localStorage.getItem('userDetails');")
            sleep(3)
            token = json.loads(token)['token']
            sleep(3)
            url = 'https://dluchapi.azurewebsites.net/api/users?email=' + email
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            
            response = requests.get(url, headers=headers)
            response = response.json()
            response_status = response['statusCode']
            if(response_status == 200):
                response_user_id = response['content']['user']['id']            
                url = 'https://dluchapi.azurewebsites.net/api/users'
                payload = {"userId": response_user_id}
                headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
                response = requests.delete(url, data=json.dumps(payload), headers=headers)
                response = response.json()
                response_status = response['statusCode']
                if(response_status == 200):
                    print('\033[96m' + '[database] Account Deleted' + '\033[0m')
                else:
                    print('\033[96m' + '[database] Account deletion has failed' + '\033[0m')
        except Exception as e:
            self.test.CleanupFailure(e, 'Delete Account')

    def LogIntoEmail(self):
        self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/sessions/new')


######TESTS######

    def driver_test(self):
        #arrange
        self.driver.InitDriver()
        testTag = 'driver_test'
        url = None
        
        #act
        try:
            self.driver.GoToPage(self.start_url)
            url = self.driver.GetUrl()
        except Exception as e:
            self.test.ErrorMsg(e, testTag)

        #assert
        self.test.Equal(url, self.start_url, testTag)
        
        #cleanup
        self.driver.CloseDriver()
        
        return True

    def Test_1(self):
        #init
        testTag = 'Test_1'
        arrangeComplete = False
        
        #arrange
        try:
            logoutVerifier = ''
            self.driver.InitDriver()
            arrangeComplete = True
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)
                
        #act
        if(arrangeComplete):
            try:
                self.LoginRoutine()
                sleep(1)
                self.LogoutRoutine()
                sleep(2)
                search = self.driver.WaitTillLoad('//*[@id="root"]/div/div/div[2]/div/div/p', SearchType.XPATH)
                logoutVerifier = search.text
            except Exception as e:
                self.test.ActFailure(e, testTag)
            
            #assert
            self.test.Equal(logoutVerifier, 'You have successfully logged out.', testTag)
        
        #cleanup
        self.driver.CloseDriver()        

    def Test_2(self):
        #init
        testTag = 'Test_2'
        arrangeComplete = False
        
        #arrange
        try:
            self.driver.InitDriver()
            self.LoginRoutine()
            url = ''
            arrangeComplete = True
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)

        if(arrangeComplete):
            #act
            try:
                search = self.driver.WaitTillLoad('//*[@id="root"]/header/div/div/div/div[2]/ul/li[2]/a', SearchType.XPATH)
                search.click()
                url = self.driver.GetUrl()
            except Exception as e:
                self.test.ArrangeFailure(e, testTag='Test_2: Dashboard > Resources')

            #assert
            self.test.Equal(url, 'https://futureworkdesign-dev.azurewebsites.net/resources', testTag='Test_2: Dashboard > Resources')
            search = None
            
            #act
            try:
                search = self.driver.WaitTillLoad('//*[@id="root"]/header/div/div/div/div[2]/ul/li[1]/a', SearchType.XPATH)
                search.click()
                url = self.driver.GetUrl()
            except Exception as e:
                self.test.ActFailure(e, testTag='Test_2: Resources > Dashboard')
                
            #assert
            self.test.Equal(url, 'https://futureworkdesign-dev.azurewebsites.net/conversations', testTag='Test_2: Resources > Dashboard')
            search = None
            
            #act
            try:
                search = self.driver.WaitTillLoad('//*[@id="root"]/header/div/div/div/div[2]/ul/li[3]/a', SearchType.XPATH)
                search.click()
                url = self.driver.GetUrl()
            except Exception as e:
                self.test.ActFailure(e, testTag='Test_2: Dashboard > Profile')
                
            #assert
            self.test.Equal(url, 'https://futureworkdesign-dev.azurewebsites.net/users/edit', testTag='Test_2: Dashboard > Profile')
            search = None
            
            #act
            try:
                search = self.driver.WaitTillLoad('//*[@id="page-navigation-button--home"]', SearchType.XPATH)
                search.click()
                url = self.driver.GetUrl()
            except Exception as e:
                self.test.ActFailure(e, testTag='Test_2: Profile > Dashboard via Logo')
                
            #assert
            self.test.Equal(url, 'https://futureworkdesign-dev.azurewebsites.net/conversations', testTag='Test_2: Profile > Dashboard via Logo')
        
        #cleanup
        self.LogoutRoutine()
        self.driver.CloseDriver()

    def Test_3(self):
        #init
        testTag = 'Test_3'
        arrangeComplete = False
        
        #arrange
        try:
            self.driver.InitDriver()
            self.LoginRoutine()
            search = None      
            arrangeComplete = True      
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)
        
        #act
        if(arrangeComplete):
            try:
                search = self.driver.WaitTillLoad('//*[@id="root"]/div[2]/div/div', SearchType.XPATH)
            except Exception as e:
                self.test.ActFailure(e, testTag)

            #assert
            self.test.Found(search, testTag)
        
        #cleanup
        self.LogoutRoutine()
        self.driver.CloseDriver()

    def Test_4(self):
        #init
        testTag = 'Test_4'
        arrangeComplete = False        
        
        #arrange
        try:
            self.driver.InitDriver()
            self.LoginRoutine()
            url = ''
            urlVerifier = 'https://futureworkdesign-dev.azurewebsites.net/conversations/new'
            arrangeComplete = True
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)
        
        #act
        if(arrangeComplete):
            try:
                sleep(2)
                search = self.driver.WaitTillLoad('page-navigation-button--create', SearchType.ID)
                search.click()
                sleep(2)
                url = self.driver.GetUrl()
            except Exception as e:
                self.test.ActFailure(e, testTag)
            
            #assert
            self.test.Equal(url, urlVerifier, testTag)
        
        #cleanup
        self.LogoutRoutine()
        self.driver.CloseDriver()

    def Test_5(self):
        #init
        testTag = 'Test_5'
        arrangeComplete = False
        
        #arrange
        try:
            self.driver.InitDriver()
            self.LoginRoutine()
            sleep(5)
            self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/conversations/new')
            nonExistantUser = 'doesntExist@nothere.com'
            errorVerifier = ''
            search = self.driver.WaitTillLoad('email_address', SearchType.ID)
            search.send_keys(nonExistantUser)
            search = self.driver.WaitTillLoad('page-form-button--complete', SearchType.ID)
            arrangeComplete = True            
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)
            
        #act
        if(arrangeComplete):
            try:
                search.click()
                search = self.driver.WaitTillLoad('//*[@id="root"]/div/div/div/div/p[1]', SearchType.XPATH)
                errorVerifier = search.text
            except Exception as e:
                self.test.ActFailure(e, testTag)
        
            #assert
            self.test.Equal(errorVerifier, 'This user isn\'t registered on the system, click the button below to invite them', testTag)
        
        #cleanup
        self.LogoutRoutine()
        self.driver.CloseDriver()            

    def Test_6(self):
        #init
        testTag = 'Test_6'
        arrangeComplete = False
        
        #arrange
        try:
            self.driver.InitDriver()
            self.LoginRoutine()
            sleep(5)
            self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/conversations/new')
            nameVerifier = ''
            search = self.driver.WaitTillLoad('email_address', SearchType.ID)
            search.send_keys(username_2)
            search = self.driver.WaitTillLoad('page-form-button--complete', SearchType.ID)
            arrangeComplete = True
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)
        
        #act
        if(arrangeComplete):
            try:
                search.click()
                search = self.driver.WaitTillLoad('//*[@id="root"]/div/div/div/div/p', SearchType.XPATH)
                nameVerifier = re.search(r'\((.*?)\)', search.text).group(1)    
            except Exception as e:
                self.test.ActFailure(e, testTag)
            
            #assert
            self.test.Equal(nameVerifier, username_2, testTag)
        
        #cleanup
        self.LogoutRoutine()
        self.driver.CloseDriver()

    def Test_7(self):
        #init
        testTag = 'Test_7'
        arrangeComplete = False
        
        #arrange
        try:
            self.driver.InitDriver()
            self.LoginRoutine()
            arrangeComplete = True
        except Exception as e:        
            self.test.ArrangeFailure(e, testTag)
        
        #act
        if(arrangeComplete):
            try:
                pass
            except Exception as e:
                self.test.ActFailure(e, testTag)
            
            #assert
            self.NotYetImplemented(testTag)
        
        #cleanup
        self.LogoutRoutine()
        self.driver.CloseDriver()

    def Test_8(self):
        #init
        testTag = 'Test_8'
        arrangeComplete = False
        
        #arrange
        try:
            self.driver.InitDriver()
            self.LoginRoutine()
            sleep(5)
            self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/conversations/new')
            url = ''
            arrangeComplete = True
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)
            
        #act
        if(arrangeComplete):
            try:
                self.FilloutNewConversation()
                url = self.driver.GetUrl()
                id = re.search(r'[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}', url).group(0)
                self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/conversations')
                search = self.driver.WaitTillLoad('//*[@id=\"cell-4-' + id + '\"]/a', SearchType.XPATH)
                search.click()
                url = self.driver.GetUrl()
            except Exception as e:
                self.test.ActFailure(e, testTag)

            #assert
            self.test.Equal(url, 'https://futureworkdesign-dev.azurewebsites.net/conversations/' + id + '/team-member-prep/new', testTag)
            
        #cleanup
        self.LogoutRoutine()
        self.driver.CloseDriver()
        self.RemoveConversation(id)

    def Test_9(self):
        #init
        testTag = 'Test_9'
        arrangeComplete = False
        
        #arrange
        try:
            testTag = 'Test_9'
            self.driver.InitDriver()
            self.LoginRoutine()
            sleep(5)
            self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/conversations/new')
            self.FilloutNewConversation()
            url = self.driver.GetUrl()
            id = re.search(r'[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}', url).group(0)
            self.StartQuestionaire(id)
            self.FilloutQuestionaire()
            surveyCompleteVerifier = ''
            arrangeComplete = True
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)
        
        #act
        if(arrangeComplete):
            try:
                sleep(5)
                search = self.driver.WaitTillLoad('//*[@id="root"]/div[1]/div/div/div', SearchType.XPATH)
                surveyCompleteVerifier = search.text
            except Exception as e:
                self.test.ActFailure(e, testTag)
        
            #assert
            self.test.Equal(surveyCompleteVerifier, 'The full survey is now successfully complete.', testTag)
        
        #cleanup
        self.LogoutRoutine()
        self.driver.CloseDriver()
        self.RemoveConversation(id)

    def Test_10(self):
        #init
        testTag = 'Test_10'
        arrangeComplete = False
        
        #arrange
        try:
            self.driver.InitDriver()
            self.LoginRoutine()
            sleep(5)
            self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/conversations/new')
            self.FilloutNewConversation()
            url = self.driver.GetUrl()
            id = re.search(r'[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}', url).group(0)
            self.StartQuestionaire(id)
            self.FilloutQuestionaire()
            search = self.driver.GetElementsGroup('category-form-field__title', SearchType.CLASS)
            successVerifier = False
            arrangeComplete = True
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)
        
        #act
        if(arrangeComplete):
            try:
                for title in search:
                    if(title.text == 'Change' or title.text == 'Relationships' or title.text == 'Demands' or title.text == 'Role' or title.text == 'Peer Support' or title.text == 'Management Support' or title.text == 'Control'):
                        successVerifier = True
                    else:
                        successVerifier = False
                        break
            except Exception as e:
                self.test.ActFailure(e, testTag)

            #assert
            self.test.IsTrue(successVerifier, testTag)
            
        #cleanup
        self.LogoutRoutine()
        self.driver.CloseDriver()
        self.RemoveConversation(id)

    def Test_11(self):
        #init
        testTag = 'Test_11'
        arrangeComplete = False
        
        #arrange
        try:
            self.driver.InitDriver()
            self.LoginRoutine()
            sleep(5)
            self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/conversations/new')
            self.FilloutNewConversation()
            url = self.driver.GetUrl()
            id = re.search(r'[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}', url).group(0)
            self.StartQuestionaire(id)
            self.FilloutQuestionaire()
            search = self.driver.WaitTillLoad('page-form-button--complete', SearchType.ID)
            url = ''
            arrangeComplete = True
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)
        
        #act
        if(arrangeComplete):
            try:
                search.click()
                url = self.driver.GetUrl()
            except Exception as e:
                self.test.ActFailure(e, testTag)
   
            #assert
            self.test.Equal(url, 'https://futureworkdesign-dev.azurewebsites.net/conversations/' + id + '/confirmations/new', testTag)
             
        #cleanup
        self.LogoutRoutine()
        self.driver.CloseDriver()
        self.RemoveConversation(id)

    def Test_12(self):
        #init
        testTag = 'Test_12'
        arrangeComplete = False
        
        #arrange
        try:
            self.driver.InitDriver()
            self.LoginRoutine()
            sleep(5)
            self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/conversations/new')
            self.FilloutNewConversation()
            url = self.driver.GetUrl()
            id = re.search(r'[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}', url).group(0)
            self.StartQuestionaire(id)
            self.FilloutQuestionaire()
            search = self.driver.WaitTillLoad('page-form-button--complete', SearchType.ID)
            search.click()
            successVerifier = False
            arrangeComplete = True
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)
        
        #act
        if(arrangeComplete):
            try:
                search = self.driver.GetElementsGroup('category-form-field__title', SearchType.CLASS)
                for title in search:
                    if(title.text == 'Change' or title.text == 'Relationships' or title.text == 'Demands'):
                        successVerifier = True
                    else:
                        successVerifier = False
                        break
            except Exception as e:
                self.test.ActFailure(e, testTag)
                
            #assert
            self.test.IsTrue(successVerifier, testTag)
            
        #cleanup
        self.LogoutRoutine()
        self.driver.CloseDriver()
        self.RemoveConversation(id)

    def Test_13(self):
        #init
        testTag = 'Test_13'
        arrangeComplete = False
        
        #arrange
        try:
            self.driver.InitDriver()
            self.LoginRoutine()
            sleep(5)
            self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/conversations/new')
            self.FilloutNewConversation()
            url = self.driver.GetUrl()
            id = re.search(r'[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}', url).group(0)
            self.StartQuestionaire(id)
            self.FilloutQuestionaire()
            search = self.driver.WaitTillLoad('page-form-button--complete', SearchType.ID)
            search.click()
            successVerifier = ''
            arrangeComplete = True
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)
        
        #act
        if(arrangeComplete):
            try:
                search = self.driver.WaitTillLoad('page-form-button--submit', SearchType.ID)
                search.click()
                sleep(5)
                
                search = self.driver.WaitTillLoad('//*[@id="root"]/div[1]/div/div/div', SearchType.XPATH)
                sleep(5)
                successVerifier = search.text
                sleep(5)
            except Exception as e:
                self.test.ActFailure(e, testTag)
                
            #assert
            self.test.Equal(successVerifier, 'Thank you. Your chosen topics have now been saved.', testTag)
        
        #cleanup
        self.LogoutRoutine()
        self.driver.CloseDriver()
        self.RemoveConversation(id)

    def Test_14(self):
        #init
        testTag = 'Test_14'
        arrangeComplete = False
        
        #arrange
        try:
            self.driver.InitDriver()
            self.LoginRoutine()
            sleep(5)
            self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/conversations/new')
            self.FilloutNewConversation()
            url = self.driver.GetUrl()
            id = re.search(r'[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}', url).group(0)
            self.StartQuestionaire(id)
            self.FilloutQuestionaire()
            search = self.driver.WaitTillLoad('page-form-button--complete', SearchType.ID)
            search.click()
            search = self.driver.WaitTillLoad('page-form-button--submit', SearchType.ID)
            search.click()
            search = self.driver.WaitTillLoad('//*[@id="root"]/header/div/div/div/div[2]/ul/li[1]/a', SearchType.XPATH)
            search.click()
            successVerifier = None
            arrangeComplete = True
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)
        
        #act
        if(arrangeComplete):
            try:
                successVerifier = self.driver.WaitTillLoad(('cell-4-' + id), SearchType.ID)
            except Exception as e:
                self.test.ActFailure(e, testTag)
            
            #assert
            self.test.Found(successVerifier, testTag)
        
        #cleanup
        self.LogoutRoutine()
        self.driver.CloseDriver()
        self.RemoveConversation(id)

    def Test_15(self):
        #init
        testTag = 'Test_15'
        arrangeComplete = False
        
        #arrange
        try:
            self.driver.InitDriver()
            self.LoginRoutine()
            sleep(5)

            self.FilloutNewConversation(username_2)
            url = self.driver.GetUrl()
            id_1 = re.search(r'[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}', url).group(0)
            self.FilloutNewConversation(username_3)
            url = self.driver.GetUrl()
            id_2 = re.search(r'[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}', url).group(0)
            self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/conversations/')
            search = self.driver.WaitTillLoad('//*[@id="root"]/div[1]/div/div/div/div[2]/form/div/div[1]/input', SearchType.XPATH)
            search.send_keys('Test User2')
            successVerifier = None
            arrangeComplete = True
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)
            
        #act
        if(arrangeComplete):
            try:
                successVerifier = self.driver.WaitTillLoad('//*[@id=\"cell-4-' + id_1 + '\"]/a', SearchType.XPATH)
            except Exception as e:
                self.test.ActFailure(e, testTag)
        
            #assert
            self.test.Found(successVerifier, testTag)
        
        #cleanup
        self.LogoutRoutine
        self.driver.CloseDriver()
        self.RemoveConversation(id_1)
        self.RemoveConversation(id_2)
        
    def Test_16(self):
        #init
        testTag = 'Test_16'
        arrangeComplete = False
        
        #arrange
        try:
            self.driver.InitDriver()
            self.LoginRoutine()
            sleep(5)
            self.driver.GoToPage('https://futureworkdesign-dev.azurewebsites.net/conversations/new')
            self.FilloutNewConversation()
            url = self.driver.GetUrl()
            id = re.search(r'[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}', url).group(0)
            self.StartQuestionaire(id)
            self.FilloutQuestionaire()
            success = False
            arrangeComplete = True
        except Exception as e:
            self.test.ArrangeFailure(e, testTag)
        
        #act
        if(arrangeComplete):
            try:
                sleep(5)
                search = self.driver.WaitTillLoad('page-function-button--remove-4af58c57-cbe4-499e-99ec-fb33c45c1b98', SearchType.ID)
                search.click()
                sleep(1)
                search = self.driver.WaitTillLoad('page-function-button--remove-7185abba-d609-4071-b6b9-6e199c475e38', SearchType.ID)
                search.click()
                sleep(1)
                search = self.driver.WaitTillLoad('page-function-button--remove-8d0b0089-2cd2-4c4f-97ff-588710cba91d', SearchType.ID)
                search.click()
                sleep(1)
                search = self.driver.WaitTillLoad('page-function-button--add-4af58c57-cbe4-499e-99ec-fb33c45c1b98', SearchType.ID)
                search.click()
                sleep(1)
                search = self.driver.WaitTillLoad('page-function-button--add-7185abba-d609-4071-b6b9-6e199c475e38', SearchType.ID)
                search.click()
                sleep(1)
                search = self.driver.WaitTillLoad('page-function-button--add-8d0b0089-2cd2-4c4f-97ff-588710cba91d', SearchType.ID)
                search.click()
                sleep(1)
                search = self.driver.WaitTillLoad('page-form-button--submit', SearchType.ID)
                search.click()
                sleep(1)
                search = self.driver.WaitTillLoad('page-form-button--complete', SearchType.ID)
                search.click()
                sleep(1)
                search = self.driver.WaitTillLoad('page-form-button--submit', SearchType.ID)
                search.click()
                success = True
            except Exception as e:
                self.test.ActFailure(e, testTag)
        
            #assert
            if(success):
                self.test.Pass(testTag)
            else:
                self.test.Fail(testTag)
            
        #cleanup
        self.LogoutRoutine()
        self.driver.CloseDriver()
        self.RemoveConversation(id)
        
    