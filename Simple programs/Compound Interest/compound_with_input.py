def compound_interest(principal, rate, time):
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound Interest :", CI)
    
principal = int(input("Enter the principal amount :"))
rate = int(input("Enter the rate :"))
time = int(input("Enter the time period :"))

compound_interest(principal, rate, time)