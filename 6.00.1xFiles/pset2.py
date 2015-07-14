# -*- coding: utf-8 -*-

## Problem Set 2 
# PROBLEM 1: PAYING THE MINIMUM

# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


# Variables
#balance = 4842
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

def payingTheMinimum(balance, annualInterestRate, monthlyPaymentRate):
    total = 0
    for month in range (1,13):    
        payment = monthlyPaymentRate * balance # Amount to pay each month depending on balance and rate.
        total += payment
        balance = (balance - payment) * (1 + annualInterestRate / 12.0)    
        print "Month: ", month
        print "Minimum monthly payment: ", round(payment, 2)
        print "Remaining balance: ", round(balance, 2)
    print "Total paid:", round(total, 2)
    print "Remaining balance:", round(balance, 2)
    
#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
def payingDebtOffInAYear(balance, annualInterestRate):
    payment = 0
    b = 1
    while b > 0:
        payment += 10
        b = balance
        for month in range(1, 13):
            b = (b - payment) * (1 + annualInterestRate / 12.0)
            
    print "Lowest Payment:", payment
    
#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly payment lower bound = Balance / 12
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0    
def usingBisectionSearch(balance, annualInterestRate):
    lowBound = balance / 12.0
    highBound = (balance * (1 + annualInterestRate / 12.0)**12) / 12.0
    payment = (highBound + lowBound) / 2.0
    b = balance
    for month in range(1,13):
        b = (b - payment) * (1 + annualInterestRate / 12.0)
    
    while abs(b) > 0.01:
        if b < 0:
            highBound = payment
        else:
            lowBound = payment
        
        payment = (highBound + lowBound) / 2.0
        b = balance
        for month in range(1,13):
            b = (b - payment) * (1 + annualInterestRate / 12.0)
    print "Lowest Payment:", round(payment,2)