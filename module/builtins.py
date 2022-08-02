"""
Demonstrate some classes that make it easy to perform standard operations.
"""
import numpy as np


class Dataset(object):
    """A dummy class that demonstrates proper documentation.
    Implements something like the pytorch Dataset class.
    """
    def __init__(self, X, y) -> None:
        """_summary_

        Args:
            X (_type_): _description_
            y (_type_): _description_
        """
        pass


def train_test_split(X, y, train_fraction=0.8):
    """Implements a split between train and test values.
    Note: always shuffles the data.

    Args:
        X (array-like): input values
        y (array-like): target labels
        train_fraction (float, optional): fraction of values to assign to training set. Defaults to 0.8.

    Raises:
        ValueError: if the X and y are not the same length

    Returns:
         Xtrain (array-like): the input values assigned to the training set
         Xtest (array-like): the input values assigned to the testing set
         ytrain (array-like): the target labels assigned to the training set
         ytest (array-like): the target labels assigned to the testing set
    """

    # check that X and y data have same number of observations
    if X.shape[0] != y.shape[0]:
        raise ValueError('X and y must have the same length.')

    # compute the training indices
    n_train = int(X.shape[0] * train_fraction)
    index = np.random.choice(np.arange(X.shape[0]), n_train, replace=False)

    # set up the logical indexer
    is_train = np.zeros(X.shape[0], type=bool)
    is_train[index] = True

    # assign the values to train and test sets
    Xtrain = X[is_train]
    Xtest = X[np.logical_not(is_train)]
    
    ytrain = y[is_train]
    ytest = y[np.logical_not(is_train)]

    return Xtrain, Xtest, ytrain, ytest
