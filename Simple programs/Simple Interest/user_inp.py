def simple_interest(p, r, t):
    print("Principle is :", p)
    print("Rate is :", r)
    print("time is :", t)
    
    si = (p*r*t)/100
    print("Simple interest is :", si)
    return si

p = int(input("Enter the principle amount :"))
r = int(input("Enter the Rate of int amount :"))
t = int(input("Enter the Time :"))
simple_interest(p, r, t)