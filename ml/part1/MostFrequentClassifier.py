import numpy as np
from scipy.stats import mode
from sklearn.base import ClassifierMixin


class MostFrequentClassifier(ClassifierMixin):
    # Predicts the rounded (just in case) median of y_train
    def fit(self, X=None, y=None):
        """
        Parameters
        ----------
        X : array like, shape = (n_samples, n_features)
        Training data features
        y : array like, shape = (_samples,)
        Training data targets
        """
        self.mostFrequent = mode(y)[0]

    def predict(self, X=None):
        """
        Parameters
        ----------
        X : array like, shape = (n_samples, n_features)
        Data to predict
        """
        return self.mostFrequent * np.ones((X.shape[0],))