import sys

while(True):
    first_name=input('Enter the firstname:').replace(' ','')
    last_name=input('Enter the lastname:').replace(' ','')

    if not (first_name.isalpha() and  last_name.isalpha()):
        print('Invalid, the firstname and lastname must contain only the alphabets')
        break

    if  len(first_name)<5:
        print('Invalid, first name must have atleast 5 alphabets')
        sys.exit()

    if  len(last_name)<1:
        print('Invalid, lastname must have atleast one alphabet')
        sys.exit()
    
    if  first_name.lower().startswith('z') or last_name.lower().startswith('z'):
        print('Invalid, firstname and lastname must not start with Z')
        sys.exit()

    else:
        print('Valid First name and Last name')