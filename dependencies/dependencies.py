from time import sleep
import re
import json
import requests

#IF THE DATABASE IS EVER DROPPED MAKE SURE YOU RECREATE THESE BY MANUALLY ADDING THEM TO THE DATABASE

username_1 = 'testUser1@email.co'
password_1 = 'Test.User123'

username_2 = 'testUser2@email.co'
password_2 = 'Test.User456'

username_3 = 'testUser3@email.co'
password_3 = 'Test.User789'

username_admin = 'josh.admin@lampada.co'
password_admin = f'GPDSEQ@0C09Joo3gB@6tPIb0%a%u'

test_email = 'thisisfwdtester@outlook.com'
test_email_password = 'asdfkjbasdfb3324!A'