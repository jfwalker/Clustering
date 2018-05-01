import sys,os
import networkx as nx

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
		
def PrintCombined(MatchList,Folder):
	
	Graph = nx.Graph()
	Graph.add_edges_from(MatchList)
	
	
	
	for line in nx.connected_components(Graph):
		test = list(line)[0]
		for element in list(line):
			print element
		print "Cluster"
		
