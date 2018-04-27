import sys,os
import Seq

'''
Ignore the variable names in this, it takes in a cluster and grabs the most character rich sequences based
on the sequences and makes a fasta
'''

#Cluster for the blast database, A negative number (array is indexed backwards), The number of Seqs interested, The Name of the newfile
def ClusterMaker(Cluster,NumbOfSeqs,BlastDb):
	NegNumbOfSeqs = NumbOfSeqs * -1
	for filename in os.listdir(Cluster):
		
		#Check if using kept the / for the folder (Drews fault)
		if Cluster[-1] != "/":
			toOpen = Cluster + "/" + filename
		else:
			toOpen = Cluster + filename		
		File = open(toOpen, "r")
		Dict = {}
		Dict_length = {}
		count = 0
		size = 0
		seq = ""
		name = ""
		
		#Read in each file and save as a dictionary
		Dict, Dict_length = Seq.fasta_parse(File)
		
		#Choose largest genes from files (does it in reverse)
		test = sorted(Dict_length.items(), key=lambda x: x[1])
		
		#create a database out of the selected genes
		filename_count = 0;
		if NumbOfSeqs < len(Dict_length.keys()):
			for x in range(NegNumbOfSeqs, 0):
				BlastDb.write(">" + filename + "@" + str(filename_count) + "\n" + Dict[test[x][0]] + "\n")
				filename_count += 1
		else:
			for keys in Dict:
				BlastDb.write(">" + filename + "@" + str(filename_count) + "\n" + Dict[keys] + "\n")
				filename_count += 1

#This takes in a hits file and summarizes what has hit what
#Pythons syntax is super dull
def MatchIt(hits):
	
	blastfile = open(hits, "r")
	for line in blastfile:
		line = line.strip()
		SizeDiff = 0
		biggest = 0
		array = []
		array = line.split("\t")
		print array
		SizeDiff = int(array[1]) - int(array[3])
		
		#Get the one that's larger
		if(0 < SizeDiff):
			biggest = array[1]
		else:
			biggest = array[3]
		SizeDiff = abs(SizeDiff)
		print SizeDiff
		
	
