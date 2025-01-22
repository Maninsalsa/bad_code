# 
# Question 1

for i in range(1, 5):
    print(i, end=" ")

# the answer is B. when two integers are passed as arguments with range, the first number
# represents the starting number, and the second number represents the stop number
# (not included or stop -1)

# therefore the loop starts at integer 1 and stops at 4. 

# Question 2 

# n = 1
# while ______:
#     print(n)
#     n += 1

# Answer: while n <= 5. this will increment n as long as n <= 5 once n reaches 5 after it's
# printed, it's value will no longer satisfy the requirements of n<=5


# Question 3

# how many hello's will be printed?

for i in range(2):
    for j in range(3):
        print("Hello")

# Answer: for each outer loop there are three iterations. Since there are two outer loops,
# and 3 innerloop iterations each, hello will print 6 times. 

# outer loop i = 0 -> inner loop executes for range 0, 1, and 2 (which is stop number - 1 based on the syntax)
# outer loop i = 1 -> inner loop exectures again for ranges, 0, 1, and 2.

# therefore there are 6 hellos printed

# Question 4

for i in range(1, 6):
    if i == 4:
        break
    print(i)
# the boolean conditional stops at 3 since the loop will iterate through all numbers from 1 to stop-1

# Question 5

# answer
for i in range(1,11):
    if i % 2 == 0: # translation: if the reaminder of i/2 == 0, which can only happen when i is even, skip and continue to the next iteration.
        continue 
    print(i) 

# Bonus
# in most cases, because the list is finite and orderd, it means the amount of iterations are predetermined, therefore a for loop would be best to access in most cases.
# one scenario of which using a while loop would be a scenario where a specific condition within the list changes, but the time of which that even happens is unknown.
# for example if you assigned random integer values to each number on a list and you were trying to make a scenario where the addition of two of values from that list  == that specific value
# 

"""
=== Level 2 ===

Tasks
	1.	Filter High Performers:
	•	Extract all sales numbers that are greater than or equal to 100 using a list comprehension.
	2.	Calculate Statistics:
	•	Use a custom function to calculate and return the average sales.
	•	Use a built-in function to find the maximum sales.
	•	Use another custom function to find the percentage of days that had sales greater than or equal to 100.
	3.	Identify Weekly Trends:
	•	Assume the list represents sales for 30 days. Slice it into weekly chunks (7 days each, with the last chunk containing the remaining 2 days).
	•	Use a loop to calculate the sum of sales for each week.
	4.	Top N Days:
	•	Create a function that accepts the sales list and an integer N.
	•	It should return the top N sales days, sorted in descending order.


"""

daily_sales = [120, 95, 70, 150, 200, 50, 90, 180, 40, 300, 120, 70, 60, 100, 
               110, 130, 45, 80, 170, 90, 60, 75, 200, 180, 90, 100, 110, 130, 
               150, 50]


# class SalesReport:

#     def filter_performers(dailysaleslist: list) -> list:
#         """Returns a list of all sales values >= 100"""
#         return [i for i in dailysaleslist if i >= 100]

#     def average_sales(dailysaleslist: list) -> float:
#         """Calculates and returns the average of all sales values"""
#         sum = 0
#         length = len(dailysaleslist)
#         for i in dailysaleslist:
#             sum += i
#         sales_average = sum/length
#         return float(sales_average)

#     def average_performance_percentage(dailysaleslist, filtered_performers: list)-> float:
#         """Calculates the percentage of days that had sales >= 100"""
#         total_sales_days = 0
#         filtered_days = 0

#         for i, v in enumerate(dailysaleslist):
#             if v >= 100:
#                 total_sales_days += i

#         for i in filtered_performers:
#             filtered_days += int(i)

#         average_performance_percentage = filtered_days/total_sales_days
#         return average_performance_percentage

#     def trend_slicer(dailysaleslist: list) -> list:
#         """Splits the sales data into weekly chunks of 7 days each"""
#         chunks = []
        
#         for i in range(0, len(dailysaleslist), 7):
#             chunk = dailysaleslist[i:i + 7]
#             chunks.append(chunk)
        
#         return chunks

#     def top_n_sales(dailysaleslist: list, n=10) -> list:
#         """Returns the top N highest sales days in descending order"""
#         sorted_daily_sales = sorted(dailysaleslist, reverse=True)
#         return [v for i, v in enumerate(sorted_daily_sales) if i < n]
    
#     def full_report(self, dailysaleslist: list) -> None:
#         """Generates a complete sales report with all metrics"""
#         # Get user input for top N days
#         n = int(input("Enter number of top sales days to show: "))
        
#         # Calculate all metrics
#         high_performers = self.filter_performers(dailysaleslist)
#         avg_sales = self.average_sales(dailysaleslist)
#         perf_percentage = self.average_performance_percentage(dailysaleslist, high_performers)
#         weekly_chunks = self.trend_slicer(dailysaleslist)
#         top_sales = self.top_n_sales(dailysaleslist, n)
        
#         # Print full report
#         print(f"\nSales Report")
#         print("-" * 50)
#         print(f"High performing sales days (>= 100): {high_performers}")
#         print(f"Average daily sales: ${avg_sales:.2f}")
#         print(f"Percentage of high performing days: {perf_percentage:.1%}")
        
#         print("\nWeekly sales breakdown:")
#         for i, week in enumerate(weekly_chunks, 1):
#             print(f"Week {i}: {week}")
            
#         print(f"\nTop {n} sales days: {top_sales}")

# # Get high performing sales (>= 100)
# answer1 = SalesReport.filter_performers(daily_sales)
# print(f"High performing sales days (>= 100): {answer1}")

# # Calculate average sales across all days
# answer2 = SalesReport.average_sales(daily_sales)    
# print(f"Average daily sales: ${answer2:.2f}")

# # Calculate percentage of high performing days
# answer3 = SalesReport.average_performance_percentage(daily_sales, answer1)
# print(f"Percentage of high performing days: {answer3:.1%}")

# # Get weekly sales chunks
# answer4 = SalesReport.trend_slicer(daily_sales)
# print("Weekly sales breakdown:")
# for i, week in enumerate(answer4, 1):
#     print(f"Week {i}: {week}")

# # Get top 5 sales days
# answer5 = SalesReport.top_n_sales(daily_sales, 5)
# print(f"Top 5 sales days: {answer5}")

# # Ge the full report
# bonus = SalesReport()
# bonus.full_report(daily_sales)

# Corrected 
class SalesReport:

    @staticmethod
    def filter_performers(dailysaleslist: list) -> list:
        """Returns a list of all sales values >= 100"""
        return [i for i in dailysaleslist if i >= 100]

    @staticmethod
    def average_sales(dailysaleslist: list) -> float:
        """Calculates and returns the average of all sales values"""
        total_sum = sum(dailysaleslist)
        length = len(dailysaleslist)
        return total_sum / length

    @staticmethod
    def average_performance_percentage(dailysaleslist: list, filtered_performers: list) -> float:
        """Calculates the percentage of days that had sales >= 100"""
        total_days = len(dailysaleslist)
        filtered_days = len(filtered_performers)
        return (filtered_days / total_days) * 100

    @staticmethod
    def trend_slicer(dailysaleslist: list) -> list:
        """Splits the sales data into weekly chunks of 7 days each"""
        return [dailysaleslist[i:i + 7] for i in range(0, len(dailysaleslist), 7)]

    @staticmethod
    def top_n_sales(dailysaleslist: list, n=10) -> list:
        """Returns the top N highest sales days in descending order"""
        return sorted(dailysaleslist, reverse=True)[:n]

    def full_report(self, dailysaleslist: list) -> None:
        """Generates a complete sales report with all metrics"""
        # Get user input for top N days
        n = int(input("Enter number of top sales days to show: "))
        
        # Calculate all metrics
        high_performers = self.filter_performers(dailysaleslist)
        avg_sales = self.average_sales(dailysaleslist)
        perf_percentage = self.average_performance_percentage(dailysaleslist, high_performers)
        weekly_chunks = self.trend_slicer(dailysaleslist)
        top_sales = self.top_n_sales(dailysaleslist, n)
        
        # Print full report
        print(f"\nSales Report")
        print("-" * 50)
        print(f"High performing sales days (>= 100): {high_performers}")
        print(f"Average daily sales: ${avg_sales:.2f}")
        print(f"Percentage of high performing days: {perf_percentage:.1f}%")
        
        print("\nWeekly sales breakdown:")
        for i, week in enumerate(weekly_chunks, 1):
            print(f"Week {i}: {week}")
            
        print(f"\nTop {n} sales days: {top_sales}")

"""
Issues and Fixes
	1.	filter_performers and other methods are not class methods:
	•	The methods need the @staticmethod decorator or the self parameter for proper usage in a class.
	•	Your full_report method calls the class methods as instance methods (self.filter_performers), but they aren’t instance methods.
	•	Fix: Add @staticmethod to methods or convert them to instance methods by including self in their definitions.

2.	average_performance_percentage logic:
	•	The way total_sales_days and filtered_days are being calculated seems incorrect.
	•	total_sales_days should be the total count of days (len(dailysaleslist)), and filtered_days should be the count of days with sales >= 100.
	•	The percentage is then (filtered_days / total_sales_days) * 100.

3.	top_n_sales logic:
	•	It works, but the list comprehension is unnecessary. The sorted() function already gives you the required result when sliced.

4.	General readability:
	•	Some variable names (sum) shadow Python’s built-in functions. Use alternatives like total_sum or total.
"""