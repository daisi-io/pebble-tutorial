import pandas as pd

#load and process data into a global structure
aq = pd.read_csv("https://raw.githubusercontent.com/BelmontTechnology/pebble-tutorial/main/data/air_quality_no2_long.csv")

def mean(city=None):
    return float( (aq if not city else aq[aq["city"]==city])["value"].mean() )

def median(city=None):
    return float( (aq if not city else aq[aq["city"]==city])["value"].median() )

def highest():
    return aq.sort_values(by="value",ascending=False).head(10)