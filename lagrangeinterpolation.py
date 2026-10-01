def lagrange_interpolation(x,y,value):
    n=len(x)
    result=0
    for i in range(n):
        term=y[i]
        for j in range(n):
            if i!=j:
                term=term*(value-x[j])/(x[i]-x[j]) 
        result=result+term
    return result 

x=[1,2,3]
y=[1,4,9]
value=4
result=lagrange_interpolation(x,y,value)
print("Interpolated Result: ",result)