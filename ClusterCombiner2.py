import sys,os
import Seq, ClusterTools

if len(sys.argv) != 4:
	print "Usage: python ClusterCombiner.py Folder1 Folder2 NumbOfBaits"
	sys.exit()

Cluster = sys.argv[1]
Cluster2 = sys.argv[2]
NumbOfSeqs = int(sys.argv[3])
BlastDb = open("BlastDatabase.fa", "w")
TestCluster = open("BlastQuery.fa", "w")

#Do this for the first cluster (one to make database of)
ClusterTools.ClusterMaker(Cluster,NumbOfSeqs,BlastDb)


#Do this for the query cluster
ClusterTools.ClusterMaker(Cluster2,NumbOfSeqs,TestCluster)

#Make the blast database
cmd = ""
cmd =  "makeblastdb -in BlastDatabase.fa -out BlastDatabase.fa -dbtype='nucl'"
os.system(cmd)

#Run the blast
cmd = ""
cmd = "blastn -db BlastDatabase.fa -query BlastQuery.fa -evalue 1e-3 -num_threads 3 -max_target_seqs 1 -out Hits.rawblastn -outfmt '6 qseqid qlen sseqid slen frames pident nident length mismatch gapopen qstart qend sstart send evalue bitscore'"
os.system(cmd)

#Make a synthesis of the hits
hits = ""
hits = "Hits.rawblastn"
ClusterTools.MatchIt(hits)
