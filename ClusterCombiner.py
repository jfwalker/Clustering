import sys,os


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
	for line in File:
	
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

	#Choose largest genes from files
	test = sorted(Dict_length.items(), key=lambda x: x[1])
	
	if NumbOfSeqs < len(Dict_length.keys()):
		for x in range(NegNumbOfSeqs, 0):
			print Dict[test[x][0]]
	else:
		print "Too Large"

