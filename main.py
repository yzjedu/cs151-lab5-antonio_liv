# Programmers: Antonio Dueno, Liv Oakes
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 10/16/24
# Lab Assignment: 5
# Problem Statement: Build a simulation of an ATM where the user can check their balance, withdraw money, and deposit money.
# Data In: user input if they wish to withdraw, how much they wish to withdraw, deposit, how much they wish to deposit,
#          view balance, or exit ATM.
# Data Out: Total account balance after depositing, total account balance after withdrawing, total account balance
# Credits:In class
from operator import truediv

#output for explanation of program
print('Hello! Welcome to the ATM simulator! This program is intended to function like a real ATM. \nYou can view your '
      'current balance, deposit money, withdraw money, or exit the program.')

#variables set before while loop
balance = 1000
choice = 't'
sentinel = 'e'

#outer while loop for ATM sumilator
while choice != sentinel:
    #output for asking user what they wish to do
    print('Would you like to view balance (v), deposit (d), withdraw (w), or exit (e)? ')
    atm = input('Input choice here: ').lower()

    #while loop for ig user does not enter valid option
    while atm != 'e' and atm != 'd' and atm != 'w' and atm != 'v':
        print ('Please enter a valid option')
        atm = input('Input choice here: ').lower()

    #if user wants to view balance
    if atm == 'v':
        print('Your balance is:', balance)
        if balance <= 0:
            print('Your balance is less than 0. You will be charged 5% interest.')

    #if user wants to deposit money
    elif atm == 'd':

        #while loop for if user does not enter a positive number, does not enter a digit, or enters nothing.
        while True:
            deposit_money = input('Input number of money you would like to deposit: ')
            try:
                deposit_money = int(deposit_money)
                if deposit_money <= 0:
                    print('Money deposited must be greater than 0.')
                else:
                    balance += deposit_money
                    print('Your balance is:', balance)
                    break
            except ValueError:
                print('Please enter a number.')

    #if user wants to withdraw money
    elif atm == 'w':

        #while loop for if user does not enter a positive number, does not enter a digit, or enters nothing.
        while True:
            withdraw_money = input('Input number of money you would like to withdraw: ')
            try:
                withdraw_money = int(withdraw_money)
                if withdraw_money <= 0:
                    print('Money withdrawn must be greater than 0.')
                else:
                    balance -= withdraw_money
                    print('Your balance is:', balance)
                    break
            except ValueError:
                print('Please enter a number.')


    #if user wants to exit program
    elif atm == 'e':
        print('Thank you for using the ATM.')
        choice = 'e'
