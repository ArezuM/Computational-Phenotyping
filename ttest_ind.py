from __future__ import division 
import string
import re
import csv
import os
from string import punctuation
from os.path import isfile, join
from numpy import genfromtxt
from string import punctuation
import numpy as np
from scipy import stats
import numpy.ma as ma
import sys

def main(firstInput,SecondInput, Output):
	
	f1 = open(firstInput, 'rU')  # read inputs
	f2 = open(SecondInput, 'rU')
	
	csv_f = csv.reader(f1) #Organize inputs in matrix
	d1 = []
	label =[]
	i=1
	for row in csv_f:
		if i==1:
			label =row
		else:
			d1.append(row)  
		i=i+1;
	data1=zip(*d1)
	
	csv_f2 = csv.reader(f2)
	d2 = []
	label2 =[]
	i=1
	for row in csv_f2:
		if i==1:
			label2 =row
		else:
			d2.append(row)  
		i=i+1;
	data2=zip(*d2)
	
	c = csv.writer(open(Output, "wb"))	# deifne output file
	c.writerow(["Feature", "mean1", "std1", "mean2", "std2", "t", "p" ])	
	
	for iind in range(1, len(data2)):
		print data2[:][iind]
		m=np.array(data2[:][iind], dtype = 'float_')
		k=np.array(data1[:][iind], dtype = 'float_')	
		try:
			t1,p1=stats.ttest_ind(m, k,equal_var=False ) # perform t-test 
		except ValueError:
			t1=Null
			p1=Null
		c.writerow([label[iind], round(np.mean(m),3) , round(np.std(m),3), round(np.mean(k),3) , round(np.std(k),3), round(t1,3) , round(p1,3)]) # print the results in output file 
	return 0;
	
main(sys.argv[1], sys.argv[2], sys.argv[3])
