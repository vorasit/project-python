import numpy
from scipy import stats
import matplotlib.pyplot as plt
"""
speed = [99,86,87,88,86,103,87,94,78,77,85,86]

#x = numpy.mean(speed)
#x = numpy.median(speed)
#x = numpy.std(speed)
x = stats.mode(speed)


print(x)

"""


"""
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)
print(x)
"""

"""
x = numpy.random.uniform(0.0, 5.0, 250)
plt.hist(x, 5)
plt.show()
"""

"""
x = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()
"""

"""
x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()
"""

"""
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
"""


x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()