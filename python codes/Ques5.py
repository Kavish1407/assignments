import re
import logging
def validate(passw):
    w = re.search("[A-Z]",passw)
    x = re.search("[a-z]",passw)
    y = re.search("[0-9]",passw)
    z = re.search("[$#@]",passw)
    if(w and x and y and z and len(passw)>=6 and len(passw)<=12):
        return 'valid'
    else:
        return 'invalid'



def main():
    passw = input("Enter a password: ")
    output=validate(passw)
    print(output)
    logging.basicConfig(filename="app.log",filemode="a",format='%(asctime)s - %(message)s',level=logging.INFO)
    logging.info(passw+" "+output)
main()