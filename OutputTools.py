import sys,os
import networkx as nx
import ClusterTools

def SummarizeBlast(Name,Matches):
	
	outw = open(Name, "w")
	for keys in sorted(Matches):
		temp = ""
		unique = {}
		for x in Matches[keys]:
			unique[x] = x
		for x in unique:
			temp = temp + x + ","
		outw.write(keys + "\t" + temp + "\n")
		
def PrintCombined(MatchList,Folder1,Folder2,OutputFolder):
	
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
			else:
				cmd += NameOfFolder2 + array[0] + " "
		cmd += " > "
		outcluster = "Cluster" + str(count)
		cmd += NameOfOutputFolder + outcluster
		os.system(cmd)
		count += 1
		
