#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.


total_money = 0
count = 0

while total_money < 1000:
    money = int(input('Amount of money your parents gave you:'))
    if money <= 10:
        print('Money is less than or equal to Rs 10.')
        continue
    else:
        total_money += money
        count += 1
        print('Money received:', total_money)
        print('Thank you.')

    if total_money >= 1000:
        break

print("Total number of times asked:", count)
