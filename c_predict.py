import sys
import math
import pandas as pd
import statsmodels.api as sm

# load data file and select and clean data
data = pd.read_csv('https://raw.githubusercontent.com/gkanapathy/pebble-tutorial/main/data/transistor_data.csv')

x = data['Date of Introduction'].tolist()
yl = [math.log10(c) for c in data['MOS transistor count']]

# prepare and build model
x1 = sm.add_constant(x)
r = sm.OLS(yl, x1).fit()

# call model to predict
def predict_y(x):
    return pow(10,r.predict(exog=[1,x]))


if __name__ == "__main__" and len(sys.argv) > 1:
    print(predict_y(float(sys.argv[1])))
    