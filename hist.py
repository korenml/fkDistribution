import numpy as np


class Hist:

    def __init__(self, variable, b):
        self.bins = np.linspace(0, 1, b)
        self.p, self.x = np.histogram(variable, bins=self.bins)  # bin it into n = N//10 bins
        #print("p ", self.p, " x ", self.x)
