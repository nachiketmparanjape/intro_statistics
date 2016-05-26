import pandas as pd
import matplotlib.pyplot as plt
import scipy
import collections


def main():
    #Loading the data    
    loansData = pd.realoansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
    loansData.dropna(inplace=True)    
    freq = collections.Counter(loansData['Open.CREDIT.Lines'])
    
    #Histogram
    plt.figure()
    plt.bar(freq.keys(),freq.values(),width=1)
    plt.show()
    
    #Chisquare test
    chi, p = scipy.stats.chisquare(freq.values())
    print ("p   = " + str(p) + "\n" + "chi = " + str(round(chi,2)))
    
main()