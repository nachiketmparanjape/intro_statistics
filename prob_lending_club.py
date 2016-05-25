import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData.dropna(inplace=True)

#Box Plot
def boxplot(data,col,name):
    plt.figure()
    data.boxplot(column=col)
    plt.title(name + " - Box Plot")
    plt.savefig(name + "_box_plot")

#Histogram
def histogram(data,col,name):
    plt.figure()
    data.hist(column=col) #default: histtype='bar'
    plt.title(name + " - Histogram")
    plt.savefig(name + "_Histogram")

#QQplot
def qqplot(data,col,name):
    plt.figure()
    stats.probplot(data[col],plot=plt) #default: dist = 'hist'
    plt.title(name + " - QQ Plot")
    plt.savefig(name + "_QQ Plot")
    
boxplot(loansData,'Amount.Requested', 'Amount_Requested')
histogram(loansData,'Amount.Requested', 'Amount_Requested')
qqplot(loansData,'Amount.Requested', 'Amount_Requested')