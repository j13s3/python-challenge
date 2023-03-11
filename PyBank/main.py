# Module 3 - Python Challenge - PyBank Analysis - Jalaj Sharma

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
total_profit_loss_change = 0

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
        
        # Perform the computations below after the first month so that changes in profit/loss can be captured
        if (total_months > 1):

            # Capture the profit/loss change from the previous month
            profit_loss_change = int(row[1]) - prev_profit_loss

            # Totalise the change in profit/loss
            total_profit_loss_change = total_profit_loss_change + profit_loss_change

            # Use IF statements to evaluate the minimum and maximum along with the corresponding month instead of using the in-built min/max functions. This way is preferred as it simplifies finding the corresponding month as the data is evaluated row by row and creating a new appended list is not required
            if (profit_loss_change) > profit_grt_inc_money:
                profit_grt_inc_money = profit_loss_change
                profit_grt_inc_month = row[0]
            
            if (profit_loss_change) < profit_grt_dec_money:
                profit_grt_dec_money = profit_loss_change
                profit_grt_dec_month = row[0]
        
        prev_profit_loss = int(row[1])

# With all the data collected from the raw data file, calculate the average profit/loss
avg_chng = round((total_profit_loss_change / (total_months - 1)), 2)

# Print the data to the terminal
print("\nFinancial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_money}")
print(f"Average Change: {avg_chng}")
print(f"Greatest Increase in Profits: {profit_grt_inc_month} (${profit_grt_inc_money})")
print(f"Greatest Decrease in Profits: {profit_grt_dec_month} (${profit_grt_dec_money})")

# Open/create the file usng the file path and write into the file
with open(text_output_path, "w") as output_text:
    # Use the .write instruction for writing text into the file
    output_text.write("Financial Analysis")
    output_text.write("\n----------------------------")
    output_text.write(f"\nTotal Months: {total_months}")
    output_text.write(f"\nTotal: {total_money}")
    output_text.write(f"\nAverage Change: {avg_chng}")
    output_text.write(f"\nGreatest Increase in Profits: {profit_grt_inc_month} (${profit_grt_inc_money})")
    output_text.write(f"\nGreatest Decrease in Profits: {profit_grt_dec_month} (${profit_grt_dec_money})")