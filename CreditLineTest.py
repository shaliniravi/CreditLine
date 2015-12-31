# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 03:40:37 2015

@author: Shalini
"""


from LineOfCredit import *
#==============================================================================
# Testing the Credit Line API - Scenario 1 and 2
#==============================================================================
APR = 0.35
CREDIT_LIMIT = 1000

print ("\n ===============Scenario 1 =============== ")

case1 = LineOfCredit(APR,CREDIT_LIMIT)
case1.withdraw(500,1)
case1.getTotalPayOffAmnt(30)

print ("\n\n ===============Scenario 2 =============== ")
case2 = LineOfCredit(APR,CREDIT_LIMIT)
case2.withdraw(500,1)
case2.makePayment(200,15)
case2.withdraw(100,25)
case2.getTotalPayOffAmnt(30)


print ("\n\n ===============Edge Cases =============== ")
case2.getTotalPayOffAmnt(23) #already calculated for 30th day 
case2.getTotalPayOffAmnt(33) # no actvity after the 1st pay cycle


print ("\n\n =============== Other Tests =============== ")
case3 = LineOfCredit(APR,CREDIT_LIMIT)
case3.withdraw(100,1)
case3.makePayment(100,2)
case3.getTransactionHistory(7)
case3.withdraw(100,3)
case3.makePayment(100,3)
case3.withdraw(100,4)
case3.makePayment(100,6)
case3.withdraw(100,7)
case3.makePayment(100,10)
case3.showfirstNActivity(3)
case3.showLastNActivity(4)
case3.getCreditLimitOn(4)
case3.getBalanceOn(3)
case3.getTransactionOn(3) #display all the transactions happened on the particular day


