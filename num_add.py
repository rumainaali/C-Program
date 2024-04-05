'''
Find sum of odd digits and sum of even digits in a number. 
For example, if the input is 58974, 
sum of odd digits is 5+9+7=21 and sum of even digits is 8+4=12
'''

num=input('Enter the number:').replace('-','')
sum_odd=0
sum_even=0

if not num.isdigit():
  print('Invalid, must consist of numbers only')
  
else:
    n=int(num)
    while n>0:
      rem=n%10
    
      if rem%2==0:
        sum_even+=rem
      else:
        sum_odd+=rem
      n=n//10
    
    print('Sum of the odd:',sum_odd)
    print('Sum of the even:',sum_even)