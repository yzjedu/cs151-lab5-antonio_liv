# Algorithm Document

1. Output explanation of program to user.
2. set initial balance to 1000
3. create variable "choice", set it to "t"
4. Set sentinel to "e"
5. while choice is not equal to sentinel: 
   2. Prompt user to either view balance, deposit, withdraw, or exit.
   3. while user input not in view, balance, deposit, withdraw or exit
      4. output prompt asking user to enter valid input
   3. If user enters "view balance":
      4. Output current balance 
      5. If balance is < 0:
         6. Output "You balance is less than 0. You will be charged 5% interest. "
   4. Otherwise-If user enters to deposit:
      5. Prompt user to input number of money they want to deposit
      6. if user enters negative number for number of money deposited or invalid character:
         7. output "Invalid. Please enter positive value."
      6. Add number of deposited money to balance
   7. Otherwise-If user enters to withdraw:
      8. Prompt user to input number of money they want to withdraw
      9. if user enters negative number for number of money withdrawn or invalid character:
         7. output "Invalid. Please enter positive value."
      9. Subtract number of withdrawn money to balance.
   11. Otherwise-If user enters "e":
       12. set choice to "e" 
13. Program ends
