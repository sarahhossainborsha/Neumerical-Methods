def f(x):
    return x**3-4*x-9
def df(x):
    return 3*x**2-4

def np(x,tolerance=1e-6,max_it=100):
    for i in range(max_it):
        if df(x)==0:
            print("derivative zero")
            return None

        x_new=x-f(x)/df(x)
        
        if abs(x_new-x)<tolerance:
            print("found at:",i+1)
            return x_new
        x=x_new

    print("max iteration reached")
    return x

root=np(2.0)
print("root",root)