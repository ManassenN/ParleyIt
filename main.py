import datetime
import sys
from Processor import *
from Account import *
from datetime import *

# Define variables
# I assumed that the system itself has a bank account, for managing all the accounts debits.
  
first_day = datetime.today()
transactions = []
system_account = Account('SYSTEM_DEFAULT' ,sys.maxsize)
# Random amount
AMOUNT = 50000
#Constant
TWELVE = 12

#Creates processor instance
processor = Processor(transactions)


def perform_advance(dst_account,amount):
    week = 0
    processor.perform_transaction(system_account,dst_account,amount,'Credit')
    next_day_date = first_day + timedelta(days=1)
    next_week_date = first_day + timedelta(days=6)

    while week <= 12:
        if next_day_date == datetime.today():
            if next_week_date == datetime.today():
                    # Testing if the transaction is valid, if not ,the debit will be attached to the week after the last
                    # week payment by not incrementing the successful week payment
                if processor.check_if_valid():
                    twelveth_of_the_amount = amount/TWELVE
                    processor.perform_transaction(dst_account,system_account,twelveth_of_the_amount,"Debit")
                    week = week + 1

            #Download daily report
            processor.download_report()
            next_day_date = datetime.today() + timedelta(days=1)

#################################################### TESTING ZONE ####################################################

# Testing The Processor Functionality....
# for _ in range(0,5):
#     num1 = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, 10)])
#     num2 = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, 10)])
#
#     amount1 = int(''.join(["{}".format(random.randint(0, 9)) for num in range(0, 4)]))
#     amount2 = int(''.join(["{}".format(random.randint(0, 9)) for num in range(0, 4)]))
#     account1 = Account(num1,amount1)
#     account2 = Account(num1, amount2)
#
#     processor.perform_transaction(account1,account2,AMOUNT,'Debit')
#
#
# #Testing The Download Report....
# #Please notice the excel sheet that created in the directory folder.
# processor.download_report()


#Testing the perform_advance function
# perform_advance(account1,amount1)
#################################################### TESTING ZONE ####################################################


