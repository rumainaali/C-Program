'''  Date:3/4/2024
Right Angled Triangle Pyramid Pattern
'''
no_of_rows=int(input('Enter the number of rows:'))
for rows in range(1,no_of_rows+1):
    for cols in range(1,rows+1):
        print('*',end='')
    print('')
for i in range(5,0,-1):
    for j in range(1,i+1):
        print('*',end='')
    print('')