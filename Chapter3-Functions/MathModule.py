#PROGRAM - 7

"""
    1. MODULE is a file that contains collection of related functions which need 
       to be imported before being used. Ex: math
    2. MODULE OBJECT contrains variables & functions defined in the module
    3. To access a functions of a module, specify the name of the module & the 
       name of the function, separated by a dot (also known as a period)
"""    

import math # creates a MODULE OBJCET

signal_power = raw_input("Enter a number for Signal Power: ")
noise_power = raw_input("Enter a number for Noise Power: ")
ratio = float(signal_power)/float(noise_power) 
decibels =  10 * math.log10(ratio)

print "signal to noise ratio in decibels:", decibels

degree = raw_input("Enter angle in degree: ")
radians = (float(degree)/360.0) * 2* math.pi
print "Sin theta value :", math.sin(radians)
