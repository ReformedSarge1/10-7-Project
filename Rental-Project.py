
#import random


#class rental():
    #def __init__(self):
        #self.income = 16.0
        #self.cash = 1500
        #self.investment = 3000
        #self.entire_investment = 24000


    #def income(self):
        #self.income = random * int
    #if income == 'y':
            #print("this is your income this year")                               
            #investment = round(random*int(70, 12.00), 2)
            #entire_investment = ("ROI")
    #ROI = (1500 * 16.0)
    #print(ROI)
    
   
# class ROI(): 
#     def __init__(self, ):
#         self.total_monthly_income = 0
#         self.total_monthly_expenses = 0
#         self.total_monthly_cash_flow = 0
#         self.total_annual_cash_flow = 0
#         self.total_investment = 0
#         self.return_on_investment = 0
    

#     def income(self):
#         self.rental_income = int(input('What is your rental income?'))
#         if self.rental_income >= 0:
#             print(f"Your monthly rental income is {self.rental_income}")
#         else:
#             print("Invalid input, please try again.")
#         self.total_monthly_income = self.rental_income
#         print(f"The total monthly income is {self.total_monthly_income}")
#     def expenses(self):
#         self.electric = int(input('How much is your electricity?'))
#         if self.electric >= 0:
#             print(f"Your monthly electric is {self.electric}")
#         else:
#             print("Invalid input, please try again.")
#         self.total_monthly_expenses = self.electric
#         print(f"The total monthly expense is {self.total_monthly_expenses}")
#     def cashflow(self):
#         self.total_monthly_cash_flow = self.total_monthly_income - self.total_monthly_expenses
#         print(f"The total monthly cash flow is {self.total_monthly_cash_flow}")

#         self.total_annual_cash_flow = self.total_monthly_cash_flow * 12
#         print(f"The total annual cash flow is {self.total_annual_cash_flow}")
#     def investment(self):
#         self.down_payment = int(input('How much is your down payment?'))
#         if self.down_payment >= 0:  
#              print(f"Your down payment is {self.down_payment}")
#         else:
#             print("Invalid input, please try again.")
#         self.total_investment = self.down_payment
#         print(f"Your total investment is {self.total_investment}")

#         self.return_on_investment = self.total_annual_cash_flow / self.total_investment
#         print(f"The ROI is {self.return_on_investment} %")
#     def UserInput(self):
#         while True:
#             response = (input("Would you like to calculate your ROI? yes, no")).lower()
#             if response == "yes":
#                 self.income()
#                 self.expenses()
#                 self.cashflow()
#                 self.investment()
#             elif response == "no":
#                 print("Goodbye.")
#                 break
#             else:
#                 print("Invalid input, please try again.")

Total = 355000
Payments = 2475
Expenses = 1250

def ROI(Total, Payments, Expenses):
    profit = Payments * 12 - Expenses
    ROI = (profit/Total)*100
    print(ROI)

ROI(Total, Payments, Expenses)