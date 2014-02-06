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
> execfile("RUtilities.py")
> execfile("factor.py")
> x = sample(letters[0:4], 20, True)
> x
array(['c', 'c', 'b', 'd', 'd', 'c', 'd', 'c', 'c', 'c', 'd', 'a', 'd',
       'b', 'a', 'c', 'c', 'c', 'd', 'd'], 
      dtype='|S1')

> y = factor(x)
> y
c c b d d c d c c c d a d b a c c c d d
Levels: a  b  c  d

> y.__class__
<class '__main__.factor'>

> y[0:3] = ["a", "b", "c"]
> y
a b c d d c d c c c d a d b a c c c d d
Levels: a  b  c  d
```
