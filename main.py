# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

quantity=int(input("Enter the amount of quantity:"))
total_cost=quantity*100

if total_cost>1000:
  discount=total_cost*10/100
  total_cost=total_cost-discount
  print("Your payable amount is:",total_cost)

else:
  print("Your payable amount is:",total_cost)

