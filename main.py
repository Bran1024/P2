a = input("What was your total bill ? ")
b = input("What percentage tip would you like to give ? 10, 12, or 15 ? ")
c = input("How many people to split the bill ? ")
d = float((float(a)*int(b)/100))
e = round(float(d)/int(c),2)
print(f"Each Person needs to pay {e} rupees" )