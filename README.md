# Pebbles platform tutorial and examples

## Introduction

Belmont Pebbles allow you to automatically deploy your
Python functions as web services. You tell your
platform where your code is, and the Pebbles platform
will create web service URLs that will run the Python
functions you've defined.

## Tutorial preparation

You can use our example code repository
(https://github.com/BelmontTechnology/pebble-tutorial)
for these tutorial exercises, though you may wish to
fork a copy of it into your own repository so you can
experiment with modifying the code or running it
locally and seeing what happens.


## Hello world

Let's deploy and run a Python function as a web service.

Take a look at the code of `ex01_hello.py`. It contains a function `hello()`:
```python
def hello(name=None):
    if not name:
        return "Hello world!"
    else:
        return f"Hello, {name}!"
```

(Optional) This is just an ordinary Python function. If
you'd like the try out the function on its own, without
deploying it to the platform, the script contains some
body code that will call the function if it's invoked
from the command line. You can clone or copy the script
to your Python command line and run it:
```
> python ex01_hello.py
Hello world! 
```
or
```
> python ex01_hello.py Gerald
Hello, Gerald!
```
Now lets deploy and run this as a Pebble. Log in to the
Pebbles platform UI, and create a new Pebble. Point at
our base repository
(`https://github.com/BelmontTechnology/pebble-tutorial`)
or your own copy of the repository. Use the `main`
branch, select the root folder, and point at the script
`ex01_hello.py`. Once you've specified the file, the
platform will create and register a Pebble and display
it in the UI.

Now let's try running it in the Pebbles UI.

...

And let's try calling the endpoint.

...

## External modules and complex data

We can also deploy multiple functions from a single
script. When a script contains multiple function
definitions, the platform creates a web service
("endpoint") for each top-level function (except those
whose names begin with an underscore (`_`) character).

The Pebbles platform will also automatically install
and use most external packages from PyPI (the Python
Package Index, the source for `pip` packages).


...

The `ex03_summarystats.py` script uses the `pandas`
data analysis library to load a dataset containing
measurements of air quality. (Data originally sourced
from the
[pandas tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html).)
It then provides functions to return the mean and
median of numeric fields as well as the 10 highest
observations, using functions from `pandas`.
```python
import pandas as pd

#load and process data into a global structure
aq = pd.read_csv("https://raw.githubusercontent.com/BelmontTechnology/pebble-tutorial/main/data/air_quality_no2_long.csv")

def mean(city=None):
    return float( (aq if not city else aq[aq["city"]==city])["value"].mean() )

def median(city=None):
    return float( (aq if not city else aq[aq["city"]==city])["value"].median() )

def highest():
    return aq.sort_values(by="value",ascending=False).head(10)
```
Create a new Pebble from the script, and you'll be able
to test the `mean()` and `median()` functions. These
functions only return a single value. Now try running
the `highest()` function. This returns a table of data,
which the Pebbles platform UI intelligently detects and
displays.


## Deploying and running a statistical model

Let's do something slightly more complex. We'll load a
statistical model, and use that model to predict values.

Take a look at the `ex03_predict.py` script, and create a
Pebble from it to deploy the `predict` function. 

In this case, we're loading in a database of historical information about CPU technology from a public cloud (from the [NumPy Moore's Law tutorial](https://numpy.org/numpy-tutorials/content/mooreslaw-tutorial.html).)
We'll use this to build a model to predict the number of transistors that a new CPU might have this year. 
We'll create an Ordinary Least Squares linear regression model against the log of this data using the `statsmodels` library, and then call it to backtest and predict.
```python
import sys
import math
import pandas as pd
import statsmodels.api as sm

# load data file and select and clean data
data = pd.read_csv('https://belmonttutorial.blob.core.windows.net/data/transistor_data.csv')

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
```
(In this example, we're loading the data from the cloud
storage and building the model when we initialize our
script, but if the model was more time-consuming to
create, we could create it offline and then load the
model from cloud storage instead.)

This particular dataset contains information up through 2019. You can call the `predict_y` function with `2021` and see how the predicted values compare against [actual CPUs introduced in 2021](https://en.wikipedia.org/wiki/Transistor_count#Microprocessors).

...

You should note that you call the `predict_y` function, it does _not_ re-load the data and re-compute the model every time, but instead calls the `predict_y` function against the already-built model in the service, as long as the service instance remains running.
