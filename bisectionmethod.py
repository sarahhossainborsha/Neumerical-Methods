def f(x):
    return x**3-x-2
def bisection(a,b,max_it=100):
    if f(a)*f(b)>=0:
        print("invalid interval")
        return None
    c=a
    for i in range(max_it):
        c=(a+b)/2
        if f(c)==0:
            print("root found at:",i+1)
            return c
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
    print("max iteration reached!!!!!!!!")
    return c
root=bisection(1.0,2.0)
print("root is : ",root)