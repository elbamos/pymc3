import numpy as np

# TODO I could not locate this function used anywhere in the code base
# do we need it?
def eval_univariate(f,var, idx, point, x):
    """
    Evaluate a function as a at a specific point and only varying values at one index.

    Useful for debugging misspecified likelihoods.
    
    Parameters
    ----------

    f : function : dict -> val 
    var : variable 
    idx : index into variable 
    point : point at which to center
    x : array points at which to evaluate x
    
    """
    bij = DictElemBij(var, idx, point) 
    return map(bij.mapf(f), x)
    
def hist_covar(hist, vars):
    """Calculate the flattened covariance matrix using a sample history"""
    def flat_h(var):
        x = hist[str(var)]
        return x.reshape((x.shape[0], np.prod(x.shape[1:])))
    
    return np.cov(np.concatenate(map(flat_h, vars), 1).T)

# TODO Also could not find this function used anywhere. Are any of the 
# functions in misc necessary?
def autocorr(x):
    x = np.squeeze(x)
    import pylab
    return pylab.acorr( x - np.mean(x))
