from tests import Tests
import re

if __name__ == "__main__":
        
    #Init Tests
    tests = Tests()
        
    # Run Tests
    driverFunctioning = False

    try:    
        driverFunctioning = tests.driver_test()
    except:
        print('\033[91m' + '[Driver Init Failure] Driver has failed to load/update' + '\033[0m')

    if(driverFunctioning):
        tests.Test_1()
        tests.Test_2()
        tests.Test_3()
        tests.Test_4()
        tests.Test_5()
        tests.Test_6()
        tests.Test_7()
        tests.Test_8()
        tests.Test_9()
        tests.Test_10()
        tests.Test_11()
        tests.Test_12()
        tests.Test_13()
        tests.Test_14()
        tests.Test_15()
        tests.Test_16()
        tests.MassCleanup()
        print('\033[94m' + '[info] Tests Complete' + '\033[91m')
        
        