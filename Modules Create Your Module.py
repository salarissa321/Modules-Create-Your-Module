


#--------------------------------------------------
#---------- Modules => Create Your Module-------
#---------------------------------------------------


import sys
print(sys.path)
# # ['c:\\Users\\faten2\\OneDrive\\Desktop\\soso', 'C:\\Users\\faten2\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip', 'C:\\Users\\faten2\\AppData\\Local\\Programs\\Python\\Python311\\DLLs', 'C:\\Users\\faten2\\AppData\\Local\\Programs\\Python\\Python311\\Lib', 'C:\\Users\\faten2\\AppData\\Local\\Programs\\Python\\Python311', 'C:\\Users\\faten2\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages']

print("+" * 50) # ++++++++++++++++++++++++++++++++++++++++++++++++++

import Salar

print(dir(Salar)) # 'sayHowAreYou', 'say_hello'

Salar.say_hello("Salar") # Hello Salar
Salar.say_hello("Issa") # Hello Issa
Salar.say_hello("Issa") # Hello Issa


Salar.sayHowAreYou("Salar") # How are You Salar ?
Salar.sayHowAreYou("Issa") # How are You Issa ?
Salar.sayHowAreYou("Issa") # How are You Issa ?

print("+" * 50) # ++++++++++++++++++++++++++++++++++++++++++++++++++

# Alias Modules

import Salar as ee

ee.say_hello("Salar") # Hello Salar
ee.say_hello("Issa") # Hello Issa
ee.say_hello("Issa") # Hello Issa


ee.sayHowAreYou("Salar") # How are You Salar ?
ee.sayHowAreYou("Issa") # How are You Issa ?
ee.sayHowAreYou("Issa") # How are You Issa ?

print("+" * 50) # ++++++++++++++++++++++++++++++++++++++++++++++++++

from Salar import say_hello

say_hello("Salar") # Hello Salar

# Alias Function

from Salar import say_hello as ss

ss("Salar") # Hello Salar


