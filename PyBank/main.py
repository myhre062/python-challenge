# import OS module
import os

# Module for reading CSV files
import csv

# Define file paths
csv_resource_path = os.path.join('PyBank','Resources','budget_data.csv') #'/Users/ezrellemyhre-hager/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv'
txt_analysis_path = os.path.join('PyBank','analysis','financial_analysis.txt') #'/Users/ezrellemyhre-hager/Documents/GitHub/python-challenge/PyBank/analysis/financial_analysis.txt'

# Initialize variables
total_months = 0
total_revenue = 0
dates = []
revenue = []
changes_per_month = [] # List to store the changes in revenue per month
dates_tracker = [] # List to track the corresponding dates for the changes

# Function to calculate the average change in revenue
def calculate_average_change(revenue):

    for i in range(len(revenue)-1):
        changes_per_month.append(revenue[i+1] - revenue[i])
        # Keep track of that dates as you record the changes
        dates_tracker.append(dates[i+1])

    return sum(changes_per_month) / len(changes_per_month)

# Open the CSV file
with open(csv_resource_path) as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter = ',')

    # Skip the header row 
    next(csv_reader)
    
    # Read each row of data after the header
    for row in csv_reader:        
        # add to the list of dates
        dates.append(row[0])

        # add to the list of revenue
        revenue.append(int(row[1]))

# Calculate total months and total revenue
total_months = len(dates)
total_revenue = sum(revenue)

# Calculate average change using the defined function
average_change = round(calculate_average_change(revenue), 2)

# Find the greatest increase and decrease in revenue
greatest_increase = max(changes_per_month)
greatest_decrease = min(changes_per_month)
greatest_increase_date = dates_tracker[changes_per_month.index(greatest_increase)]
greatest_decrease_date = dates_tracker[changes_per_month.index(greatest_decrease)]

# Write the analysis results to a text file
with open(txt_analysis_path, 'w', newline='') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_revenue}\n")
    txt_file.write(f"Average Change: ${average_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

# Print results to the terminal
print("")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
print("")
