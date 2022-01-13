import pandas as pd

#load and process data into a global structure
titanic = pd.read_csv("https://raw.githubusercontent.com/BelmontTechnology/pebble-tutorial/main/data/titanic.csv")

def mean(field="Age"):
    return titanic[field].mean()

def median(field="Age"):
    return titanic[field].median()

def percentile(field="Age", percentile=[.25, .5, .75]):
    return titanic[field].quantile(percentile)

def oldest():
    return titanic.sort_values(by="Age",ascending=False).head(10)