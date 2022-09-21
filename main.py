import datetime
import sys
from Processor import *
from Account import *
from datetime import *

# Define variables
first_day = datetime.today()
next_week_date = first_day + timedelta(days=6)
transactions = []
system_account = Account('SYSTEM_DEFAULT' ,sys.maxsize)
AMOUNT = 50000
TWELVE = 12

#Creates processor instance
processor = Processor(transactions)


def perform_advance(dst_account,amount):
    week = 0
    account = Account(dst_account,amount)
    direction = input("Credit or Debit? ")
    if direction != "Credit" and direction != "Debit":
        raise ValueError("Please try to run the program again without typos")
        quit(1)
    else:
        processor.perform_transaction(system_account,dst_account,amount,direction)

        while week <= 12:
            if next_week_date == datetime.today():
                # Testing if the transaction is valid, if not ,the debit will be attached to the week after the last
                # week payment by not incrementing the successful week payment
                if processor.check_if_valid():
                    twelveth_of_the_amount = amount/TWELVE
                    processor.perform_transaction(account,system_account,twelveth_of_the_amount,direction)
                    week = week + 1


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
#     processor.perform_transaction(account1,account2,AMOUNT,'direct')
#
#
# #Testing The Download Report....
# #Please notice the excel sheet that created in the directory folder.
# processor.download_report()
#
#
# #Testing the perform_advance function
# perform_advance(account1,amount1)
#################################################### TESTING ZONE ####################################################


