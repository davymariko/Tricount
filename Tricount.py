#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os
class Transaction:
    '''	Class representing a transaction (un remboursement) between two people
    '''

    def __init__(self, payer, amount, receiver):
        self.payer = payer
        self.amount = amount
        self.receiver = receiver

    def __str__(self):
        return "{} pays {} eur to {}".format(self.payer, round(self.amount,2), self.receiver)

class Tricount:
    '''	Class representing an instance of the problem. It reads a file, the argument is given in the init function
    '''
    def __init__(self, file_path):
    	self.file = file_path

    def balance(self):
        ''' Returns a table (list) of transcation which set the current accounts to zero.
            Attention: the number of Transactions in the table must be less than the number of people who participated in the activity
        '''
        openfile = open(self.file, "r") #reads the file
        self.transactlist = []
        self.balancelist = []
        self.netowned = []
        check = 0
        for i in openfile.readlines():
        	if check == 0:
        		self.transanum = int(i)
        	else:
        		self.transactlist.append(i.strip('\n').split('\t')) #save in a list
        	check += 1
        openfile.close()
        print(self.transactlist)

        for bal in self.transactlist: #faire une liste de 1 à 1 transaction de dette à rembourser
        	length = int(len(bal))
        	amountperid=float(bal[1])/float(length-2)
        	onetransac = []
        	onepaid = []
        	idi=0
        	for ine in range(2,length):
        		if bal[0] == bal[ine]:
        			idi = 1
        			amountnet = amountperid - (float(bal[1]))
        			onetransac = [int(bal[ine]),amountnet]
        			self.balancelist.append(onetransac)
        		else:
        			onetransac = [int(bal[ine]),amountperid]
        			self.balancelist.append(onetransac)
        	if idi != 1:
        		amountpaid=-(float(bal[1]))
        		onepaid = [int(bal[0]),amountpaid]
        		self.balancelist.append(onepaid)
        self.balancelist.sort()
        # print("BALANCE")
        # print(self.balancelist)

        for owe in self.balancelist: #list of net debt
        	net = 0
        	if (len(self.netowned) == 0):	 #empty list at the beginning
        		self.netowned.append(owe)
        	else:
        		if(self.netowned[-1][0] == owe[0]):    #check if the last id in the list does not match the current balancelist id and change the sum
        			net = self.netowned[-1][1] + owe[1]
        			self.netowned[-1][1] = net
        		else:                                   #if this is not the case we append to the list
        			self.netowned.append(owe)

        self.netowned.sort(key=lambda x:x[1])
        self.netowned.reverse()
        # print("NET")
        # print(self.netowned)
        self.remisezero = []
        num = 0
        for zero in range(len(self.netowned)):
        	if self.netowned[zero][1] == 0 or self.netowned[zero][1]<0:
        		break
        	if self.netowned[zero][1] > 0:
        		for ozer in range(len(self.netowned)-1,-1,-1):
        			if self.netowned[ozer][1] < 0 and self.netowned[zero][1] != 0:
        				if int(self.netowned[zero][1]+self.netowned[ozer][1]) == 0:
        					self.repay = Transaction(self.netowned[zero][0],-self.netowned[ozer][1],self.netowned[ozer][0])
        					self.remisezero.append(self.repay)
        					self.netowned[zero][1] = 0
        					self.netowned[ozer][1] = 0
        				elif self.netowned[zero][1]+self.netowned[ozer][1] < 0:
        					num = self.netowned[zero][1]+self.netowned[ozer][1]
        					self.repay = Transaction(self.netowned[zero][0],self.netowned[zero][1],self.netowned[ozer][0])
        					self.remisezero.append(self.repay)
        					self.netowned[zero][1] = 0
        					self.netowned[ozer][1] = num
        				elif self.netowned[zero][1]+self.netowned[ozer][1] > 0:
        					num = self.netowned[zero][1]+self.netowned[ozer][1]
        					self.repay = Transaction(self.netowned[zero][0],-self.netowned[ozer][1],self.netowned[ozer][0])
        					self.remisezero.append(self.repay)
        					self.netowned[zero][1] = num
        					self.netowned[ozer][1] = 0

        return self.remisezero

if __name__ == '__main__':
    '''	This simple test aims to make it easier for you to validate the result of the work.
        Those who want to do a more robust verification of the solution are invited
        to write a test suite with the `unittest` (or` nose`) module of python.
    '''

    instance = Tricount("ex2.txt")
    result = instance.balance()
    print('\n')
    print(result)
    print("The number of transactions that need to take place are: {}".format(len(result)))
    if len(result) > 0:
        print("Transactions Made: ")
        for t in result:
            print(t)
    # os.remove("smallExample.txt")
