#PROGRAM - 25

"""
    1. LISTS: Sequence of value of any type included within square brackets.
    2. DIR function returns a list of function & methods that can be applied on 
       a data type
    3. LEN function can be used to determine the length of a list
    4. RANGE: Creates a list containing arithmetic progressions. It is most 
       often used in for loops. The arguments must be plain integers. 
       If the step argument is omitted, it defaults to 1. If the start argument 
       is omitted, it defaults to 0
                 range(stop)
                 range(start, stop[, step])
    5. Unlike STRINGS which are NONMUTABLE, LISTS are MUTABLE i.e either value 
       can be modified after being initialized. All other features of lists are 
       same as string like accessing individual elements of the list using 
       INDEXING & also SLICING ([] Bracket OPERATOR)
    6. IN operator also works on LISTS
    7. CONCATINATION(+) and REPETATION(*) operators work just like they do on 
       STRINGS
    8. LIST() is a CONSTRUCTOR that generates an empty list([]) but when a 
       string is passed as a parameter, it returns a list containing each 
       character of the string as its elements
    9. Most LIST METHODS are all void; they modify the list and return NONE.      
       This is exactly opposite to STRING METHODS, which return a new string & 
       leave the original alone
        - APPEND : Add an item to the end of the list
                        list.append(x)
        - EXTEND : Extend the list by appending all the items in the given list
                        list.extend(L)
        - INSERT : Insert an item at a given position. The first argument is the 
                  index of the element before which to insert
                        list.insert(i, x)
        - POP : Remove the item at a given INDEX in the list, & return it. 
                If no index is specified, removes & returns last item of list
                        list.pop([i])
        - REMOVE : Remove the first appearance of VALUE is x. It is an error if 
                   there is no such item 
                        list.remove(x)       
        - COUNT : Return the number of times x appears in the list.
                        list.count(x)
        - INDEX : Return the index of first appearance of value x in the list. 
                  It is an error if there is no such item.
                        list.index(x)
        - REVERSE : Reverse the elements of the list, in place.
                        list.reverse()
        - SORT : Sort the items of the list in place
                        list.sort(cmp=None, key=None, reverse=False)
    10. SUM function adds each elements of the list to produce the result
                total = sum(list) 
    11. DEL is a operator used to delete an item in the list at a given INDEX      
        without. Same as POP except no return value.
                del list[i] or del list[i:j]    
    12. IS operator: used to check if two variables refer to the same OBJECT
        When we have two string variable with same value them they refer to the 
        same OBJECT then they are IDENTICAL i.e value & object are the same but 
        when we have two LIST variables with same list elements then they still 
        hare not referring to same objects hence they are not IDENTICAl; however 
        are EQUIVALENT                                                    
"""
nums = [1,2,3,]
letters =  ['a','b']
floats = [2.3] 
mixed =  [2,'abcd', 34.56, [1,2]]
empty = []

print type(nums), len(nums)
print type(letters), len(letters)
print type(floats), len(floats)
print type(mixed), len(mixed) #nested list still counts as a single element.
print type(empty), len(empty)

print dir(nums)

for item in mixed:
    print item

for i in range(len(mixed)):
    print  mixed[i]   
    
for item in empty:
    print "This is never executed"

new_list = list('456789')
for i in range(4):
    new_list.append(i)  
print new_list 
   
new_list.extend(nums)
print new_list 

new_list.insert(4,10)
print new_list 

print new_list.pop(), new_list 
print new_list.pop(2), new_list 

print new_list.remove(0), new_list 
#print new_list.remove(20), new_list # returns a value error when x is not found

print new_list.count(1)

print new_list.index(10)
#print new_list.index(20), new_list # returns a value error when x is not found
print mixed.sort(), mixed
print new_list.reverse(), new_list

list1 = [1,2,3]
list2 = list()

for i in range(len(list1)):
    list2.append(sum(list1[:i+1]))
print list1, list2  

a = 'archu'
b = 'archu'
print str(a is b) #IDENTICAL strings which are also EQUIVALENT(value)

a = list(a)
b = list(b)
print str(a is b) #EQUEVANLENT list but not IDENTICAL(refer to diff OBJECTS)  

b = a #aliasing, both a & b lists refer to same object
print str(a is b) #IDENTICAL lists!!
    