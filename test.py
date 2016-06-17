import random
from numpy import *

def suangua():
    total=[49,0,0,0]
    table=[]	
    for j in range(6):
        i=0
        while i<=2:
            a_1=random.randint(1,total[i])
            b_1=total[i]-a_1
            k_1=random.randint(0,1)
            if	k_1==0:
                a_1=a_1-1
            else:
                b_1=b_1-1
            c_1=a_1%4
            if	c_1==0:
                c_1=4
            else:
                c_1=c_1
            d_1=b_1%4
            if	d_1==0:
                d_1=4
            else:
                d_1=d_1
            total[i+1]=total[i]-c_1-d_1-1
            i=i+1
        #if total[-1]/4==6:
            #print "-  -"
        #if	total[-1]/4==8:
            #print "-  -"
        #if	total[-1]/4==7:
            #print "----"
        #if	total[-1]/4==9:
            #print "----"
        table.append(total[-1]/4)
    return table


store=[]
for i in range(1000000):
    temp = suangua()
    store.append(temp)

#print store

number6=0
number7=0
number8=0
number9=0
for i in range(1000000):
    for j in range(6):
        if store[i][j]==6:
            number6=number6+1
        if store[i][j]==7:
            number7=number7+1
        if store[i][j]==8:
            number8=number8+1
        if store[i][j]==9:
            number9=number9+1
print number6
print number7
print number8
print number9




