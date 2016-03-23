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
#from scipy.stats import ttest_ind

def main(firstInput,SecondInput, intersect, missedvalue):
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
	dat1=zip(*d1)
	
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
	dat2=zip(*d2)
	
	c1 = csv.writer(open(intersect, "wt")) # output files 
	c2 = csv.writer(open(missedvalue, "wt"))
	
	c1.writerow(label[0:]+label2[1:])
	c2.writerow(["ID"])
		
	for i in range (0, len(d2)-1):
		try: 		# marge values 
			ind=data1[0][:].index(data2[0][i]);				
			c1.writerow(d1[:][ind]+d2[1:][i])
	
		except ValueError: # missing transcripts
			c2.writerow(data2[0][i])
	return 0;
	
main(sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4] )		
	
		