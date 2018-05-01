import sys,os
import Seq, ClusterTools, OutputTools

if len(sys.argv) != 6:
	print "Usage: python ClusterCombiner.py Folder1 Folder2 NumbOfBaits OutFile OutFolder"
	sys.exit()

Cluster = sys.argv[1]
Cluster2 = sys.argv[2]
NumbOfSeqs = int(sys.argv[3])
NameOfOutfile = str(sys.argv[4])
Folder = str(sys.argv[5])

BlastDb = open("BlastDatabase.fa", "w")
TestCluster = open("BlastQuery.fa", "w")
#HitsFile = open(NameOfOutfile, "w")


#Do this for the first cluster (one to make database of)
AllClustsFolder1 = {}
AllClustsFolder1 = ClusterTools.ClusterMaker(Cluster,NumbOfSeqs,BlastDb)


#Do this for the query cluster
AllClustsFolder2 = {}
AllClustsFolder2 = ClusterTools.ClusterMaker(Cluster2,NumbOfSeqs,TestCluster)

#Make the blast database
cmd = ""
cmd =  "makeblastdb -in BlastDatabase.fa -out BlastDatabase.fa -dbtype='nucl'"
os.system(cmd)

#Run the blast
print "Running Blast"
cmd = ""
cmd = "blastn -db BlastDatabase.fa -query BlastQuery.fa -evalue 1e-3 -num_threads 3 -max_target_seqs 1 -out Hits.rawblastn -outfmt '6 qseqid qlen sseqid slen frames pident nident length mismatch gapopen qstart qend sstart send evalue bitscore'"
os.system(cmd)

#Make a synthesis of the hits
print "Analyzing hits"
Matches = {}
MatchList = []
hits = ""
hits = "Hits.rawblastn"
Matches,MatchList = ClusterTools.MatchIt(hits)

#Summarize Output to file
print "Summarizing results"
OutputTools.SummarizeBlast(NameOfOutfile,Matches)

#Print to the new folder
print "Combining clusters"
OutputTools.PrintCombined(MatchList,Cluster,Cluster2,Folder,AllClustsFolder1,AllClustsFolder2,NameOfOutfile)

print "####Results####"
print "Clusters Combined summary is: " + NameOfOutfile + "\n" + "Folder with clusters is: " + Folder

#clean the area
cmd = ""
cmd = "rm BlastDatabase* BlastQuery.fa Hits.rawblastn"
os.system(cmd)


