import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #in case needed

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')


loansData['FICO.Range'] = map(lambda x: int(x[0:3]), loansData['FICO.Range'])
loansData['Interest.Rate'] = map(lambda x: float(x[0:-1]), loansData['Interest.Rate'])
loansData['Loan.Length'] = map(lambda x: int(x[0:-7]), loansData['Loan.Length'])
loansData['Debt.To.Income.Ratio'] = map(lambda x: float(x[0:-1]), loansData['Debt.To.Income.Ratio'])

loansData.to_csv('loansData_clean.csv', header=True, index=False)
#plt.figure()
#p = loansData['FICO.Score'].hist()
#plt.show()

#Plotting Histograms instead of the meaningless plot of the variables plotted against themselves
#a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

#3 variable linear regression
#independent variable
y = np.matrix(intrate).transpose()

#Dependent variables
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print f.summary()