# 4 questions in this assignment.

# Note: When guessing output, try not to print before guessing
# This will help you understand the logic behind the code

import random

# Question 1
"""
Try and Understand what this program does and why I chose dictionary for this program
Then Run the program to see if the output is what you had expected.

"""

SOCCER_PLAYERS = "Steven,Gerrard \n Cristiano,Ronaldo \n Lionel,Messi \n Bastian,Schweinsteiger "
PLAYER_BY_NAME = {}

def build_dict(string):
    global PLAYER_BY_NAME
    temp_list = string.split('\n')
    for line in temp_list:
        (key, value) = (line.split(','))
        PLAYER_BY_NAME[key.strip()] = value
    return PLAYER_BY_NAME

PLAYER_BY_NAME = build_dict(SOCCER_PLAYERS)
print PLAYER_BY_NAME

"""
Write a function that calls the above function.
Print a list of keys for the dictionary
Print a list of each key-value pair in the dictionary
If you observe the printed dictionary carefully, you'll notice trailing white space
in the values for each key. Use a for loop and remove white space for each value
"""

# Question 2
"""
Try and Understand what the following function does and how it is called
"""

ANSWER = "clint"
FIRST_NAME = "clint"
LAST_NAME = "dempsey"

def chk_ans(first, answer):

    if answer == first:
        print "You're right!"
    else:
        print "wrong"

chk_ans(FIRST_NAME, ANSWER)

"""
Create a list of first names of players from the above soccer dictionary
Create a list of last names of players from the above soccer dictionary

Create another function:
    Randomly select a last name from LAST_NAME list. Use random.choice
    Ask a question: What is the first name of last_name_selected
    You need to match index of last_name to correct first name. Use LAST_NAME.index(random lastname)
    Create variable that gets the correct first name for this player. FIRST_NAME[index_no]
    Now call chk_ans from inside this function

Modify chk_ans to also tell us if answer is wrong and in that case, print correct answer
"""

# Question 3
"""
A neater implementation of the process above is to directly work with dictionaries in case
of pairs
"""

cars = {"Toyota": ["Prius", "Camry"], "Honda": ["Accord", "Civic"], "Nissan": ["Altima", "Leaf"]}

def random_key(dictionary):
    brand = random.choice(cars.keys())
    return brand

brand = random_key(cars)
print brand

"""
Create a function and enclose the above random_key call in it.
Ask user to name a car from the brand randomly chosen
Iterate over list of car names for the brand and if the answer matches,
print appropriate message
Hint: Use for loop to iterate over values. Get values using .get(brand)
Don't forget to convert strings to .lower()
"""

# Question 4 (OPTIONAL: DO IT IF YOU LIKE MATH)

"""
One of the advantages about a higher level language like Python is that many
functions are inbuilt and we simply learn to use them.
Sometimes, it is important to try and understand what really happens under some of
these functions

Let's understand the modulo operator in Python "%"
We are going to implement a function that replicates the result of %.
For now, we assume that the pre-built % doesn't exist.

Like we saw in our first session, % is used to print remainder of a division.
One of it's most popular application is our 12 hour clock. When time changes to 13, 14...etc
it prints 1, 2,...

%'s output however, is tricky to understand when it comes to negative numbers.
First print 5%2, 7%3 to see if you understand how % works.
Now print -7%3. Did you expect this answer?
In case of negative numbers, the simplest way to understand % is, it rounds the divisor
(in our case, 3) to the closest possible number to positive(dividend) that is divisible 
by 3 and greater than dividend and returns the difference between this number and 
our dividend(7)
i.e. we convert -7 to 7. Closest number divisible by 3 and > 7 is 9. 9 - 7 is 2.
Therefore, -7 % 3 is 2
It's actual mathematical implementation is:
new_no = ceiling of -7/3.0 (-2 is the answer. -2.33335 rounded up to -2)
mod = (abs(new_no) + 1) * 3 + (-7)

Yeah... it's tricky and really hard to grasp, but that's what it is.
Let's try a few examples and then implement the mod function.
"""
import math

print "7/3 is", 7/3   # 7 is the dividend, 3 is the divisor
print "7%3 is", 7%3
print "-7%3 is", -7%3
print "Absolute value of -5 is, ", abs(-5)

# math.floor rounds up a floating number to closest lower integer
# math.ceil rounds up a floating number to closest higher integer
print "7/3.0 is", 7/float(3)
print "7/3.0 to the floor is", math.floor(7/float(3))
print "7/3.0 to the ceiling is", math.ceil(7/float(3))

"""
Now try replacing 7 with -7 and see the results
"""
def implement_mod(dividend, divisor):
    """
    Write an if loop that will handle cases if dividend < 0
    and an else loop that handles other cases
    if dividend is > 0
    mod will be the remainder of a regular division
    """
    pass
