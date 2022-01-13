# Pebbles platform tutorial and examples

## Introduction

Belmont Pebbles allow you to automatically deploy your
Python functions as web services. You tell your
platform where your code is, and the Pebbles platform
will create web service URLs that will run the Python
functions you've defined.

## Tutorial preparation

You can use our example code for the first few tutorial
exercises, though you may wish to fork a copy of it
into your own repository so you can experiment with
modifying the code or running it locally and seeing
what happens.

## Hello world

Let's deploy a simple script with a simple function.
Take a look at the code of `ex01_hello.py`. It contains a
function `hello` that will be deployed as a web
service.
```
def hello(name=None):
    if name is None:
        return "Hello world!"
    else:
        return f"Hello, {name}!"
```

(Optional) This is just an ordinary Python function. If
you'd like the try out the function on its own, without
deploying it to the plaform, the script contains some
body code that will call the function if it's invoked
from the command line. You can Clone or copy the script
to your Python execution environment and run it with:
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
branch, and point at the path `ex01_hello.py`. This is
the script and the function we'll deploy as a service.

Now let's try running it in the UI.

...

And let's try calling the endpoint from our browser.

...

## Multiple functions and external modules

We can also deploy multiple functions from a single
script. When a script contains multiple function
definitions, the platform creates web services
("endpoints") for each top-level function whose name
does not begin with an underscore (`_`) character.

The Pebbles platform will also automatically install and use most external packages from PyPI (the Python Package Index, the source for `pip` packages). 

Create a pebble from the `ex02_summarystats.py` file in
the tutorial repository's `main` branch and see that
you can call URLs from each of the corresponding
functions.

This code uses the `pandas` data analysis library to
load a dataset containing information about passengers
on the Titanic. (Data originally sourced from the [pandas tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html).) It then provides functions to return
the mean, median and percentile of numeric fields using
functions from `pandas`. You can test the mean, median,
and percentile functions by calling them on the `Age`
field (default) or on the `Fare` field.

## Deploying and running a model

Let's do something slightly more complex. We'll load a
statistical model, and use that model to predict values.

Take a look at the `ex03_predict.py` script, and create a
Pebble from it to deploy the `predict` function. 

In this case, we're loading in a database of historical information about CPU technology (from the [NumPy Moore's Law tutorial](https://numpy.org/numpy-tutorials/content/mooreslaw-tutorial.html).)
We'll use this to build a model to predict the number of transistors that a new CPU might have this year. 
We'll create an Ordinary Least Squares linear regression model against the log of this data using the `statsmodels` library, and then call it to backtest and predict.

In this example, we're loading the data and building the model in our script, but if our data and model were more complex, we could instead load the model directly from external persistent storage.

It should be noted that when you call the `predict_y` function, it does _not_ re-load the data and re-compute the model every time, but rather simply calls the already-built model in the service, as long as the service instance remains running.

## Secure database access

Pebbles web services run in the public cloud, so any
data they need to access must be available to the
public internet. But Pebbles may nevertheless
authenticate in order to access secured resources.