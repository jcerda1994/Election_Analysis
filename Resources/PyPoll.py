# import datetime as dt
# now=dt.datetime.now()

# print('the time irght now is',now)


# import csv


# file_to_load='Resources/election_results.csv'

# election_data = open(file_to_load, 'r') #---->open and close
# election_data.close()


# with open(file_to_load) as election_data:
#     print(election_data)
    
    
# import os
# dir(os)
# print(dir(os.path))

# #CHAINING
# import csv
# import os

# file_to_load=os.path.join('Resources','election_results.csv') #----> read a file
# with open(file_to_load) as election_data:
#     print(election_data)


# # file_to_save=os.path.join('analysis','election_analysis.txt')  #---->create a file in a folder
# # open(file_to_save,'w')

# file_to_save=os.path.join('analysis','election_analysis.txt')  #---->create a file in a folder AND WRITE
# outfile=open(file_to_save,'w')
# outfile.write('hello world')
# outfile.close()

# #or (CLEANER)

# file_to_save=os.path.join('analysis','election_analysis.txt')
# with open(file_to_save,'w') as txt_file:
#     txt_file.write("Arapahoe\nDenver\nJefferson")


#REDA THE ELECTION RESULTS:#####

import csv
import os
file_to_load=os.path.join("Resources","election_results.csv")
file_to_save=os.path.join("analysis",'election_analysis.txt')

#get the total votes
total_votes=0

#get candidate options
candidate_options=[]

#declare empty dict to get the tot votes from each candid
candidate_votes={}

#detrmine the winning candidate
#winning candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percentage=0



with open(file_to_load) as election_data:
    #to do:read and analyze the data here
    file_reader=csv.reader(election_data)
    
    
    headers=next(file_reader)
    print(headers)
    
    for row in file_reader:
        #print(row)
        #add to the total vote count
        total_votes+=1
    
        #print the candidate name from each row
        candidate_name=row[2]
    
        #add the candidate name to the candidate list
        #candidate_options.append(candidate_name)
        
        if candidate_name  not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            
            #begin tracking the candidates vote count
            candidate_votes[candidate_name]=0
            
        #add a vote to that candidates count
        candidate_votes[candidate_name]+=1
        
with open(file_to_save,'w') as txt_file: #--->end
    
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results) #--->end
    
            
        
    #print(total_votes)
    #print(candidate_votes)



    #detrmine the percentage of votes for each candidate
    #iterate through the cand list
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes=candidate_votes[candidate_name]
        vote_percentage=float(votes)/float(total_votes)*100
        #print(f"{candidate_name}: received {vote_percentage}% of the vote")
        
        #to do:print out each candidates name, vote count, and %
        #Determine winning vote count and candidate
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate_name
            
    #print out each candidate name, vote count and perc:
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)#-->end
        
        
            
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary) #--->end
            





        
    

    
