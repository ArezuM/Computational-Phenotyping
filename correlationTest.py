from __future__ import division 
import string
import re
import csv
import os
import math
from string import punctuation
from os.path import isfile, join
from numpy import genfromtxt
from string import punctuation
import numpy as np
from scipy import stats
import sys

def main(firstInput, SecondInput, Output):

	f1 = open(firstInput, 'rU')  # read inputs	
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

	c = csv.writer(open(Output, "wb"))	# deifne output file
	
	L=int(secondInput)  # segmenting point
	
	for j in range(0, L):
		iind=j
		k1=np.array(data1[:][iind], dtype = 'float_')  
		if np.max(k1)-np.min(k1)!=0: # normalize
				k=((k1-np.min(k1))/(np.max(k1)-np.min(k1)))
	
		for i in range(L, len(data1)):
			iind2=i
			m1=np.array(data1[:][iind2], dtype = 'float_')	
			if np.max(m1)-np.min(m1)!=0:
				m=((m1-np.min(m1))/(np.max(m1)-np.min(m1)))
	
			r1,p1=stats.pearsonr(k,m)  # performe correlation test 
			if 	p1<0.05 and j!=i:
					c.writerow( [label[j], label[iind2], round(r1,4),round(p1,4)])
					
	return 0;
	
main(sys.argv[1], sys.argv[2], sys.argv[3])

		
			
	
