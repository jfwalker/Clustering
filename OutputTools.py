import sys,os
import networkx as nx
import ClusterTools

def SummarizeBlast(Name,Matches):
	
	outw = open(Name, "w")
	outw.write("###Best Blast Hits###" + "\n")
	for keys in sorted(Matches):
		temp = ""
		unique = {}
		for x in Matches[keys]:
			unique[x] = x
		for x in unique:
			temp = temp + x + ","
		outw.write(keys + "\t" + temp + "\n")
		
def PrintCombined(MatchList,Folder1,Folder2,OutputFolder,Cluster1Hash,Cluster2Hash,NameOfOutfile):
	
	outw = open(NameOfOutfile, "a")
	
	outw.write("###Combinations###" + "\n")
	#make graph and connect edges
	Graph = nx.Graph()
	Graph.add_edges_from(MatchList)
	
	#Get the folder names to add items into folders
	NameOfFolder1 = ClusterTools.FolderNameCheck(Folder1)
	NameOfFolder2 = ClusterTools.FolderNameCheck(Folder2)
	NameOfOutputFolder = ClusterTools.FolderNameCheck(OutputFolder)
	
	
	#From the graph print out clusters
	count = 0
	array = []
	for line in nx.connected_components(Graph):
		cmd = "cat "
		test = list(line)[0]
		for element in list(line):
			
			array = element.split(".folder")
			if array[1] == "1":
				cmd += NameOfFolder1 + array[0] + " "
				del Cluster1Hash[array[0]]
			else:
				cmd += NameOfFolder2 + array[0] + " "
				del Cluster2Hash[array[0]]
		cmd += " > "
		outcluster = "Cluster" + str(count) + ".fa"
		cmd += NameOfOutputFolder + outcluster
		outw.write(cmd + "\n")
		os.system(cmd)
		count += 1
	outw.write("###No Hit###" + "\n")
	for keys in Cluster1Hash:
		cmd = ""
		outw.write("NoHits Folder 1: " + Cluster1Hash[keys] + "\n")
		cmd += "cp " + NameOfFolder1 + Cluster1Hash[keys] + " " + NameOfOutputFolder + "NC_F1_" + Cluster1Hash[keys]
		os.system(cmd)
	for keys in Cluster2Hash:
		cmd = ""
		outw.write("NoHits Folder 2: " + Cluster2Hash[keys] + "\n")
		cmd += "cp " + NameOfFolder2 + Cluster2Hash[keys] + " " + NameOfOutputFolder + "NC_F2_" + Cluster2Hash[keys]
		os.system(cmd)

		
