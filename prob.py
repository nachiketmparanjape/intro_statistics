import matplotlib.pyplot as plt
import scipy.stats as stats

data = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

#Box Plot
plt.figure()
plt.boxplot(data)
plt.title("Box Plot")
plt.savefig("Box_Plot")

#Histogram
plt.figure()
plt.hist(data) #default: histtype='bar'
plt.title("Histogram")
plt.savefig("Histogram")

#QQplot
plt.figure()
stats.probplot(data,plot=plt) #default: dist = 'hist'
plt.title("QQ Plot")
plt.savefig("QQ Plot")