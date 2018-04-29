import sys,os

def SummarizeBlast(NameOfOutfile,Matches):
	
	for keys in sorted(Matches):
		temp = ""
		unique = {}
		for x in Matches[keys]:
			unique[x] = x
		for x in unique:
			temp = temp + x + ","
		NameOfOutfile.write(keys + "\t" + temp + "\n")
		
def PrintCombined(Hits,Folder):
	
	print "Need to add"
