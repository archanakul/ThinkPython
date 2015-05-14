#PROGRAM - 8

""" 
1. Operands of LOGICAL OPERATORS should be BOOLEAN expressions (True/False - bool type)
2. Any NON-ZERO number is considered as True by python
3. OR is a LOGICAL OPERATOR where the output is TRUE if either of the inputs are true else output is FALSE. Python also provides AND & NOT bitwise operators.
4. PASS Statement - Ideally, each if condition needs to have at-least one indented statement as part of its body but sometimes its useful to reserve it for later, use a PASS statement in such case which does nothing
5. CHAINED CONDITIONS - Even when more than one condition is true, only the first true branch gets executed hence need to be careful about the order of the conditional checks.  
"""

s = raw_input("Enter a score between 0.0 & 1.0:")
try:
    score = float(s)
except:
    print "Enter a numeric score value!!"
    quit()

if (score < 0.0) or (score > 1.0):
    pass
elif score >= 0.9:
    print "Your grade is A"
elif score >= 0.8:
    print "Your grade is B"    
elif score >= 0.7:
    print "Your grade is C" 
elif score >= 0.6:
    print "Your grade is D" 
elif score < 0.6:
    print "Your grade is F"         