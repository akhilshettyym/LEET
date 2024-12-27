def Compound_intrest(principal, rate, time):
    Amount = principal * (pow((1 + rate/100), time))
    CI = Amount - principal
    print("Compound Interest :", CI)
Compound_intrest(10000, 10.25, 5)