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
import math
import numpy as np
from scipy import stats
#from scipy.stats import ttest_ind
def main(firstInput, secondInput, thirdInput, Output):

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

	H=int(thirdInput)  # comparing point
	
	N1=np.array(data1[:][H], dtype = 'float_')  # normalize
	if np.max(N1)-np.min(N1)!=0:
		n=((N1-np.min(N1))/(np.max(N1)-np.min(N1))) #C

	L=int(secondInput)  # segmenting point
	
	for j in range(0, L): #A"
		iind=j
		k1=np.array(data1[:][iind], dtype = 'float_')
		if np.max(k1)-np.min(k1)!=0:
				k=((k1-np.min(k1))/(np.max(k1)-np.min(k1)))
	
		for i in range(L, len(data1)): #"B"
			iind2=i
			m1=np.array(data1[:][iind2], dtype = 'float_')	
			if np.max(m1)-np.min(m1)!=0:
				m=((m1-np.min(m1))/(np.max(m1)-np.min(m1)))
	
			r12,p1=stats.pearsonr(k,m)  # performing partial correlation (A,B,C)
			r13,p1=stats.pearsonr(k,n)
			r23,p1=stats.pearsonr(m,n)	
			r123=(r12-r13*r23)/math.sqrt((1-math.pow(r13,2))*(1-math.pow(r23,2)))  
	
			if 	abs(r123)>0.2 and j!=i:
					c.writerow( [label[j], label[iind2], label[H], round(r123,4)]) # print final result
		
main(sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4])
	

