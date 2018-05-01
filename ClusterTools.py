import sys,os
import Seq
#from collections import defaultdict
'''
Ignore the variable names in this, it takes in a cluster and grabs the most character rich sequences based
on the sequences and makes a fasta
'''

#Check folder names becomes weirdly useful
def FolderNameCheck(Folder):
	if Folder[-1] != "/":
		toOpen = Folder + "/"
	else:
		toOpen = Folder
	return toOpen	

#Cluster for the blast database, A negative number (array is indexed backwards), The number of Seqs interested, The Name of the newfile
def ClusterMaker(Cluster,NumbOfSeqs,BlastDb):
	NegNumbOfSeqs = NumbOfSeqs * -1
	ClusterNames = {}
	for filename in os.listdir(Cluster):
		
		ClusterNames[filename] = filename
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
	return ClusterNames

#This takes in a hits file and summarizes what has hit what
#Pythons syntax is super dull
def MatchIt(hits):
	
	Match_Hash = {}
	match_list = []
	blastfile = open(hits, "r")
	
	for line in blastfile:
		
		line = line.strip()
		array = []
		temp_list = []
		matches = ()
		array = line.split("\t")
		#print array
		species1_array = array[0].split("@");
		species2_array = array[2].split("@");
		#Make a hash of names representing the hits
		species1_array[0] = species1_array[0] + ".folder2"
		species2_array[0] = species2_array[0] + ".folder1"
		
		#For the graph make a list of tuples
		temp_list = [species1_array[0], species2_array[0]]
		matches = tuple(temp_list)
		match_list.append(matches)
		
		#Get the unique hits for the output file
		if species1_array[0] in Match_Hash:
			Match_Hash[species1_array[0]].append(species2_array[0])
		else:
			Match_Hash[species1_array[0]] = []
			Match_Hash[species1_array[0]].append(species2_array[0])
	return Match_Hash,match_list

