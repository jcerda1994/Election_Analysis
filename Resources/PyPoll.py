import datetime as dt
now=dt.datetime.now()

print('the time irght now is',now)


import csv


file_to_load='Resources/election_results.csv'

election_data = open(file_to_load, 'r') #---->open and close
election_data.close()


with open(file_to_load) as election_data:
    print(election_data)
    
    
import os
dir(os)
print(dir(os.path))

#CHAINING
import csv
import os

file_to_load=os.path.join('Resources','election_results.csv') #----> read a file
with open(file_to_load) as election_data:
    print(election_data)


# file_to_save=os.path.join('analysis','election_analysis.txt')  #---->create a file in a folder
# open(file_to_save,'w')

file_to_save=os.path.join('analysis','election_analysis.txt')  #---->create a file in a folder AND WRITE
outfile=open(file_to_save,'w')
outfile.write('hello world')
outfile.close()

#or (CLEANER)

file_to_save=os.path.join('analysis','election_analysis.txt')
with open(file_to_save,'w') as txt_file:
    txt_file.write("Arapahoe\nDenver\nJefferson")


#REDA THE ELECTION RESULTS:#####

import csv
import os
file_to_load=os.path.join("Resources","election_results.csv")
file_to_save=os.path.join("analysis",'election_analysis.txt')

with open(file_to_load) as election_data:
    #to do:read and analyze the data here
    file_reader=csv.reader(election_data)
    
    headers=next(file_reader)
    print(headers)
    
    

    
