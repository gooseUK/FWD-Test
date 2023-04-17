class Assertions:
    
    passes = 0
    failures = 0
    
    def __init__(self):
        pass
    
    def Pass(self, testTag):
        self.passes = self.passes + 1
        print('\033[92m' + '[pass] ' + testTag + '\033[0m')
        print('[Pass Count]: ' + str(self.passes))
        
    def Fail(self, testTag):
        self.failures = self.failures + 1
        print('\033[91m' + '[fail] ' + testTag + '\033[0m')
        print('[Fail Count]: ' + str(self.failures))
    
    def ErrorMsg(self, e, testTag):
        print('\033[93m'  + '[Test ' + testTag + ' Error]:' + '\033[0m')
        print(e)

    def Equal(self, a, b, testTag):
        if(a == b):
            self.Pass(testTag)
        else:
            self.Fail(testTag)
            
    def Found(self, a, testTag):
        if(a != None):
            self.Pass(testTag)
        else:
            self.Fail(testTag)
            
    def IsTrue(self, a, testTag):
        if(a == True):
            self.Pass(testTag)
        else:
            self.Fail(testTag)
            
    def IsFalse(self, a, testTag):
        if(a == False):
            self.Pass(testTag)
        else:
            self.Fail(testTag)
            
    def ArrangeFailure(self, e, testTag):
        print('\033[91m' + '[Arrange Failure] ' + testTag + '\033[0m')
        print(e)
    
    def ActFailure(self, e, testTag):
        print('\033[91m' + '[Act Failure] ' + testTag + '\033[0m')
        print(e)
        
    def AssertFailure(self, e, testTag):
        print('\033[91m' + '[Assert Failure] ' + testTag + '\033[0m')
        print(e)
    
    def CleanupFailure(self, e, testTag):
        print('\033[91m' + '[Cleanup Failure] ' + testTag + '\033[0m')
        print(e)