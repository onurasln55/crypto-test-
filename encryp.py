import os
import fnmatch
path="h:/" #partition
key=input()
for root, dir, files in os.walk(path):#folder walking
        print (root)
        print ("")
        for items in fnmatch.filter(files, "*"):
                print ("..." + items)
                os.rename(root+"/"+items,root+"/"+items+"."+key)
        print ("")
