# -*- coding: utf-8 -*-

# Implementation of factor class based on lists

#   The purpose of the level object is to create a class that allows selection 
# on unique items that is able to handle when an item is selected and isn't in
# the list
class level(np.ndarray):
    '''
        Description
        -----------\n
        The purpose of the levels class is to create a class that is used to
        represent levels in the subsequent factor class. The reason that this
        needs to be done is to allow adequate support for nan assignment,
        coersion and selection effects. It is a subclass of ndarray
        
        Parameters
        ----------\n
        x: This is the list of items that should be converted into levels of a factor.
        
        Returns
        -------\n
        Returns a level class object
        
        Examples
        --------\n
        xx = level([1,2,3,4,5,6,3,4,2,4])\n
        xx[np.nan]\n
        xx[[1,3,np.nan]]\n
        yy = level(['1', '2', np.nan, 'riser'])
    '''
    def __new__(cls, x):
        # converting x to an array
        if isstring(x):
            x = [x]
        else:
            if x.__class__.__name__ == 'ndarray':
                x = x.tolist()
        # Removing the nan values
        x = naomit(x)
        # Getting the unique values
        x = np.unique(x)
        # Creating the object
        obj = np.ndarray.__new__(cls, shape = (x.__len__(),), dtype = object)
        obj[...] = aschar(x)
        return obj
    def __getitem__(self, key):
        out = []
        if key.__class__.__name__ == 'ndarray':
            if key.dtype.name != 'bool':
                for i in key:
                    if i.__class__.__name__ == 'float':
                        if not np.isnan(i):
                            out.append(super(level, self).__getitem__(i))
                        else:
                            out.append(np.nan)
                    else:
                        out.append(super(level, self).__getitem__(i))
        elif key.__class__.__name__ == 'list':
            for i in key:
                if i.__class__.__name__ == 'float':
                    if not np.isnan(i):
                        out.append(super(level, self).__getitem__(i))
                    else:
                        out.append(np.nan)
                else:
                    out.append(super(level, self).__getitem__(i))
        elif np.isnan(key):
            return np.array(np.nan, dtype = object)
        else:
            return super(level, self).__getitem__(key)
        out = np.array(out, dtype = object)
        return out
    def __repr__(self):
        strRep = 'Levels: ' + '  '.join(self)
        return strRep


# Now create the factor class
class factor(object):
    '''
    Description
    -----------\n
    This is the factor class designed to closely emulate R's factor class
    
    Parameters
    ----------\n
    x: array vector to be converted into a factor\n
    levels: character vector denoting the levels that should be used for the
            factor levels of x
    
    Returns
    -------\n
    Returns an R-like factor class object
    
    Examples
    --------\n
    # Sampling items to be used to create the factor\n
    facts = sample(LETTERS[0:4], 20)\n
    # Creating the factor\n
    xx = factor(x = facts)\n
    xx\n
    # The levels\n
    xx.levels\n
    xx.levels = LETTERS[4:9]\n
    # Subsetting\n
    xx[5]\n
    xx[4:7]\n
    # Setting items in the factor array\n
    xx[0] = 'F'\n
    xx[0:2] = np.array(['I', 'G'])\n
    # nan cohersion\n
    xx[5] = 'V'\n
    xx\n
    # nan assignment\n
    xx[5] = np.nan\n
    xx\n
    # multiple nan assignment\n
    xx[5:7] = [np.nan, np.nan]\n
    # implied multiple nan assignment\n
    xx[5:9] = np.nan\n
    # isnan method\n
    xx.isnan()\n
    # coercing character vector to a factor\n
    asfactor(sample(LETTERS[0:4], 20))\n
    '''
    def __init__(self, x, levels = None):
        if levels == None:
            levels = level(x)
        else:
            levels = level(levels)
        x = aschar(x)
        x = match(x, levels)
        self.f = x
        self._levels = levels
    def nlevels(self):
        return self._levels.__len__()
    @property
    def levels(self):
        return self._levels
    @levels.setter
    def levels(self, lvls):
        lvls = level(lvls)
        if len(self._levels) <= len(lvls):
            self._levels = lvls
        else:
            raise AttributeError('You are trying to replace levels with \n\
            an array that is shorter than the current number of levels')
    def __repr__(self):
        strRep = self._levels[self.f]
        strRep = vapply(strRep, str)
        maxLen = np.max(vapply(strRep, len))
        spacing = ''.join(np.repeat(' ', maxLen))
        lvlOut = self._levels.__repr__()
        return spacing.join(strRep) + '\n' + lvlOut
    def __str__(self):
        return self._levels[self.f].__str__()
    def asvector(self):
        return self._levels[self.f]
    def __getitem__(self, key):
        return factor(np.array(self._levels[self.f[key]]), levels = self._levels)
    def __setitem__(self, key, value):
        value = aschar(value)
        if value.__len__() == 1:
            value = value[0]
        self.f[key] = match(value, self._levels)
    def __len__(self):
        return self.f.__len__()
    def isnan(self):
        return np.isnan(np.array(self.f, dtype = 'float'))


# To determing whether an object is a factor
def isfactor(x):
    return x.__class__.__name__ == 'factor'

# Convenient R-like as.factor() function
def asfactor(x):
    if isfactor(x):
        return x
    return factor(x)

