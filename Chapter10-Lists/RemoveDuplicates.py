#PROGRAM - 32

def remove_duplicates(lst):
    """ Takes a list & returns a new list with only the unique elements from the 
        original """
	new_lst = list()
	for item in lst:
		if item not in new_lst:
			new_lst.append(item)
	return new_lst
	
print remove_duplicates([1,2,3,2,1,4,2])	