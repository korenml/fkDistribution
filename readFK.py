import hist
import numpy as np


class Read:
    def __init__(self, path, treshold):
        self.fk = []
        self.fk2 = []
        mean = 0
        mean2 = 0
        with open(path) as f:
            datalines = f.readlines()

            for i in range(0, len(datalines)):
                if "internalField" in datalines[i]:
                    print(datalines[i])
                    self.cells = int(datalines[i + 1].replace("\n", ""))
                    print(datalines[i + 2])
                    start = i + 3
                if "boundaryField" in datalines[i]:
                    print("end: ", datalines[i - 4])
                    end = i - 4

            for i in range(start, end + 1):
                value = datalines[i].replace("\n", "")
                mean += float(value)
                self.fk.append(float(value))
                if float(value) < treshold:
                    self.fk2.append(float(value))
                    mean2 += float(value)

        mean = mean/len(self.fk)
        sorted = np.sort(self.fk)
        n = len(sorted)
        if n % 2 == 0:
            median1 = sorted[n // 2]
            median2 = sorted[n // 2 - 1]
            median = 0.5*(median1 + median2)
        else:
            median = sorted[n // 2]
        print("cells ", self.cells, " values ", len(self.fk))
        print("Min: ", min(self.fk), " mean: ", mean, " median: ", median)


        mean2 = mean2/len(self.fk2)
        sorted2 = np.sort(self.fk2)
        n2 = len(sorted2)
        if n2 % 2 == 0:
            median21 = sorted2[n2 // 2]
            median22 = sorted2[n2 // 2 - 1]
            median2 = 0.5*(median21 + median22)
        else:
            median2 = sorted2[n2 // 2]
        print("cells ", self.cells, " values ", len(self.fk2))
        print("Min2: ", min(self.fk2), " mean2: ", mean2, " median2: ", median2)

