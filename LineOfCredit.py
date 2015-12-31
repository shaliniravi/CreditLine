# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:17:24 2015

@author: Shalini
"""

import math

#==============================================================================
# This program is an API used for Credit card Application. 
#(Except there is no credit card)
#==============================================================================

class LineOfCredit(object):
    def __init__(self, apr=0.0, creditLimit=0.0):

        if apr > 0 and creditLimit > 0:
            self.apr = apr
            self.creditLimit = creditLimit
            self.currentOwed  = 0.0     # current amount to be paid (without interest)
            self.interest = {}          # cache holds the previous interest
            self.transactions = {}      # holds day as key with transaction details as value
            self.currentPayoff = 0.0    # current amount to be paid (with interest)


            print ("\nCongratulations !! Your Credit Line has been created with LIMIT = ", self.creditLimit, " and APR = ", apr)

        else:
            print ("Please check the APR or the Amount(limit)!!")

    # returns: current balance
    def getOutStanding(self):
        return self.currentOwed

    # returns: credit limit
    def getCurrentLimit(self):
        return self.creditLimit

    # This method perform withdraw functionality
    def withdraw(self, amount, day):
        if amount > 0 and amount <= self.creditLimit:
            self.creditLimit = self.creditLimit - amount;
            self.currentOwed  = self.currentOwed  + amount;
            self.recordTransactions(-amount, day,self.creditLimit, self.currentOwed )
            print ( "\n************** TRANSACTION RECEIPT **************")
            print ( "Day = ", day)
            print ( "Amount withdrew = ", amount)
            print ( "Your Current Credit Limit = ", self.creditLimit)
            print ( "Your Out Standing Balance = ", self.currentOwed )
            return True

        else:
            print ( "Please check the Amount you are trying to withdraw!!")
            return False

    # This method perform make payment functionality
    def makePayment(self, amount, day):
        if amount > 0 and amount <= self.currentOwed :
            self.creditLimit = self.getCurrentLimit() + amount;
            self.currentOwed  = self.getOutStanding() - amount;
            self.recordTransactions(amount, day,self.creditLimit, self.currentOwed )
            print ( "\n************** TRANSACTION RECEIPT **************")
            print ( "Day = ", day)
            print ( "Amount Paid = ", amount)
            print ( "Your Out Standing Balance = ", self.currentOwed )
            print ( "Your Current Credit Limit = ", self.creditLimit)
            return True

        else:
            print ( "Please check the Amount you are trying to Pay!!")
            return False

    # This method records every transactions
    def recordTransactions(self, amount, day, credit, balance):
        if (day in self.transactions):
            self.transactions[day][0].extend([amount])   
            self.transactions[day][1] = credit
            self.transactions[day][2] = balance

        else:
            # In case of several transactions per day, 
            # the transactions will be saved as list of list.
            self.transactions[day] = [[amount] , credit, balance]


    # This is a helper method which shows the transaction history 
    # happend on a particular day.
    def getTransactionHistory(self, day, flag = False):
        if (day in self.transactions):
            lenght = len(self.transactions[day][0])
            if lenght > 1 and flag == False:
                while (lenght > 0) :
                    lenght = lenght -1
                    self.displayTransaction(self.transactions[day][0][lenght],day)
            elif lenght <=1 or flag == True :
                self.displayTransaction(self.transactions[day][0][0],day)

        else:
            print ( "\nNo Transaction has been happened on the given day!! ")


    # Display a amount paid /with drew on a particular day
    def displayTransaction(self,amount, day):
            if amount < 0:
                print ( "\nDay = ", day,"  Amount Withdrew = ", amount)
            elif amount > 0:
                print ( "\nDay = ", day,"  Amount Paid = ", amount)
            else:
                self.displayStatement()
    
    # This method is an edge case in case something is off    
    def displayStatement(self):
        print ( "Your Out Standing Balance = ", self.getOutStanding())
        print ( "Your Current Credit Limit = ", self.getCurrentLimit())
    
 
   # returns: current payoff
    def getCurrentPayOff(self):
        #print ( "Your Current Pay Off = ", self.currentPayoff)
        return self.currentPayoff
    
    # This method displays first N Transactions    
    def showfirstNActivity(self, n):
        self.checkN(True, n)

    # This method displays last N Transactions
    def showLastNActivity(self, n):
        self.checkN(False, n)
    
    # This method checks for the transaction count and
    # call respective method to display the transaction history    
    def checkN(self, type, n):
        if n == 0:
            print ( "No Activity has been recorded so far!!")
        elif n == 1:
            self.getTransactionHistory(self.transactions.keys()[0],True)
        elif n > 1 and len(self.transactions) >= n:
            self.showStatement(type, n)
        else:
            for i in range(len(self.transactions)):
                self.getTransactionHistory(self.transactions.keys()[i], True)

    # This method sorts the dictionary based on its keys
    # and shows the transaction history either last or first N
    def showStatement(self, type, n):
        count = 0
        if type is True:
            term = "First"
            keySet = sorted(self.transactions.keys())
        else:
            term = "Last"
            keySet = sorted(self.transactions.keys(), reverse=True)
        print ( "\n ******* The ", term, " ", n, " Activities Listed *******")
        while (count < n):
            self.getTransactionHistory(keySet[count], True)
            count += 1

    # returns: credit limit on a particular day(past).
    def getCreditLimitOn(self,day):
        if day in self.transactions:
            print ( "\nCredit Limit on day - ",day, " = ",self.transactions[day][1])
            return self.transactions[day][1]
        else :                  
            print ("\n Sorry. Wrong Entry !!")
     
    # returns: balance on a particular day(past).       
    def getBalanceOn(self,day):
        if day in self.transactions:
            print ( "\nPrinciple Balance on day - ",day, " = ",self.transactions[day][2])
            return self.transactions[day][2]
        else :                  
            print ("\n Sorry. Wrong Entry !!")
    
    # This method calculates interest
    def calculateInterest(self, amount, days):
        interest = 0.0
        interest = amount * (self.apr / 365) * days
        # rounding to 2 decimal points
        interest = float("{0:.2f}".format(interest))
        #print ( "Interest = ",interest)
        return interest

    
    def getTransactionOn(self, day):
        if day in self.transactions:
            print ( "\n************** TRANSACTION HISTORY FOR DAY = ",day ," **************")
            self.getTransactionHistory(day, False)
        else :                  
            print ("\n Sorry. Wrong Entry !!")

    # returns: Total Pay off amount.       
    def getTotalPayOffAmnt(self,day):
        if day in self.interest:
            payoff = self.interest[day]
        elif (len(self.interest) > 0) :
            keySet = sorted(self.interest.keys(), reverse=True)
            if day < keySet[0]:
                payoff =  self.interest[keySet[0]]
            else:
                payoff = self.getPayOffAmnt(day)
        else:
           payoff = self.getPayOffAmnt(day)
        print  ( "\nYour Total Pay Off = ",payoff)



#==============================================================================
#  This method calculates pay off amount:
#  
#==============================================================================
    def getPayOffAmnt(self,day):

            interest = 0.0
            last_balance = 0.0
            # finds the 30 day window based on the given day
            payment_period = math.ceil(day/30) *30 - 29
            #print ("\nDay = ",day , "payment_period = ",payment_period)
            # the payment period start from the first day of the 30 day window
            # if there was any transaction happend on day 1 on the window, then
            # last balance will the balance recorded on that day else it will be zero
            if payment_period in self.transactions :
                last_balance = self.transactions[payment_period][2]
            # take the previous interest cached if any    
            if payment_period-1 in self.interest:
                interest = self.interest[payment_period - 1]
                last_balance = 0   
            last_day = payment_period - 1
            #loop throught the last payment period to the given day
            for i in range(payment_period, day+1):
                  if i in self.transactions :
                    #ignore the day one calculation  
                    if i != (payment_period-1):
                        #print ("i = ",i , "amount = ",self.transactions[i][2], "i - lastday = ",i-last_day)
                        interest = interest + self.calculateInterest(last_balance, i-last_day)
                        last_day = i
                        last_balance = self.transactions[last_day][2]
                        #print ("last_day = ",last_day)
                        #print ("Interest = ",interest)
            
            # if we dont have any transaction after the last payment calculation period
            # then payoff will remain same as previous             
            if(last_balance != 0) :
                #print ("Interest = ",interest , "amount = ",self.getOutStanding(), "day - lastday = ",day-last_day)
                interest = interest + self.calculateInterest(self.getOutStanding(), day - last_day)
                payoff = self.getOutStanding() + interest
                #cache the result
                if day % 30 == 0 :
                    self.interest[day] = payoff
                self.currentPayoff= payoff
            else:
                payoff = self.getCurrentPayOff()
            #print ("Payoff = ",payoff)
            return payoff


