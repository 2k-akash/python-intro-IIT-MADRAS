ram_bank_balance=100000
#as it is a bank balance,it should be positive
ram_loan=500000
#it should be returned ,so it must negative
lakshman_bank_balance=2000000

lakshman_loan=10000000
net_income=ram_bank_balance+lakshman_bank_balance
#income of two brothers
net_liability=ram_loan+lakshman_loan
#loan of two brothers
final_value=net_income-net_liability
#it may be negative
print(final_value)
