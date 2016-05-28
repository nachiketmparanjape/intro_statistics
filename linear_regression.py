import pandas as pd
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData['FICO.Score'] = map(lambda x: int(x[0:3]), loansData['FICO.Range'])

plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()

#Plotting Histograms instead of the meaningless plot of the variables plotted against themselves
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')