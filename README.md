# python
<
import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
>
# Read stock csv file
<
def get_data(filename):
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
    		next(csvFileReader)	# skipping column names
		for row in csvFileReader:
			dates.append(int(row[0].split('-')[0])) #
			prices.append(float(row[1]))
	return
>
