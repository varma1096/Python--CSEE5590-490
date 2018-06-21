import numpy as num
import matplotlib.pyplot as mat

a=num.array([0,1,2,3,4,5,6,7,8,9])
b=num.array([1,3,2,5,7,8,8,9,10,12])
mean_a=num.mean(a)
mean_b=num.mean(b)
x=num.sum((a-mean_a)*(b-mean_b))
y=num.sum(pow(a-mean_a,2))
slope=x/y
intercept_y=mean_b-(slope*mean_a)
print("slope: {}".format(slope))
print("Y Intercept: {}".format(intercept_y))
values=(slope*a)+intercept_y
mat.plot(a,b,values,'ro')
mat.plot(values,color="blue")
mat.xlabel("X Values")
mat.ylabel("model values")
mat.show()
