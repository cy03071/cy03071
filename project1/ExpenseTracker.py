print("""
Personal Expense Tracker
      1.Add Transaction
      2.Edit Transaction
      3.Delect Transaction
      4.View Summary
      5.Save and Exit
""")
import pandas as pd
date = {
      'date': [],  
    'category': [],                 
    'amount': [] ,
    'type': []
     

}
choice = input("Enter your choice: ")
while choice != "5":
    if choice == "1":
          print("""

""")
          choice = input("Enter your choice: ")
    elif choice == "2":
          print("Edit Transaction")
          print("""
Personal Expense Tracker
      1.Add Transaction
      2.Edit Transaction
      3.Delect Transaction
      4.View Summary
      5.Save and Exit
""")
          choice = input("Enter your choice: ")
    elif choice == "3":
          print("Delect Transaction")
          print("""
Personal Expense Tracker
      1.Add Transaction
      2.Edit Transaction
      3.Delect Transaction
      4.View Summary
      5.Save and Exit
""")
          choice = input("Enter your choice: ")
    elif choice == "4":
          print("View Summary")
          print("""
Personal Expense Tracker
      1.Add Transaction
      2.Edit Transaction
      3.Delect Transaction
      4.View Summary
      5.Save and Exit
""")
          choice = input("Enter your choice: ")
else:
     print("Save and exit")


import pandas as pd
df = pd.DataFrame()






     



        
        
      