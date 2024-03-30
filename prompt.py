pr = '''
JUST RETURN A CSV FORMATTED DATA 
You will be given a single message that will be a bank statement, 
Please extract the following useful data from the provided message and return them as a CSV Value:

1. For each message, identify and extract only useful information, for example:
    anount received, phone number, reason for transaction, current balance, airtime
2. Ensure that the extracted amounts are represented as real numerical values, such as 12000 instead of "12,000".

Example message:
"You have received 3000 from 09006700. Reason: J. Your balance is 170000."

you should output exactly and only this =>  3000, 09006700, J., 170000;
like wise adapt for different types of datas
'''