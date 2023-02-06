# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_months = 0

extra_payment_start_month = 61
extra_payment_end_month = 109
extra_payment = 1000

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

    if extra_payment_start_month < total_months < extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    total_months += 1

    print(total_months, ' ', total_paid,' ',principal)

#print('Total paid', total_paid, ' ', total_months)
