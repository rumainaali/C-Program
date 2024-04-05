'''  Date:3/4/2024
Right Angled Triangle Pattern
'''

no_of_rows=int(input('Enter the number of rows:'))
for rows in range(1,no_of_rows+1):
    for cols in range(1,rows+1):
        print('*',end='')
    print('')