import pandas as pd

#load and process data into a global structure
titanic = pd.read_csv("https://raw.githubusercontent.com/BelmontTechnology/pebble-tutorial/main/data/titanic.csv")

def mean(field="Age"):
    return float(titanic[field].mean())

def median(field="Age"):
    return float(titanic[field].median())

def oldest():
    return titanic.sort_values(by="Age",ascending=False).head(10)