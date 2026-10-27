# emp_id = input("Enter the Number :")

# while emp_id !="-1":
#     trade = int(input("Enter the Amount :"))
#     profit_lose = 0
#     while trade!= 0:
#         profit_lose = profit_lose + trade
#         trade = int(input("Enter the Amount"))
        
#     print(profit_lose)
#     emp_id = input("Enter the number :")
    
for i in range(1, 5):
    
    emp_id = input("Enter Employee ID: ")

    profit = 0

    trade = int(input("Enter Amount (0 to stop): "))

    while trade != 0:
        profit = profit + trade
        trade = int(input("Enter Amount (0 to stop): "))

    print("Employee ID:", emp_id)
    print("Total Profit:", profit)
    print()