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

	c1 = csv.writer(open(Output, "wt"))
	c1.writerow(["Feature", "dif","F1 score"])


	for j in range (0, len(label)):
		ct=0; 
		FS=0
		for i in range (1, len(d1)):
			if d1[i][j]!=d2[i][j]:  # compare the values
				ct+=1; 
				if d1[i][j]> d2[i][j]:
				   PR=0;
				   if float(d1[i][j])!=0:
						 PR=float(d2[i][j])/float(d1[i][j]);  # precision for the current transcript
				   RC=0
				   if float(d2[i][j])!=0:
						RC=float(d1[i][j])/float(d2[i][j]);   # recall for the current transcript	
	
				else:
					PR=0; 
					if float(d1[i][j])!=0:
						 PR=float(d1[i][j])/float(d1[i][j]);
					RC=0
	
					if float(d2[i][j])!=0:
						RC=float(d1[i][j])/float(d2[i][j]); 				
					
				if (PR+RC) !=0:  # F1 measure for one transcript
					F1=2*PR*RC/(PR+RC) 	
				else: 
					F1=0
				print F1
				FS+=F1; 
		FF=	(len(d1)-ct+FS)/len(d1)  # average F1 measure
		
		c1.writerow([label[j],ct, FF]) # print the results

	return 0;
	
main(sys.argv[1], sys.argv[2], sys.argv[3])