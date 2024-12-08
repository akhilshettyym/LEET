def simple_interest(p, r, t):
    print("Principle is :", p)
    print("Rate is :", r)
    print("time is :", t)
    
    si = (p*r*t)/100
    print("Simple interest is :", si)
    return si

simple_interest(8, 6, 8)