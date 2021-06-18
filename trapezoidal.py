from numpy.lib.scimath import logn
from math import e
from logic import *
from tabulate import tabulate

def velocity(time):
    u=2000
    q=2100
    m0=140000
    g=9.8
    return u*logn(e,m0/(m0-q*time))-g*time

trueVal=11061.33554
t1=8
t2=30






def showTable(func):
    tableData = [['n', 'value', 'Et', 'et %', 'ea %']]
    prevVal=0
    for i in range(1, 6):
        val = func(velocity, t1, t2, i)
        et=trueVal-val
        etP=abs(et/trueVal)*100
        eaP='----'
        if i>1:
            eaP=abs((prevVal-val)/val)*100
        tableData.append([i, val, et,etP,eaP])
        prevVal=val
    print(tabulate(tableData, headers='firstrow', tablefmt='fancy_grid'))


def execute(n):
    print("trapezoidal rule : "+str(trapezoid(velocity,t1,t2,n)))
    showTable(trapezoid)
    print("simpsons rule : " + str(simpsons(velocity, t1, t2, n)))
    showTable(simpsons)

print("Enter n:")
execute(int(input()))