import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

lending_df = pd.read_csv("https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/loans/loansData.csv",index_col=0)

#Clean The Data
lending_df = lending_df.dropna()
lending_df['int_rate'] = map(lambda x: float(x[0:-1]), lending_df['Interest.Rate'])
lending_df['Loan.Length'] = map(lambda x: int(x[0:-6]), lending_df['Loan.Length'])
lending_df['Debt.To.Income.Ratio'] = map(lambda x: float(x[0:-1]),lending_df['Debt.To.Income.Ratio'])
lending_df['FICO.Score'] = map(lambda x: int(x[0:3]),lending_df['FICO.Range'])
lending_df['annual_inc'] = map(lambda x: x*12, lending_df['Monthly.Income'])
lending_df['home_ownership'] = pd.Categorical(lending_df['Home.Ownership']).codes

#First fit
X = lending_df['annual_inc']
y = lending_df['int_rate']
X = sm.add_constant(X)
est1 = sm.OLS(y, X).fit()

#including home ownership in the fit
X = lending_df[['annual_inc','home_ownership']]
y = lending_df['int_rate']
X = sm.add_constant(X)
est2 = sm.OLS(y, X).fit()

print est1.summary().tables[1]
print "p values"
print est1.pvalues
print est2.summary().tables[1]
print "p values"
print est2.pvalues
