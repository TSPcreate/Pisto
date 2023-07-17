import matplotlib.pyplot as plt
import numpy as np
print("welcome to plot the histogram all we will need is 3 different values in order to start")
num1=int(input("enter the location"))
num2=int(input("enter the scale"))
num3=int(input("enter the size"))
yvalue=str(input("Enter your y axis"))
xaxis=str(input("Enter your x axis"))
x=np.random.normal(num1, num2, num3)
plt.xlabel(xaxis)
plt.ylabel(yvalue)
plt.hist(x)
plt.show()