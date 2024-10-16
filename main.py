# Programmers:
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 10//24
# Lab Assignment: 5
# Problem Statement:
# Data In:
# Data Out:
# Credits:In class
print('Welcome to the ATM')
balance = 1000
choice = 't'
sentinel = 'e'
while choice != sentinel:
    atm = input('Would you like to view your balance (b), deposit (d), withdraw (w), or exit (e)? ').lower()
    if atm == 'b':
        print(balance)
        if balance < 0 or balance != int:
            print('Your balance is less than 0. You will be charged 5% interest.')
    elif atm == 'd':
        deposit_money = int(input('How much money would you like to deposit? '))
        if deposit_money < 0:
            print('Invalid. Please enter a positive number.')
        balance = balance + deposit_money
        print(f'Your balance is {balance}')
    elif atm == 'w':
        withdraw_money = int(input('How much money would you like to withdraw? '))
        if withdraw_money < 0:
            print('Invalid. Please enter a positive number.')
        balance = balance - withdraw_money
        print(f'Your balance is {balance}')
    elif atm == 'e':
        choice = 'e'
