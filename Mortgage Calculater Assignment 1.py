#Author: Zuriahn Yun
#Date: January 27th 2023
#Mortgage Calculator

import sys
if len(sys.argv) > 1:
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
    print(sys.argv[3])
else:
#Asking for inputs for each Variable for the equation
    P = int(input("Home price(P):"))
    D = int(input("Down payment amount (D):"))
    N = int(input("Loan term in months (N):"))
    Yearlyrate = float(input("Yearly interest rate:"))

#Converting the yearly interest into a Percentage
r = Yearlyrate *0.01 / 12

#Equation to get the Monthly Payment Amount
monthly1 = P - D
monthly2 = r * (1 + r) **N
monthly3 = (1 + r) ** N - 1
monthlyfinal = monthly1 * (monthly2 / monthly3)
print("Monthly payment amount:", monthlyfinal)