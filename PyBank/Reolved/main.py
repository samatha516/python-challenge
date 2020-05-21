# Modules
import os
import csv

# Set path for budget file
budget_file_path = os.path.join("..", "Resources", "budget_data.csv")

months = []				# months present in the dataset
revenue = []			# profit/loss values in the dataset
revenue_change = [] 	# difference in the profit/loss between each month
	
total_months = 0		# total number of months in the dataset
total_profit_loss = 0 	# overall totoal amount of profit_loss 
average_change = 0		# overall average change 
max_profit = 0			# maximum dollar amount profit in the entire period
max_loss = 0			# maximum dollar amount loss in the entire period

# Open the CSV
with open(budget_file_path) as budget_file:
	budget_reader = csv.reader(budget_file, delimiter=",")	
	#skip the header
	budget_header = next(budget_reader)
	
	#loop through the file to get to the solution
	for row in budget_reader:
		#grab all the months into months list
		months.append(row[0])

		#grab all the profit/loss values into revenue list and cast it to int.
		revenue.append(int(row[1]))
		
# The total number of months included in the dataset
total_months = len(months)

# The net total amount of "Profit/Losses" over the entire period
total_profit_loss = sum(revenue)

for i in range(len(revenue) - 1):
	profit_loss = revenue[i+1] - revenue[i]
	revenue_change.append(profit_loss)

# The average of the changes in "Profit/Losses" over the entire period
average_change = round(sum(revenue_change)/len(revenue_change),2)

# The greatest increase in profits (date and amount) over the entire period
max_profit = max(revenue_change)
max_profit_month = months[revenue_change.index(max_profit)+1]

# The greatest decrease in losses (date and amount) over the entire period
max_loss = min(revenue_change)
max_loss_month = months[revenue_change.index(max_loss)+1]	

#Print Statements

print('Financial Analysis')
print('------------------------------------------------'+'\n')
print("Total Months: " + str(total_months))
print("Total: $ " + str(total_profit_loss))      
print("Average Change: $ " + str(average_change))
print(f"Greatest Increase in Profits: {max_profit_month} (${max_profit})")
print(f"Greatest Decrease in Profits: {max_loss_month} (${max_loss})")	

with open("financial_analysis.txt", 'w') as text:
	text.write("Financial Analysis"+ "\n")
	text.write("--------------------------------------------------\n\n")
	text.write("Total Months: " + str(total_months) + "\n")
	text.write("Total: $" + str(total_profit_loss) + "\n")
	text.write("Average Change: $" + str(average_change) + "\n")
	text.write(f"Greatest Increase in Profits: {max_profit_month} (${max_profit}) \n")
	text.write(f"Greatest Decrease in Profits: {max_loss_month} (${max_loss})")	