#!/bin/python3

import math
import os
import random
import re
import sys


def choose_job(start_time,end_time,profit,n):
    #  code here
    s=0
    
    
 
    for i in range (0,n):
        if (start_time[i]==start_time[i+1]):
            for j in range (0,n):
                for k in range (0,n):
                    if (profit[j]>profit[k]):
                        a= profit[j]
                        profit[k]=profit[j]
                        profit[j]=a
            return profit[0]
        else :
            s+=profit[0]
            for l in range (0,n):
                if(end_time[l]< start_time[l+1]):
                    s+=profit[l+1]
            return s

    
            
if __name__ == '__main__':
    start_time = [1,1,1]
    end_time = [2,3,4]
    profit = [5,6,4]

    
    n = int(input("Enter number of elements : "))

    result = choose_job(start_time,end_time,profit,n)
    
    print(result)
    
    print('\n')

    
