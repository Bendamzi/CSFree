money = input("Money invested: ")
interest_rate = input("Interest Rate: ")

money = float(money)

interest_rate = float(interest_rate) * .01
n = int(input("Duration: "))
for i in range (n):
    money = money + (money * interest_rate)
    
print("Investment after {} months : {:.2f}".format(n, money))