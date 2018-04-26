import sys, os
#This is a bunch of utilities for sequence manipulation


#This is for reading in fastas and returning dictionaries
def fasta_parse(fasta):
	count = 0
	size = 0
	Dict = {}
	Dict_length = {}
	for line in fasta:
		line = line.strip()
		if line[0] == ">":
			if count != 0:
				Dict[name] = seq
				size = len(seq)
				Dict_length[name] = size
			name = line
			seq = ""
		else:
			seq = seq + line
		count += 1
	#Dealing with last seq
	Dict[name] = seq
	size = len(seq)
	Dict_length[name] = size;
	
	return Dict, Dict_length
	
