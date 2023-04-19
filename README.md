# Clustering
Ericales and Nyctag etc....
Basic program to combine clusters

The first two arguments are folders with clusters to be combined, the next argument is how many samples you want to check
for the combination. It will sample the most character rich from each cluster, or if the number is larger than the cluster
it will use all of them. The next argument is a file in which to pul all the clusters that are combined and then finally
the name of an empty folder in which the new clusters will be added.

This relies upon Networkx from python and blast

```Ex: python CombineClades.py Test1/ Test2/ 10 Out Combined```
