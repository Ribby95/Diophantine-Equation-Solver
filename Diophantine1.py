# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
a=17
b=12
c=58
def bezout(a,b):
    old_remainder=max(a,b)
    new_remainder=min(a,b)

    old_first_coefficient=1
    new_first_coefficient=0

    old_second_coefficient=0
    new_second_coefficient=1

    while new_remainder!=0:
        quotient=old_remainder//new_remainder
        old_remainder,new_remainder=new_remainder,old_remainder-quotient*new_remainder
        old_first_coefficient,new_first_coefficient=new_first_coefficient,old_first_coefficient-quotient*new_first_coefficient
        old_second_coefficient,new_second_coefficient=new_second_coefficient,old_second_coefficient-quotient*new_second_coefficient
    return (old_remainder,old_first_coefficient,old_second_coefficient,new_first_coefficient,new_second_coefficient) #GCD, 

def both_positive(x,y):
    return x*abs(y)+abs(x)*y>0

def frobenius(a,b):
    return a*b-a-b

def solver(coefficients,answer):
    B=bezout(coefficients[0],coefficients[1])
    xnot=B[1]*c/B[0]
    ynot=B[2]*c/B[0]
    Upper_bound=xnot*B[0]/coefficients[1]
    lower_bound=-ynot*B[0]/coefficients[0]
    for m in range(math.floor(lower_bound),math.ceil(Upper_bound)):
        solution_x=xnot+m*B[3]
        solution_y=ynot+m*B[4]
        if both_positive(solution_x,solution_y):
            return (solution_x,solution_y)

def slosher(coefficients,solution,answer):
    if sum([coefficients[i]*coefficients[i]  for i in range(0,len(coefficients))])!=answer:
        return "try again"
    temp=dict(zip(coefficients,solution))

def brute_force_recursive(coefficients,answer):
    solution_list=[]
    limits=[math.floor(answer/a) for a in coefficients]
    base=[0 for a in coefficients]
    def update(original,index,bounds=limits):
            if original[index]+1<=bounds[index]:
                original[index]=original[index]+1
            else:
                original[index]=0
                if index+1<len(original):
                    update(original,index+1,bounds)
            return original
    for i in range(0,math.prod([x+1 for x in limits])):
        if sum([base[j]*coefficients[j] for j in range(0,len(coefficients))])==answer:
            solution_list.append(base)
        base=update(base,0,limits)
    return solution_list
print(brute_force_recursive([3,5],18))
#print(B[1]*a+B[2]*b)
#print(solver([a,b],c))