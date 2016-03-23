# Written by AREZOO MOVAGHAR
# Contact info: amovaghar@wisc.edu

from __future__ import division 
import string
import sys
import re
import csv
import os
from string import punctuation
from os.path import isfile, join
from string import punctuation

def featureExt(path,typeIn,output):

	c1 = csv.writer(open(output, "wt"))
	c1.writerow(["ID","UtrNo","StatementNo","ExclamationNo","QuestionsNo","AbondanedUtr","OneWordUtr","UtrWithMazes","UtrWithPauses","UtrWithOmissions","Total completed words","MLU in words","Number of words", "Number of Mazes", "Number of Maze words", "Maze words Percentage","Words rate", "Within_Utr Pauses","Average Mazes per Utterance", "Average Word per Mazes", "RevisionNo","Revision_partword", "Revision_word", "Revision_phrase", "RepetitionNo", "Repetition_partword", "Repetition_word", "Repetition_phrase","FilledPauses", "Dysfluency","UL0","UL1","UL2","UL3","UL4","UL5","UL6","UL7","UL8","UL9","UL10","UL11","UL12","UL13","UL14","UL15+", "PUMUL0","PUMUL1","PUMUL2","PUMUL3","PUMUL4","PUMUL5","PUMUL6","PUMUL7","PUMUL8","PUMUL9","PUMUL10","PUMUL11","PUMUL12","PUMUL13","PUMUL14","PUMUL15+", "NMUL0","NMUL1","NMUL2","NMUL3","NMUL4","NMUL5","NMUL6","NMUL7","NMUL8","NMUL9","NMUL10","NMUL11","NMUL12","NMUL13","NMUL14","NMUL15+", "NMML0","NMML1","NMML2","NMML3","NMML4","NMML5","NMML6","NMML7","NMML8","NMML9","NMML10","NMML11","NMML12","NMML13","NMML14","NMML15+", "NUNM0","NUNM1","NUNM2","NUNM3","NUNM4","NUNM5","NUNM6+","Label"
	])
	# read .SLT files from input directory
	Name="";
	for filename in os.listdir(path):
	  if filename.endswith(".SLT") or filename.endswith(".slt"):
	    Name=filename.split('.')[0]; #extarct the name 
	    ID=filename.split('_')[0];	#extarct the ID
		
	    if typeIn=="FX":
		    label=1;
	    else:
		    label =0;
	    file=os.path.join(path, filename); # read input file
	    f=open(file, 'r');
	    
	 #####################INIT ######################
	    dist=[0 for i in range(0, 16)];
	    m_dist=[0 for i in range(0, 16)];
	    ml_dist=[0 for i in range(0, 16)];
	    l_dist=[0 for i in range(0, 16)];
	    ld=[0 for i in range(0, 16)];
	    
	    um_dist=[0 for i in range(0, 7)];
	
	    wordNo=0;
	    UtrNo=0;
	    StatementNo=0;
	    ExclamationNo=0 
	    QuestionsNo=0;
	    IntonationPrompts=0;
	    AbondanedUtr=0;
	    InterruptedUtr=0;
	    VerbalUtr=0;
	    NonVerbalUtr=0;
	    UninteligibleUtr=0;
	    PartlyIntelligibleUtr=0;
	    ResponsesToQuestions=0;
	    Yes_No_Responses=0;
	    ResponsesToIntonations=0;
	    Imitations=0;
	    OneWordUtr=0;
	    UtrWithMazes=0;
	    UtrWithPauses=0; 
	    UtrWithOmissions=0;
	    UtrWithOverlappingSpeech=0;
	    UtrWithWordCodes=0;
	    UtrWithUtrCodes=0;
	    ElapsedTime=0;
	    BetUtrPauses=0;
	    FilledPauses=0;
	    RevisionNo=0;
	    Revision_phrase=0;
	    Revision_word=0;
	    Revision_partword=0;
	    RepetitionNo=0;
	    Repetition_phrase=0;
	    Repetition_partword=0;
	    Repetition_word=0;
	    OmissionNo=0;
	    Imitation=0;
	    OverlappingSpeech=0;
	    ll=0
	    wordNo2=0
	    punct='!$%&()+,-./:;<=>?@[\]^_`{|}~'
	    pause=0	
	    Omissions=0
	    MazeNo=0
	    N_ml=0; 
	    Omis=0
	################################################
	
	    for line2 in f:  # process input file line by line 
	      if len(line2)>2:
	        
	        nml=0
	        line= line2.replace(',','')
	        utrL=0;
	        ll=ll+1
	        start=line[0]	
	        if start=="$": # process the header
	          l=re.compile('\w+').findall(line);
	
	          spk1=l[0][0]; # find the speaker IDs
	          spk2=l[1][0];
	
	        elif start==spk1: # process the paitents lines of speech
	
	                StatementNo+=line.count('.');  		# statements
	                line= line.replace('.','')	
	                ExclamationNo+=line.count('!'); 	# Exclamations
	                QuestionsNo+=line.count('?'); 		# Questions
	                line= line.replace('?','')	
	                line= line.replace('[',' [')
	                line= line.replace('"','')		
	                pause=pause+line.count(':'); 		# pauses 
	                IntonationPrompts+=line.count('~'); # prompts
	                AbondanedUtr+=line.count('>')-line.count('<'); # unfinished utterances
	
	                InterruptedUtr+=line.count('^');	# interuption by examiner 
	             #   OmissionNo+=line.count("*");		# Omissions
	                
	                if line.find("(")>-1: 				# check for dysfluency occurance in the current utterance
	                        UtrWithMazes+=1
	                t=0
	                i=1;
	                nml=line.count('(');				# number of dysfluencies
	                utr= line.split('\r\n');
	                line= line.replace('\r\n','')	
	                line= line.replace('\n','')	
	        
	                UtrNo+=(len(utr)-1)
	                if UtrNo<StatementNo+AbondanedUtr:
	                  UtrNo=StatementNo+AbondanedUtr
	                word = []
	                ww=line.upper().split(' ');			
	                for wt in ww:							# filter words				
	                        #wt=wr.split()				
	                        if len(wt)>0:
	                                word.append(wt)
	                filter(None, word)
	
	                if (word[i]=="YES") or (word[i]=="No"): # count number of "YES" or "NO" responses. 
	                
	                        Yes_No_Responses+=1;		
	
	                wl=0;		
	                	
	                while i < len(word):					# process the current utterance word by word	
	                        w=word[i];		
	                        wl+=1;		
	                        te=w.upper().find("X"); 		#find uninteligible utterances (utterances with X)
	                        if te==0:				
	                                UninteligibleUtr+=1		
	                        Rutr="";
	                        if w[0]=="(": 					# process the dysfluency statemnet 
	                                wl-=1;
	                                MazeNo+=1;
	                                Rutr="";
	                                j=i
	                                strt=i
	                                if word[j].find(")")!=-1:		# find the dysfluenct segmnet
	                                        Rutr=word[i].strip(punct)		
	                                        i+=1;				
	                                else:						
	                                        j=i+1;
	                                        Rutr=word[i][1:].strip(punct)
	                                        if word[j][0]=="*":
	                                                Omissions+=1;
	                                        while word[j].find(")")==-1:				
	                                                        Rutr=' '.join([Rutr,word[j].strip(punct)])
	                                                        if word[j][0]=="*":
	                                                                Omissions+=1;
	
	                                                        j+=1
	                                        
	                                        Rutr=' '.join([Rutr,word[j].strip(punct)])
	                                        i=j+1;
	                                                                                        
	                                ml=len(Rutr.split());   # process the dysfluent segment
	                                N_ml+=ml;  
	                                if ml<15:  				# distrbution of dysfluency (by length)
	                                        m_dist[ml]=m_dist[ml]+1;		
	                                elif ml>=15:
	                                        m_dist[15]=m_dist[15]+1;		
	                                wordNo2+=ml;            # number of words in dysfluent segemt (by sample)
	
	                                if Rutr.upper().count("UM") or Rutr.upper().count("UH") or Rutr.upper().count("EH"): # count filled pauses in the current dysfluent segment
	                                  FilledPauses+=Rutr.upper().count("UM")+ Rutr.upper().count("UH") + Rutr.upper().count("EH"); 
	                                  Rutr=Rutr.upper().replace("UM",'')
	                                  Rutr=Rutr.upper().replace("UH",'') 				
	                                  Rutr=Rutr.upper().replace("EH",'') 				
	                                rep=False;  # process revisions and repetitions
	                                rev=False;
	                                crep=0
	                                crev=0
	                                Rutrd=Rutr.split()
	                                Tutr=Rutr.split();
	                                ti=0
	                                Sutr=[]
	                                srev=0
	                                while ti< len(Tutr):
	                                        tu=Tutr[ti]
	                                        Sutr.append(tu);
	                                        if tu in Tutr[ti+1:] and not("*" in tu): # repetition word inside the segment
	                                                tnd=ti+1+Tutr[ti+1:].index(tu)
	                                                if tnd==ti+1:
	                                                        RepetitionNo+=1;
	                                                        Repetition_word+=1;
	                                                        Sutr.pop()
	                                                        ti=tnd;								
	                                                else:
	                                                
	                                                        if len(Tutr)> tnd+tnd-ti-1 and Tutr[ti:tnd]==Tutr[tnd:tnd+tnd-ti]: # repetision phrase inside the segment 
	                                                                RepetitionNo+=1;
	                                                                Repetition_phrase+=1;
	                                                                Sutr.pop()
	                                                                ti=tnd
	
	                                                        else:
	                                                                ti=ti+1;
	                                                                
	                                        else:
	                                                if "*" in tu:		# repetition part-word inside the segment
	                                                        if ti+1< len(Tutr) and Tutr[ti+1].find(tu[:-1])==0:
	                                                                RepetitionNo+=1;
	                                                                Repetition_partword+=1;
	                                                                Sutr.pop()									
	                                                
	                                                ti=ti+1;
	                                ui=0
	                                lc=0
	
	                                while ui< len(Sutr) and i< len(word):		# process dysfluent segment considering the next words (outside the segment( 								
	                                        if Sutr[ui]==word[i]:
	                                                ki=ui
	                                                kj=i
	                                                while ki< len(Sutr) and kj<len(word):
	                                                        if word[kj]!=Sutr[ki]:							
	                                                                break
	                                                        lc+=1;
	                                                        ki+=1;
	                                                        kj+=1;
	                                                
	                                                if ki+1==len(Sutr) and Sutr[ki][-1]=="*":
	                                                                if word[kj].find(Sutr[ki][:-1])==0:
	                                                                        lc+=1;
	                                                                        ki+=1;
	                                                                        kj+=1;										
	                                                if ki== len(Sutr):  
	                                                        RepetitionNo+=1;  # repetition outside the segment 
	                                                        
	                                                        if lc==1:
	                                                                Repetition_word+=1; # repetition word outside the segment 
	                                                        else:																
	                                                                Repetition_phrase+=1; # repetition phrase outside the segment 
	                                                else:
	                                                        lc=0
	                                        else:						
	                                                if ui+1==len(Sutr) and Sutr[ui][-1]=="*":							
	                                                        if word[i].find(Sutr[ui][:-1])==0:
	                                                                RepetitionNo+=1;
	                                                                Repetition_partword+=1; # repetition part-word outside the segment 
	                                                                lc=lc+1;
	                                                        
	                                                        
	                                        ui+=1	
	                                strc=0;
	                                if len(Sutr)-lc>0:   # process revisions
	                                        if Sutr[0][-1]=="*":						
	                                                tr=0
	                                                while tr< len(Sutr)-lc and Sutr[tr][-1]=="*":
	                                                        strc+=1;
	                                                        tr+=1;
	                                                        RevisionNo+=1;		
	                                                        Revision_partword+=1
	                                        if len(Sutr)-lc-strc==1:
	                                                RevisionNo+=1;		
	                                                Revision_word+=1
	                                        if len(Sutr)-lc-strc>1:
	                                                RevisionNo+=1;		
	                                                Revision_phrase+=1
	
	                        
	                                                          
	                        #### end of dysfluent segment processing####                        
	                        elif w[0]=="<":
	                          OverlappingSpeech+=1;  # overlap in speech 
	                          UtrWithOverlappingSpeech+=1;
	                          wl-=1;
	                          j=i					
	                          while word[j][-1]!=">":
	                                  j+=1
	                          i=j+1;
	                                
	                        elif w[0]=="[":  # Error in speech
	                          j=i; 
	                          wl-=1;
	                          if w.find(':')!=-1:
	                                  pause-=1;
	                          if w.find("EW"):
	                                  UtrWithWordCodes+=1;
	
	                          else:
	                                  if w.find("EU"):
	                                          UtrWithUtrCodes+=1;
	                          while word[j].find("]")==-1:
	                                  j+=1
	                          i=j+1;
	
	        
	                        elif w[0]=="*":
	                          Omissions+=1;
	                          i+=1
	                          wl-=1;
	
	                        else:
	                          wordNo+=1;				
	                          utrL+=1;
	                          i+=1;
	        
	                
	                if pause>0:
	                  UtrWithPauses+=1; 
	                  pause=0
	                if Omissions>0:
	                  UtrWithOmissions+=1;
	                  Omis+=Omissions
	                  Omissions=0	
	               
	                wordNo2+=wl; 
	
	                if wl<15:  # dysfluency distrbutions
	                        dist[wl]=dist[wl]+1;		
	                elif wl>=15:
	                        dist[15]=dist[15]+1;
	                
	                if nml<6: # dysfluency length distrbution
	                        um_dist[nml]=um_dist[nml]+1;
	                else:
	                        um_dist[6]=um_dist[6]+1;		
	
	                if nml>0:
	                  if nml<15:
	                    ml_dist[nml]=ml_dist[nml]+1;
	                  elif nml>=15:
	                    ml_dist[15]=ml_dist[15]+nml;	
	                
	                if nml>0:
		                 if wl<15:
	        	            l_dist[wl]=l_dist[wl]+1;		
		                 else:	
	                	    l_dist[15]=l_dist[15]+1;					
  
	      if utrL==1:
	          OneWordUtr+=1;	# one word utterances		
	
	      for i in range (0, 16):
	            if dist[i]>0:  # percentage of utterances with dysfluency (length distrbution)
	                    ld[i]=l_dist[i]/dist[i]
	      
	      # write in output file               
	    c1.writerow([ID,UtrNo,StatementNo,ExclamationNo,QuestionsNo,AbondanedUtr,OneWordUtr,UtrWithMazes,UtrWithPauses,UtrWithOmissions, wordNo,wordNo/UtrNo,wordNo2, MazeNo,N_ml, N_ml/wordNo2,wordNo2/5, UtrWithPauses, MazeNo/UtrNo, N_ml/max(MazeNo, 0.00000001),RevisionNo,Revision_partword, Revision_word, Revision_phrase, RepetitionNo, Repetition_partword, Repetition_word, Repetition_phrase, FilledPauses,RepetitionNo+RevisionNo+AbondanedUtr]+dist+ ld+m_dist+ml_dist+ um_dist+[label])

	f.close();
####################################################################	
def main(inputDir,inputType, output):
	
	featureExt(inputDir,inputType, output)
	
main(sys.argv[1], sys.argv[2], sys.argv[3])

