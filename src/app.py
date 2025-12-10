#!/bin/python
import math

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mult (a, b):
    return a*b

def div (a, b):
    if(b==0):
        return None
    return a/b

def log (a):
    if(a<=0):
        return None
    return math.log(a)