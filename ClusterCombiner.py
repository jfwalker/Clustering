import sys,os
import Seq

if len(sys.argv) != 4:
	print "Usage: python ClusterCombiner.py Folder1 Folder2 NumbOfBaits"
	sys.exit()

Cluster = sys.argv[1]
Cluster2 = sys.argv[2]
NumbOfSeqs = int(sys.argv[3])
NegNumbOfSeqs = NumbOfSeqs * -1

for filename in os.listdir(Cluster):
	
	#Because Drew is picky
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
	
	#Choose largest genes from files
	test = sorted(Dict_length.items(), key=lambda x: x[1])
	
	filename_count = 0;
	if NumbOfSeqs < len(Dict_length.keys()):
		for x in range(NegNumbOfSeqs, 0):
			print ">" + filename + "@" + str(filename_count)
			print Dict[test[x][0]]
			filename_count += 1
	else:
		for keys in Dict:
			print ">" + filename + "@" + str(filename_count)
			print Dict[keys]
			filename_count += 1

