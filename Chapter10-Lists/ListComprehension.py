#Program - 28

""" Returns a list of the squares of the numbers in the input. """
def square_list1(numbers):
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result
    
""" Returns a list of the squares of the numbers in the input. """
def square_list2(numbers):
    return [n ** 2 for n in numbers] # loop through every number in numbers & compute their squares & add then to a temporary list which is return at the end of for loop


print square_list1([4, 5, -2])
print square_list2([4, 5, -2])


"""Returns whether the ball is in the desired range. """
def is_in_range(ball):
    return ball[0] >= 0 and ball[0] <= 100 and ball[1] >= 0 and ball[1] <= 100

""" Returns a list of those input balls that are within the desired range. """
def balls_in_range1(balls):

    result = []
    for ball in balls:
        if is_in_range(ball):
            result.append(ball)
    return result
""" Returns a list of those input balls that are within the desired range. """
def balls_in_range2(balls):
    return [ball for ball in balls if is_in_range(ball)] # loop through every number in numbers & add then to a temporary list if they are in range. Return temporary list created at the end of for loop

print balls_in_range1([[-5,40], [30,20], [70,140], [60,50]])
print balls_in_range2([[-5,40], [30,20], [70,140], [60,50]])
