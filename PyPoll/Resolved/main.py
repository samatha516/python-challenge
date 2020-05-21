# Modules
import os
import csv

# Set path for election file
election_path = os.path.join("..", "Resources", "election_data.csv")

votes_grand_total = 0		# total number of votes for all the candidates
candidates = []				# individual candidate names
all_votes = []				# all the votes that the election got
candidate_vote_count = []	# votes each candidate got
candidate_vote_percent = []	# votes percent per individual candidate
winner = ''

# Open the CSV
with open(election_path) as election_data:
	election_reader = csv.reader(election_data, delimiter=",")	
	#skip the header
	next(election_reader)	

	for row in election_reader:			
		# list of all the votes
		all_votes.append(row[2])

# Total number of votes in the election
votes_grand_total = len(all_votes)	

# create a list of individual candidates
candidates = list(set(all_votes))
#print(candidates)

# count individual vote count and percent
for candidate in candidates:
	candidate_vote_count.append(all_votes.count(candidate))
	candidate_vote_percent.append(round(all_votes.count(candidate)/votes_grand_total * 100,3))

# declare the winner based on the max individual vote count
winner = candidates[candidate_vote_count.index(max(candidate_vote_count))]

print('Election Results')
print('---------------------------')
print(f"Total Votes: {votes_grand_total}" )
print('---------------------------')
for i in range(len(candidates)):
	print(f"{candidates[i]}: {candidate_vote_percent[i]}% ({candidate_vote_count[i]})")
print('---------------------------')
print(f"Winner: {winner}")
print('---------------------------')
	
with open("pypoll_end_result.txt", 'w') as text:
	text.write('Election Results \n')
	text.write('--------------------------- \n')
	text.write(f'Total Votes: {votes_grand_total} \n')
	text.write('--------------------------- \n')
	for i in range(len(candidates)):
		text.write(f"{candidates[i]}: {candidate_vote_percent[i]}% ({candidate_vote_count[i]})\n")
	text.write('--------------------------- \n')
	text.write(f"Winner: {winner} \n")
	text.write('---------------------------')		