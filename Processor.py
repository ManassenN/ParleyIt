import random
from datetime import *
import pandas as pd

class Processor():
    # Class constructor , initialize a transaction database (later export it to Excel sheet)
    def __init__(self,transactions):
        self.transactions_list = transactions


    #This function simulates a demo testing transaction , its assumes that 8/10 of every 10 transactions is successful
    def check_if_valid(self):
        num = random.randint(0, 11)
        if num >= 2:
            return 1

    def perform_transaction(self,src_bank_account,dst_bank_account,amount,direction):
        # Generates a random number between 0 - 10
        transaction_id = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, 10)])

        #Creates a new transaction
        new_transaction = {
            "src_bank_account":src_bank_account,
            "dst_bank_account":dst_bank_account,
            "amount": amount,
            "direction": direction,
            "transaction_id": transaction_id,
            "day": datetime.now().strftime("%d"),
            "month": datetime.now().strftime("%m"),
            "year": datetime.now().strftime("%Y"),
            "status":'UNKNOWN'
        }
        #Checking if the transaction is valid!
        if self.check_if_valid():
            src_bank_account.balance = src_bank_account.balance - amount
            dst_bank_account.balance = dst_bank_account.balance + amount
            new_transaction['status'] = "success"
        else:
            new_transaction['status'] = "fail"

        #Append the new transaction to the transaction list
        self.transactions_list.append(new_transaction)
        return transaction_id


    # downloads the transactions info report from the last 5 days
    def download_report(self):
        today_day_date =int(datetime.now().strftime("%d"))
        valid_transactions = []
        for transaction in self.transactions_list:
            if int(transaction["day"]) - today_day_date <=5 and int(transaction["day"]) - today_day_date >= 0:
                valid_transactions.append(transaction)
        df = pd.DataFrame(valid_transactions)
        df.to_excel('output.xlsx')

