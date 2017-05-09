# python

import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

# Read stock csv file

dates = []
prices = []
def get_data(filename):
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
    		next(csvFileReader)	# skipping column names
		for row in csvFileReader:
			dates.append(int(row[0].split('-')[0])) #
			prices.append(float(row[1]))
	return

get_data('aapl.csv') # calling get_data method by passing the csv file to it

#print "Dates- ", dates
#print "Prices- ", prices
