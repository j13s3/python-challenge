# Module 3 - Python Challenge - PyBank Analysis

# Importing python modules
import csv
import os

# Declaring the file path for the raw data input
budget_data_path = os.path.join("Resources", "budget_data.csv")
# Declaring the file path for the analysis text output
text_output_path = os.path.join("analysis", "text_output.txt")

# Initialising variables for calculations
total_months = 0
total_money = 0
profit_grt_inc_money = 0
profit_grt_dec_money = 0

# List for recording the monthly profits/losses
monthly_profits = []

# Open the file usng the file path and read the data by setting ',' as the delimiter
with open(budget_data_path) as input_data:
    read_data = csv.reader(input_data, delimiter=',')        

    # Record the header and move onto the next row/line
    read_data_header = next(read_data)

    # With the header out of the way, start reading one row at a time
    for row in read_data:

        # Increment the number of months counter
        total_months = total_months + 1

        # Aggregate the total amount of money
        total_money = total_money + int(row[1])

        # Populate the list with the montly profits/losses
        monthly_profits.append(int(row[1]))

        # Use IF statements to evaluate the minimum and maximum along with the corresponding month
        if ((int(row[1])) > profit_grt_inc_money):
            profit_grt_inc_money = int(row[1])
            profit_grt_inc_month = row[0]
        
        if ((int(row[1])) < profit_grt_dec_money):
            profit_grt_dec_money = int(row[1])
            profit_grt_dec_month = row[0]
    
    # Always good to close a file once done with it
    input_data.close()

# With all the data collected from the raw data file, calculate the average profit/loss
avg_chng = round((total_money / total_months), 2)

# Print the data to the terminal
print("\nFinancial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_money}")
print(f"Average Change: {avg_chng}")
print(f"Greatest Greatest Increase in Profits: {profit_grt_inc_month} (${profit_grt_inc_money})")
print(f"Greatest Greatest Increase in Profits: {profit_grt_dec_month} (${profit_grt_dec_money})")

# Open/create the file usng the file path and write into the file
with open(text_output_path, "w") as output_text:
    # Use the .write instruction for writing text into the file
    output_text.write("Financial Analysis")
    output_text.write("\n----------------------------")
    output_text.write(f"\nTotal Months: {total_months}")
    output_text.write(f"\nTotal: {total_money}")
    output_text.write(f"\nAverage Change: {avg_chng}")
    output_text.write(f"\nGreatest Greatest Increase in Profits: {profit_grt_inc_month} (${profit_grt_inc_money})")
    output_text.write(f"\nGreatest Greatest Increase in Profits: {profit_grt_dec_month} (${profit_grt_dec_money})")

    # Always good to close a file once done with it
    output_text.close()