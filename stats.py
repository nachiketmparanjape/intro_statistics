import pandas as pd
from collections import Counter

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

def rangex(l):
	return max(l)-min(l)
def mode(l):
    data = Counter(l)
    return data.most_common(1)  # Returns the highest occurring item

data = data.split('\n')
data = [i.split(',') for i in data]
column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns = column_names)
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)
print "The range for Alcohol and Tobacco dataset is %f for Alcohol and %f for Tobacco." %(rangex(df['Alcohol']),rangex(df['Tobacco']))
print "The mean is %f for Alcohol and %f for Tobacco" %(df['Alcohol'].mean(),df['Tobacco'].mean()),
print "and the median is %f for Alcohol and %f for Tobacco." %(df['Alcohol'].median(),df['Tobacco'].median())
print "The variance is %f for Alcohol and %f for Tobacco" %(df['Alcohol'].var(),df['Tobacco'].var()),
print "and the standard deviation is %f for Alcohol and %f for Tobacco." %(df['Alcohol'].std(),df['Tobacco'].std())