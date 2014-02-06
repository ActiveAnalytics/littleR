# -*- coding: utf-8 -*-

import numpy as np

# Function to find if an object is a string
def isstring(x):
    '''
        Function to test whether the argument input is a string
        
        Parameters
        ----------
        x: Any object
        
        Returns
        -------
        Boolean for whether the argument is a string
        
        
        Examples
        --------
        x = 'apple'\n
        IsString(x)\n
    '''
    return x.__getattribute__.__objclass__ == str

# Function to find if the contents of an array vector is string
def ischar(x):
    '''
        Function to test whether the argument is a str or an array vector
        
        Parameters
        ----------
        x: a numpy array
        
        Returns
        -------
        Boolean for whether the argument is a string or vector of strings
        
        Examples
        --------
        ischar(1) # False
        ischar('sam') # True
        ischar(array(['ted', 'is', 'totally', 'rad'])) # True
        ischar(np.array([1,2,3,4])) # False
    '''
    if not isIter(x):
        return x.__getattribute__.__objclass__ == str
    return x.dtype.char == 'S'


# Find out if an object is iterable
def isIter(x):
    '''
    Description
    -----------
    This function tests whether an item x is iterable

    Parameters
    ----------
    x: The item to test for iterability
    
    Returns
    -------
    Boolean for whether x is iterable or not
    
    Examples
    --------
    isIter([1,2,3,4,5,6]) # True\n
    isIter(1) # False
    '''
    try:
        iter(x)
    except TypeError:
        return False
    return True

# 
def __match(x, arr):
    '''
        Description
        -----------
        This function matches an individual item x in a vector vec.
        It returns the index if the first occurence of x or NAN if
        x is not contained in the vector. It is designed as a sub-function
        of the match() funtion
        
        Parameters
        ----------
        x: The item to be searched for\n
        arr: The vector within which the item will be searched
        
        Returns
        -------
        An integer index for the location of the item in the vector
    '''
    for i in range(arr.__len__()):
        if x == arr[i]:
            return i
    return np.nan

def match(vec1, vec2):
    '''
    Description
    -----------
    Designed to be similar to R's match() function
    
    Parameters
    ----------
    vec1: an array vector to be matched\n
    vec2: an array vector to be matched against]
    
    Returns
    -------
    This function returns indexes in vec2 that match the indexes in vec1
    
    Examples
    --------
    match(['1', '4'], ['4', '6', '3', '1', '34', '2'])\n
    match(['3', 3], range(10)) # produces a different result from in R
    '''
    if isstring(vec1):
        return __match(vec1, vec2)
    if isIter(vec1):
        out = lapply(vec1, __match, arr = vec2)
    else: return __match(vec1, vec2)
    # Return object because it is a flexible type - list-like but with 
    #      array advantages
    return np.array(out, dtype = object)



# The sample function
def sample(x, size = 1, replace = True, prob = None):
    '''
    R-like sample function, stands in for sample and sample.int it is a
    wrapper for the numpy function np.random.choice()
    
    Parameters
    ----------
    
    x: the object you wish to sample from, can be a list, 1-D array, or an
        integer if it is an integer then samples with be taken between zero and 
        that number\n
    size: The size of the sample that should be returned\n
    replace: Whether sampling should take place with or without replacement\n
    prob: a list or array giving the probabilities associated with each entry
        in x
    
    Returns
    -------
    
    samples: 1-D ndarray, shape (size,). The generated random sample
    
    Examples
    --------
    
    sample(5, 10)\n
    sample(['a', 'b', 'c', 'd', 'e'], 10)\n
    '''
    return np.random.choice(a = x, size = size, replace = replace, p = prob)

# The lapply function
def  lapply(_list, fun, **kwargs):
    """
    lapply() and R-like function
    
    lapply() function is an R-like lapply() to process each item
    in the list _list() using function specified by fun.
    
    Parameters
    ----------
    
    _list: This is a list object of items to be processed\n
    fun: This is the function that processes each time in the list\n
    **kwargs: These names arguments are passed to fun\n
    
    Returns
    -------
    
    Returns a list of processed items, each for the corresponding
            item in the input _list
    """
    return [fun(item, **kwargs) for item in _list]


def  vapply(vec, fun, **kwargs):
    """
    vapply() and R-like function
    
    vapply() function is an R-like vapply() to process each item
    in the vector vec using function specified by fun.
    
    Parameters
    ----------
    
    vec: This is an nump array vector object of items to be processed\n
    fun: This is the function that processes each time in the vector\n
    **kwargs: These names arguments are passed to fun\n
    
    Returns
    -------
    
    Returns an numpy array vector of processed items, each for the corresponding
            item in the input vector
    """
    if isstring(vec) or not isIter(vec):
        vec = np.array([vec])
    #nabool = np.isnan(vec)
    out = np.array([fun(item, **kwargs) for item in vec])
    #out[nabool] = np.nan
    #if out.__len__() > 1:
    #    return out
    return out


# The identity function
def I(x):
    ''' A skeleton for the 'As-Is' function in R '''
    return x


def _str(x):
    if x.__class__.__name__ == 'float':
        if np.isnan(x):
            return np.nan
        else:
            return str(x)
    return str(x)
# converts an array vector to string
def aschar(x):
    '''
    Description
    -----------
    
    aschar is similar to R's as.character() function, it will coerce an array\n
    vector to a string array if a non iterable is submitted, it will be 
    converted to string and returned
    
    Parameters
    ----------
    x: a numpy array
    
    Returns
    -------
    Either a string array or a single string object
    '''
    if not isstring(x) and isIter(x):
        return np.array(lapply(x, _str), dtype = object)
    return np.array([_str(x)], dtype = object)


# This is the sub function for strsplit
def __strsplit(x, split):
    # .split does not work for split = '' so treat it differently
    if split != '':
        splt = x.split(split)
        if not isstring(splt):
            return np.array(splt)
        else:
            return splt
    else:
        return np.array([ind for ind in x])


# Function to split strings
def strsplit(x, split):
    '''
    R-like strsplit function to split strings
    
    Parameters
    ----------
    
    x:      the string that needs to be split\n
    split:  the character string by which the string should be split\n
    
    Returns
    -------
    
    If a single string is submitted, it returns a list of split strings or else
    if a list of strings are submitted, it returns a list of lists, 
    where each sub-list contain a list of split strings for the given submitted
    string.
    
    Examples
    --------
    
    '''
    
    if not isstring(x):
        return vapply(x, __strsplit, split = split)
    else:
        return __strsplit(x = x, split = split)


def toupper(x):
    '''
        R-like toupper function to convert string or list of strings to upper
        case.
        
        Parameters
        ----------
        x: the string to be converted
        
        Returns
        -------
        The string converted to upper case
        
        Examples
        --------
        
        toupper('python is the future')\n
        toupper(['python', 'is', 'the', 'future'])
    '''
    if not isstring(x):
        return lapply(x, lambda y: y.upper())
    else:
        return x.upper()


def tolower(x):
    '''
        R-like tolower function to convert string or list of strings to lower
        case.
        
        Parameters
        ----------
        x: the string to be converted
        
        Returns
        -------
        The string converted to lower case
        
        Examples
        --------
        
        tolower('PYTHON IS THE FUTURE')\n
        tolower(['PYTHON', 'IS', 'THE', 'FUTURE'])
    '''
    if not isstring(x):
        return lapply(x, lambda y: y.lower())
    else:
        return x.lower()

# Function to get unique values from a list
def unique(x):
    out = []
    for i in x:
        if i not in out:
            out.append(i)
    return out

def naomit(x):
    out = []
    for i in x:
        if i.__class__.__name__ == 'float':
            if not np.isnan(i):
                out.append(i)
        else:
            out.append(i)
    return out

# Some convenient constants
letters = 'qwertyuiopasdfghjklzxcvbnm'
letters = strsplit(letters, '')
letters.sort()

LETTERS = np.array(toupper(letters))


