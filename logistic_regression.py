import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #in case needed

loansData = pd.read_csv('loansData_clean.csv')


def Rate_Classifier(row):
    Interest = row
    
    if Interest < 12:
        return 0
    else:
        return 1
        
def logistic_function(coeffs, loan_amt, FICO):
    return 1/(1 + np.exp(-coeffs[2] - coeffs[0]*FICO + coeffs[1]*loan_amt))
    
    
    
loansData['IR_TF'] = loansData['Interest.Rate']
loansData['IR_TF'].loc[loansData['IR_TF'] < 12] = 0
loansData['IR_TF'].loc[loansData['IR_TF'] >= 12] = 1

loansData['Intercept'] = 1

ind_vars = ['FICO.Score','Amount.Requested','Intercept']

logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])
result = logit.fit()

coeff = result.params

print logistic_function(coeff,10000,720)


def plot_to_estimate(loan_amt):
    fico_list = []
    prob_list = []
    for FICO in range(550,950):
        fico_list.append(FICO)
        prob_list.append(logistic_function(coeff,loan_amt,FICO))
    plt.plot(fico_list,prob_list)
    plt.axis([550,950,0,1])
    plt.show()
    
plot_to_estimate(10000)
    
