#PROGRAM - 14

"""
    1. Body of the loop should change value of one or more variables so that the loop condition eventually becomes false & the loop terminates
"""
total = 0.0
count = 0
while(True): # infinite loop as the loop condition is always true
    input = raw_input("Enter a number: ") 
    try:
        number = float(input)
    except:
        if (input == "Done"):
            break # Terminates encompassing loop in the middle of a iteration
        else:
            print ("Invalid input \n")
            continue #Jumps back to loop iteration condition without executing below  statements for the loop iteration
    total = total + number
    count = count + 1 
          
print "Count =", count
print "Total =", total
print "Average =", total/count                

    