littleR
=======

littler is a small set of Python scripts that give some R-like features in Python and is 
intended for demonstration purposes in Active Analytics Ltd. blog www.activeanalytics.co.uk/blog

Utilities.py
------------

Contains R-like functions such as match(), sample(), lapply(), vapply(), aschar(), strsplit(), toupper(), 
tolower(), unique(), naomit(), and data items letters, and LETTERS as well as some other helper functions.


factor.py
---------

Contains R-like factor class with all the features that R's factor has


Examples
--------

```
>>> execfile("RUtilities.py")
>>> execfile("factor.py")
>>> x = sample(letters[0:4], 20, True)
>>> x
array(['c', 'c', 'b', 'd', 'd', 'c', 'd', 'c', 'c', 'c', 'd', 'a', 'd',
       'b', 'a', 'c', 'c', 'c', 'd', 'd'], 
      dtype='|S1')

>>> y = factor(x)
>>> y
c c b d d c d c c c d a d b a c c c d d
Levels: a  b  c  d

>>> y.__class__
<class '__main__.factor'>

>>> y[0:3] = ["a", "b", "c"]
> y
a b c d d c d c c c d a d b a c c c d d
Levels: a  b  c  d

# Here we create a 5 batches of 5 random normal distributed numbers each having a different mean
>> vapply(np.array(range(5)), np.random.normal, size = 5)
array([[-0.67618853, -0.3939033 ,  0.49074697, -0.65955165, -0.53552188],
       [ 1.47710633, -0.69960636,  1.08200627,  1.56646386,  2.73198602],
       [ 1.05342574,  1.76063512,  1.99736665,  1.43769847,  0.08689192],
       [ 2.46219842,  2.54457608,  2.59306678,  5.48947124,  3.94090388],
       [ 5.09717554,  3.97830888,  5.23352363,  4.47189075,  2.30385836]])
```
