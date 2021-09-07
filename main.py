#Simple program to generate a password
import random

#Function to transform a list to string format
def listToString(options):

    str1 = ""
    for element in options:
        str1 += element
    return  str1

#Password options and picking lenght
options = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
           't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',
           'Z','!','#','$','%','&','/','(',')']

password = random.sample(options,10)
print('Password: ',listToString(password))