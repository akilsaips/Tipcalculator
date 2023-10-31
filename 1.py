#TIP CALC
print('Welcome to the tip calculator!')

q1 = float(input("What was the total bill? $"))
q2 = int(input("How much tip would you like to give? 10, 12, or 15? "))
q3 = int(input("How many people to split the bill? "))

c1 = q1 * q2/100
c2 = q1 + c1
c3 = c2/q3

print(f"Each person should pay: ${round(c3, 2)}")
